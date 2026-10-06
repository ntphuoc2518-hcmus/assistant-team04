"""Environment validation script for Smart Virtual Assistant project.

Verifies:
1. Python version >= 3.10
2. Project structure and essential directories
3. Essential configuration and data files
4. Required dependencies (e.g. pytest)
"""

import importlib.util
import sys
from pathlib import Path

REQUIRED_PYTHON_MAJOR = 3
REQUIRED_PYTHON_MINOR = 10

REQUIRED_DIRS = [
    "src",
    "src/assistant",
    "tests",
    "data",
    "docs",
    "ui",
]

REQUIRED_FILES = [
    "pyproject.toml",
    "requirements.txt",
    "README.md",
    "src/assistant/rules.py",
    "tests/test_smoke.py",
]

REQUIRED_PACKAGES = [
    "pytest",
]


def check_python_version() -> bool:
    current = sys.version_info
    print(f"Checking Python version: {current.major}.{current.minor}.{current.micro}...", end=" ")
    if (current.major, current.minor) >= (REQUIRED_PYTHON_MAJOR, REQUIRED_PYTHON_MINOR):
        print("[PASS]")
        return True
    print(f"[FAIL] (Requires Python >= {REQUIRED_PYTHON_MAJOR}.{REQUIRED_PYTHON_MINOR})")
    return False


def check_directories(root: Path) -> bool:
    all_ok = True
    print("\nChecking project directories:")
    for directory in REQUIRED_DIRS:
        dir_path = root / directory
        if dir_path.is_dir():
            print(f"  [PASS] {directory}/")
        else:
            print(f"  [FAIL] {directory}/ (missing)")
            all_ok = False
    return all_ok


def check_files(root: Path) -> bool:
    all_ok = True
    print("\nChecking essential project files:")
    for filename in REQUIRED_FILES:
        file_path = root / filename
        if file_path.is_file():
            print(f"  [PASS] {filename}")
        else:
            print(f"  [FAIL] {filename} (missing)")
            all_ok = False
    return all_ok


def check_dependencies() -> bool:
    all_ok = True
    print("\nChecking required Python dependencies:")
    for package in REQUIRED_PACKAGES:
        spec = importlib.util.find_spec(package)
        if spec is not None:
            print(f"  [PASS] {package}")
        else:
            print(f"  [WARN/FAIL] {package} is not installed in the current environment")
            all_ok = False
    return all_ok


def main() -> int:
    root_dir = Path(__file__).resolve().parent.parent
    print("=" * 60)
    print("  Smart Virtual Assistant - Environment Verification")
    print("=" * 60)

    py_ok = check_python_version()
    dirs_ok = check_directories(root_dir)
    files_ok = check_files(root_dir)
    deps_ok = check_dependencies()

    print("\n" + "=" * 60)
    if py_ok and dirs_ok and files_ok and deps_ok:
        print("  All environment checks passed successfully! [OK]")
        print("=" * 60)
        return 0
    elif py_ok and dirs_ok and files_ok:
        print("  Core project files are OK. Note: install missing dependencies via:")
        print("  pip install -r requirements.txt")
        print("=" * 60)
        return 0
    else:
        print("  Some environment checks failed. Please review errors above.")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
