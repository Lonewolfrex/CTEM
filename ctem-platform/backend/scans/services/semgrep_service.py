import json
import shutil
import subprocess
import tempfile

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RULE_FILE = (
    BASE_DIR
    / "config"
    / "semgrep"
    / "ctem-rules.yaml"
)


def run_semgrep_scan(repo_url):

    workdir = tempfile.mkdtemp()

    try:

        repo_dir = Path(workdir) / "repo"

        subprocess.run(
            [
                "git",
                "clone",
                repo_url,
                str(repo_dir)
            ],
            check=True
        )

        report_file = Path(workdir) / "semgrep.json"

        subprocess.run(
            [
                "semgrep",
                "--config",
                "p/owasp-top-ten",
                "--config",
                "p/security-audit",
                "--config",
                "p/secrets",
                "--json",
                "--output",
                str(report_file),
                str(repo_dir)
            ],
            check=False
        )

        if not report_file.exists():
            return {"results": []}

        with open(report_file) as fp:
            return json.load(fp)

    finally:

        shutil.rmtree(
            workdir,
            ignore_errors=True
        )