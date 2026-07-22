from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "deploy-pages.yml"


class PagesWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.source = WORKFLOW.read_text(encoding="utf-8")
        validate_start = self.source.index("\n  validate:\n")
        deploy_start = self.source.index("\n  deploy:\n")
        self.validate_job = self.source[validate_start:deploy_start]
        self.deploy_job = self.source[deploy_start:]

    def test_validation_uses_python_3_9_and_the_complete_standard_library_suite(self):
        self.assertIn("python-version: \"3.9\"", self.validate_job)
        self.assertIn(
            "python3 -m unittest discover -s tests -p 'test_*.py'",
            self.validate_job,
        )

    def test_generated_artifacts_are_checked_without_rebuilding(self):
        self.assertIn("python3 tools/build.py --check", self.validate_job)
        self.assertNotIn("python3 tools/build.py\n", self.validate_job)

    def test_pages_deployment_requires_the_validation_job(self):
        self.assertIn("needs: validate", self.deploy_job)
        self.assertIn("contents: read", self.deploy_job)
        for action in (
            "actions/configure-pages@v5",
            "actions/upload-pages-artifact@v3",
            "actions/deploy-pages@v4",
        ):
            with self.subTest(action=action):
                self.assertNotIn(action, self.validate_job)
                self.assertIn(action, self.deploy_job)

    def test_workflow_installs_no_project_packages(self):
        for command in ("pip install", "npm install", "npm ci"):
            with self.subTest(command=command):
                self.assertNotIn(command, self.source)


if __name__ == "__main__":
    unittest.main()
