# build
import subprocess
import os
import glob
import io

ROOT = os.path.dirname(__file__)


def build_portable_rez():
    cmd = [
        "pyoxidizer",
        "build",
        "--path",
        ROOT
    ]
    subprocess.call(cmd)


def read_file(path):
    """Read the file content."""
    with io.open(path, "r", encoding="utf-8") as file_:
        content = file_.read()
    return content


def write_file(path, content):
    """Write the file content."""
    with io.open(path, "w", encoding="utf-8", newline="\n") as file_:
        file_.write(content)


def patch_file(source, target, key_values, report_error=True):
    """Modify file with key value pairs."""
    key_values = key_values if key_values else {}
    found_keys = []
    file_data = read_file(source)
    for key, value in key_values.items():
        before_ = file_data
        file_data = file_data.replace(key, value)
        if before_ != file_data:
            found_keys.append(key)
    write_file(target, file_data)

    if report_error:
        not_found = list(set(key_values.keys()) - set(found_keys))
        if not_found:
            raise IndexError("Not found: {0}".format(not_found))


def patch_rez():
    """Patch rez.
    
    https://github.com/AcademySoftwareFoundation/rez/pull/1359

    """
    dst_rez_pattern = os.path.join(ROOT, "build", "**", "site-packages")
    for path in glob.iglob(dst_rez_pattern, recursive=True):
        plugin_managers_py = os.path.join(path, "rez", "plugin_managers.py")
        patch_file(
            plugin_managers_py,
            plugin_managers_py,
            {
                "                module_path = os.path.join(importer.path, name)": (
                    "                try:\n                    module_path = os.path.join(importer.path, name)\n       "
                    "         except AttributeError:\n                    continue"
                ),
            },
        )
        rez_production_install = os.path.join(path, "portable_rez", ".rez_production_install")
        write_file(rez_production_install, "")


def rename_portable_rez():
    dst_rez_pattern = os.path.join(ROOT, "build", "**", "portable_rez.exe")
    for rez_exe in glob.iglob(dst_rez_pattern, recursive=True):
        os.rename(rez_exe, rez_exe.replace("portable_rez.exe", "rez.exe"))


def main():
    build_portable_rez()
    print("Patching rez.")
    patch_rez()
    print("Rename to rez")
    rename_portable_rez()


if __name__ == "__main__":
    main()
