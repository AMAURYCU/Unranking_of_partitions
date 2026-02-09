"""Smoke tests for ordered_lah_partitions."""

from pathlib import Path
import sys

THIS_DIR = Path(__file__).resolve().parent
ROOT_DIR = THIS_DIR.parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import combinatorial
import lexicographic


def run():
    print("Smoke test for ordered_lah_partitions")
    try:
        print("combinatorial:", combinatorial.combinatorial_info())
    except Exception as e:
        print("combinatorial import error:", e)
    try:
        print("lexicographic:", lexicographic.lexicographic_info())
    except Exception as e:
        print("lexicographic import error:", e)


if __name__ == "__main__":
    run()

