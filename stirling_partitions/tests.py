"""Smoke tests for stirling_partitions."""

from . import combinatorial, lexicographic


def run():
    print("Smoke test for stirling_partitions")
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
