#!/usr/bin/env python3
"""
Test script to reproduce the pre-commit formatting issue.
This script runs pre-commit and checks if it passes without making changes.
"""

import subprocess
import sys
import os

def run_precommit():
    """Run pre-commit and return the result."""
    try:
        # Change to the repository directory
        os.chdir('/lca-workspace/repos/django-import-export__django-import-export')
        
        # Run pre-commit on all files
        result = subprocess.run(
            ['pre-commit', 'run', '--all-files'],
            capture_output=True,
            text=True
        )
        
        print("Pre-commit output:")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error running pre-commit: {e}")
        return False

def check_git_status():
    """Check if there are any uncommitted changes."""
    try:
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            cwd='/lca-workspace/repos/django-import-export__django-import-export'
        )
        
        if result.stdout.strip():
            print("Git status shows uncommitted changes:")
            print(result.stdout)
            return False
        else:
            print("No uncommitted changes detected.")
            return True
            
    except Exception as e:
        print(f"Error checking git status: {e}")
        return False

def main():
    print("Testing pre-commit formatting issue...")
    
    # First check git status
    print("\n1. Checking initial git status...")
    initial_clean = check_git_status()
    
    # Run pre-commit
    print("\n2. Running pre-commit...")
    precommit_passed = run_precommit()
    
    # Check git status after pre-commit
    print("\n3. Checking git status after pre-commit...")
    final_clean = check_git_status()
    
    # Summary
    print("\n=== SUMMARY ===")
    print(f"Initial git status clean: {initial_clean}")
    print(f"Pre-commit passed: {precommit_passed}")
    print(f"Final git status clean: {final_clean}")
    
    if precommit_passed and final_clean:
        print("✅ SUCCESS: Pre-commit passed without making changes!")
        return 0
    else:
        print("❌ FAILURE: Pre-commit failed or made changes!")
        return 1

if __name__ == "__main__":
    sys.exit(main())