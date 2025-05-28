#!/usr/bin/env python3
"""
Test script to specifically verify that import_export/admin.py passes black formatting.
"""

import subprocess
import sys
import os

def test_black_formatting():
    """Test that admin.py passes black formatting."""
    try:
        os.chdir('/lca-workspace/repos/django-import-export__django-import-export')
        
        # Run black on just the admin.py file
        result = subprocess.run(
            ['python', '-m', 'black', '--check', '--diff', 'import_export/admin.py'],
            capture_output=True,
            text=True
        )
        
        print("Black check output:")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error running black: {e}")
        return False

def test_isort_formatting():
    """Test that admin.py passes isort formatting."""
    try:
        os.chdir('/lca-workspace/repos/django-import-export__django-import-export')
        
        # Run isort on just the admin.py file
        result = subprocess.run(
            ['python', '-m', 'isort', '--check-only', '--diff', 'import_export/admin.py'],
            capture_output=True,
            text=True
        )
        
        print("Isort check output:")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error running isort: {e}")
        return False

def test_flake8_formatting():
    """Test that admin.py passes flake8 formatting."""
    try:
        os.chdir('/lca-workspace/repos/django-import-export__django-import-export')
        
        # Run flake8 on just the admin.py file
        result = subprocess.run(
            ['python', '-m', 'flake8', 'import_export/admin.py'],
            capture_output=True,
            text=True
        )
        
        print("Flake8 check output:")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error running flake8: {e}")
        return False

def main():
    print("Testing admin.py formatting with individual tools...")
    
    # Test black
    print("\n1. Testing black formatting...")
    black_passed = test_black_formatting()
    
    # Test isort
    print("\n2. Testing isort formatting...")
    isort_passed = test_isort_formatting()
    
    # Test flake8
    print("\n3. Testing flake8 formatting...")
    flake8_passed = test_flake8_formatting()
    
    # Summary
    print("\n=== SUMMARY ===")
    print(f"Black passed: {black_passed}")
    print(f"Isort passed: {isort_passed}")
    print(f"Flake8 passed: {flake8_passed}")
    
    if black_passed and isort_passed and flake8_passed:
        print("✅ SUCCESS: All formatting checks passed!")
        return 0
    else:
        print("❌ FAILURE: Some formatting checks failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())