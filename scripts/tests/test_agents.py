"""The agent roster (project/AGENTS.md) matches .claude/agents and .claude/skills (GR-5.1)."""
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def front(path: Path) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    return yaml.safe_load(m.group(1)) if m else {}


class Roster(unittest.TestCase):
    def roster(self) -> list[str]:
        text = (ROOT / "project/AGENTS.md").read_text(encoding="utf-8")
        return re.findall(r"^\| `([a-z\-]+)` \|", text, re.M)

    def test_every_rostered_agent_has_a_definition_and_a_skill(self):
        names = self.roster()
        self.assertEqual(len(names), 9)
        self.assertEqual(sorted(p.stem for p in (ROOT / ".claude/agents").glob("*.md")), sorted(names))
        for name in names:
            agent = front(ROOT / ".claude/agents" / f"{name}.md")
            self.assertEqual(agent.get("name"), name)
            self.assertTrue(agent.get("description") and agent.get("tools"), name)
            skill = ROOT / ".claude/skills" / name / "SKILL.md"
            self.assertTrue(skill.exists(), name)
            self.assertEqual(front(skill).get("name"), name)
            self.assertIn(f".claude/skills/{name}/SKILL.md", (ROOT / ".claude/agents" / f"{name}.md").read_text(encoding="utf-8"))

    def test_reviewers_cannot_edit_and_the_source_researcher_cannot_run_commands(self):
        for name in ("confidentiality-reviewer", "accuracy-reviewer", "editorial-reviewer"):
            tools = str(front(ROOT / ".claude/agents" / f"{name}.md")["tools"])
            self.assertNotIn("Edit", tools, name)
            self.assertNotIn("Write", tools, name)
        source = (ROOT / ".claude/agents/source-researcher.md").read_text(encoding="utf-8")
        self.assertIn("scratchpad", source)
        tools = str(front(ROOT / ".claude/agents/source-researcher.md")["tools"])
        self.assertNotIn("Bash", tools)  # no git, so nothing it reads can be committed by it

    def test_the_main_session_orchestrates(self):
        text = (ROOT / ".claude/skills/section-pipeline/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("The main session orchestrates", text)
        for path in (ROOT / ".claude/agents").glob("*.md"):
            self.assertNotRegex(path.read_text(encoding="utf-8"), r"(?i)\bhand (?:off|the)\b", path.name)

    def test_reviewer_skills_end_with_a_reviewer_verdict_not_a_record_verdict(self):
        for name in ("confidentiality-reviewer", "accuracy-reviewer", "editorial-reviewer"):
            text = (ROOT / ".claude/skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("Reviewer verdict: ACCEPT", text)
            self.assertFalse(re.search(r"^Verdict:", text, re.M), name)


if __name__ == "__main__":
    unittest.main()
