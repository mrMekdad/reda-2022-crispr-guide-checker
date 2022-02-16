import argparse
from crispr_guide_checker.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Reference management and rule-based checks for guide candidate review.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
