import zipfile
import os
import datetime
import argparse

def get_files_to_export():
    folders = ["app", "sheme", "preview", "docs", "plugins"]
    files = [
        "app.py",
        "Dockerfile",
        "docker-compose.yml",
        "HelmChart.yaml",
        "k8s_deploy.yml",
        "README.md",
        "CHANGELOG.md"
    ]
    all_files = []

    for folder in folders:
        for root, _, filenames in os.walk(folder):
            for f in filenames:
                all_files.append(os.path.join(root, f))

    for f in files:
        if os.path.exists(f):
            all_files.append(f)

    return all_files

def export_project(ci_mode=False):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "projekat_" + timestamp + (".zip" if not ci_mode else "_ci.zip")

    with zipfile.ZipFile(filename, "w") as zipf:
        for fpath in get_files_to_export():
            zipf.write(fpath)

    print(f"Projekat exportovan u: {filename}")
    return filename

# CLI opcija za CI
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ci-mode", action="store_true")
    parser.add_argument("--cloud-build", action="store_true")
    args = parser.parse_args()

    export_project(ci_mode=args.ci_mode)