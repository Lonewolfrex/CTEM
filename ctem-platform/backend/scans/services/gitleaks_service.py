import json
import shutil
import subprocess
import tempfile

from pathlib import Path


def run_gitleaks(repo_url):

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

        report_file = Path(workdir) / "gitleaks.json"

        subprocess.run(
            [
                "gitleaks",
                "detect",
                "--source",
                str(repo_dir),
                "--report-format",
                "json",
                "--report-path",
                str(report_file)
            ],
            check=True
        )

        if not report_file.exists():
            return []

        with open(report_file) as fp:
            return json.load(fp)

    finally:

        shutil.rmtree(
            workdir,
            ignore_errors=True
        )