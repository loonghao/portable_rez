# Import built-in modules
import argparse
import os
import shutil
import subprocess
import zipfile

# Import third-party modules
import nox
from nox_actions.utils import PACKAGE_NAME
from nox_actions.utils import THIS_ROOT


@nox.session(name="build-exe", reuse_venv=True)
def build_exe(session: nox.Session) -> None:
    parser = argparse.ArgumentParser(prog="nox -s build-exe --release")
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--version", default="0.5.0", help="Version to use for the zip file")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args(session.posargs)
    build_root = THIS_ROOT / "build"
    binary_name = "portable_rez.exe" if os.name == "nt" else "portable_rez"
    rez_binary_name = "rez.exe" if os.name == "nt" else "rez"
    session.install("pyoxidizer")
    session.run("pyoxidizer", "build", "install", "--path", THIS_ROOT, "--release")
    for platform_name in os.listdir(build_root):
        platform_dir = build_root / platform_name / "release" / "install"
        print(os.listdir(platform_dir))
        print(f"build {platform_name}")
        print(f"rename {binary_name} to {rez_binary_name}")
        rez_exe = platform_dir / binary_name
        rez_exe.rename(platform_dir / rez_binary_name)

        if args.test:
            print("run tests")
            subprocess.check_call(["rez", "--help"], cwd=platform_dir)

        if args.release:
            temp_dir = os.path.join(THIS_ROOT, ".zip")
            shutil.rmtree(temp_dir, ignore_errors=True)
            version = str(args.version)
            print(f"make zip to current version: {version}")
            os.makedirs(temp_dir, exist_ok=True)
            zip_file = os.path.join(temp_dir, f"{PACKAGE_NAME}-{version}-{platform_name}.zip")
            with zipfile.ZipFile(zip_file, "w") as zip_obj:
                for root, _, files in os.walk(platform_dir):
                    for file in files:
                        zip_obj.write(os.path.join(root, file),
                                      os.path.relpath(os.path.join(root, file),
                                                      os.path.join(platform_dir, ".")))
            print("Saving to {zipfile}".format(zipfile=zip_file))
