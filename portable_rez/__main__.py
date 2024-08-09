# Import built-in modules
import re
import sys

# Import third-party modules
from rez.cli._entry_points import run_rez


if __name__ == "__main__":
    sys.argv[0] = re.sub(r"(-script\.pyw?|\.exe)?$", "", sys.argv[0])
    sys.exit(run_rez())
