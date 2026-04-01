#!/usr/bin/env python3
"""
Verification script to test the reorganized project structure.
Run this to ensure all paths are correctly configured.
"""
import os
import sys

def check_file(path, description):
    """Check if a file exists and report status."""
    exists = os.path.exists(path)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {path}")
    return exists

def check_directory(path, description):
    """Check if a directory exists and report status."""
    exists = os.path.isdir(path)
    status = "✓" if exists else "✗"
    print(f"{status} {description}: {path}")
    return exists

def main():
    print("=" * 60)
    print("Kafka 101 Project Structure Verification")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check directories
    print("Checking directories...")
    all_good &= check_directory("config", "Config directory")
    all_good &= check_directory("docs", "Documentation directory")
    all_good &= check_directory("src", "Source code directory")
    all_good &= check_directory("templates", "Templates directory")
    print()
    
    # Check essential files
    print("Checking essential files...")
    all_good &= check_file("README.md", "Main README")
    all_good &= check_file("STRUCTURE.md", "Structure documentation")
    all_good &= check_file("requirements.txt", "Python dependencies")
    all_good &= check_file("LICENSE", "License file")
    all_good &= check_file(".gitignore", "Git ignore file")
    print()
    
    # Check config files
    print("Checking configuration files...")
    all_good &= check_file("config/config.ini.example", "Config template")
    has_config = check_file("config/config.ini", "Actual config (optional)")
    if not has_config:
        print("  ℹ️  Note: You need to create config/config.ini from the example")
    print()
    
    # Check source files
    print("Checking source code files...")
    all_good &= check_file("src/__init__.py", "Python package init")
    all_good &= check_file("src/app.py", "Flask web application")
    all_good &= check_file("src/consumer.py", "Kafka consumer")
    all_good &= check_file("src/producer.py", "Kafka producer")
    print()
    
    # Check templates
    print("Checking templates...")
    all_good &= check_file("templates/index.html", "Web interface template")
    print()
    
    # Check documentation
    print("Checking documentation...")
    all_good &= check_file("docs/README.md", "Documentation index")
    print()
    
    # Test path resolution
    print("Testing path resolution from src/...")
    script_dir = os.path.dirname(os.path.abspath("src/app.py"))
    config_path = os.path.join(script_dir, "config", "config.ini")
    template_dir = os.path.join(script_dir, "templates")
    
    print(f"  Working directory: {os.getcwd()}")
    print(f"  Config path would be: {config_path}")
    print(f"  Template dir would be: {template_dir}")
    print()
    
    # Summary
    print("=" * 60)
    if all_good:
        print("✓ All essential files and directories are in place!")
        print()
        print("Next steps:")
        print("1. Copy config/config.ini.example to config/config.ini")
        print("2. Edit config/config.ini with your Confluent Cloud credentials")
        print("3. Run: python src/consumer.py config/config.ini")
        print("4. Run: python src/app.py")
    else:
        print("✗ Some files or directories are missing!")
        print("Please check the structure and try again.")
        sys.exit(1)
    print("=" * 60)

if __name__ == "__main__":
    main()

# Made with Bob
