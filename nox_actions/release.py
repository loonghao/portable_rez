# Import built-in modules
import argparse
import os
import shutil
import zipfile

# Import third-party modules
import nox

from nox_actions.utils import PACKAGE_NAME, THIS_ROOT


@nox.session(name="build-exe", reuse_venv=True)
def build_exe(session: nox.Session) -> None:
    parser = argparse.ArgumentParser(prog="nox -s build-exe --release")
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--version", default="0.5.0", help="Version to use for the zip file")
    args = parser.parse_args(session.posargs)
    build_root = THIS_ROOT / "build" / "x86_64-pc-windows-msvc" / "release" / "install"
    session.install("pyoxidizer")
    session.run("pyoxidizer", "build", "install", "--path", THIS_ROOT, "--release")
    rez_exe = build_root / "portable_rez.exe"
    rez_exe.rename(build_root / "rez.exe")

    if args.release:
        temp_dir = os.path.join(THIS_ROOT, ".zip")
        shutil.rmtree(temp_dir, ignore_errors=True)
        version = str(args.version)
        print(f"make zip to current version: {version}")
        os.makedirs(temp_dir, exist_ok=True)
        zip_file = os.path.join(temp_dir, f"{PACKAGE_NAME}-{version}.zip")
        with zipfile.ZipFile(zip_file, "w") as zip_obj:
            for root, _, files in os.walk(build_root):
                for file in files:
                    zip_obj.write(os.path.join(root, file),
                                  os.path.relpath(os.path.join(root, file),
                                                  os.path.join(build_root, ".")))
        print("Saving to {zipfile}".format(zipfile=zip_file))
