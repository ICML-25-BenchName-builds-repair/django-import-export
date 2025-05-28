#!/usr/bin/env python3
"""
Script to reproduce the flake8 issue with unused import.
This script runs flake8 specifically on the problematic file to verify the issue.
"""

import subprocess
import sys
import os

def run_flake8_on_file():
    """Run flake8 on the specific file that has the issue."""
    file_path = "tests/core/tests/test_resources/test_resources.py"
    
    print(f"Running flake8 on {file_path}...")
    
    try:
        result = subprocess.run(
            ["flake8", file_path],
            capture_output=True,
            text=True,
            cwd="/lca-workspace/repos/django-import-export__django-import-export"
        )
        
        print(f"Exit code: {result.returncode}")
        if result.stdout:
            print(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            print(f"STDERR:\n{result.stderr}")
            
        return result.returncode == 0
        
    except FileNotFoundError:
        print("flake8 not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "flake8"])
        return run_flake8_on_file()

def run_pre_commit():
    """Run pre-commit to reproduce the full CI issue."""
    print("\nRunning pre-commit --all-files...")
    
    try:
        result = subprocess.run(
            ["pre-commit", "run", "--all-files"],
            capture_output=True,
            text=True,
            cwd="/lca-workspace/repos/django-import-export__django-import-export"
        )
        
        print(f"Exit code: {result.returncode}")
        if result.stdout:
            print(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            print(f"STDERR:\n{result.stderr}")
            
        return result.returncode == 0
        
    except FileNotFoundError:
        print("pre-commit not found. Please install it first.")
        return False

if __name__ == "__main__":
    print("=== Reproducing the flake8 unused import issue ===")
    
    # Change to the repository directory
    os.chdir("/lca-workspace/repos/django-import-export__django-import-export")
    
    # Test 1: Run flake8 on the specific file
    flake8_passed = run_flake8_on_file()
    
    # Test 2: Run full pre-commit
    precommit_passed = run_pre_commit()
    
    print("\n=== Summary ===")
    print(f"Flake8 on specific file passed: {flake8_passed}")
    print(f"Pre-commit passed: {precommit_passed}")
    
    if not flake8_passed or not precommit_passed:
        print("Issue reproduced successfully!")
        sys.exit(1)
    else:
        print("No issues found.")
        sys.exit(0)