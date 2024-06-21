"""
Copyright (c) 2024 Iot Vlogs.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# C:\Users\IoT Vlogs\Documents\DRSAutomationbyIoTVlogs\zDRSAutomationbyIoTVlogs.py
import os
import subprocess
import sys
import shutil

# Import PyInstaller dynamically
try:
    import PyInstaller
except ImportError:
    print("PyInstaller not found. Attempting to install...")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    import PyInstaller

def create_exe():
    # Prompt the user to enter the path of the .py file
    py_file_path = input("Enter the path of the .py file: ").strip()

    # Ensure the provided file path exists
    if not os.path.isfile(py_file_path):
        print("Error: Provided file path does not exist.")
        return

    # Get the directory containing the .py file
    file_dir = os.path.dirname(py_file_path)

    # Set boolean flag for keeping the build directory
    keep_build = input("Keep build directory after build? (yes/no): ").strip().lower() == 'yes'

    # Run PyInstaller to create the .exe file
    command = [
        "pyinstaller",
        "--onefile",
        "--noconsole",
        "--distpath", file_dir,  # Set dist path to the same directory as the .py file
        py_file_path
    ]
    try:
        subprocess.run(command, check=True)
        print("Executable created successfully.")
    except subprocess.CalledProcessError as e:
        print("Error creating executable:", e)
        return

    # Hide command prompt window when running the executable
    exe_name = os.path.splitext(os.path.basename(py_file_path))[0] + ".exe"
    exe_path = os.path.join(file_dir, exe_name)
    
    # Remove the build directory if the flag is set to False
    build_dir = os.path.join(file_dir, "build")
    if not keep_build and os.path.exists(build_dir):
        shutil.rmtree(build_dir)
        print("Build directory deleted.")

    # Remove the .spec file
    spec_file_path = os.path.join(file_dir, os.path.splitext(os.path.basename(py_file_path))[0] + ".spec")
    if os.path.exists(spec_file_path):
        os.remove(spec_file_path)
        print(".spec file deleted.")

    # Check if the .exe file exists in the specified directory
    if os.path.exists(exe_path):
        print(f"Running executable: {exe_path}")
        subprocess.Popen(exe_path, creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        print(f"Error: Executable not found at {exe_path}")

if __name__ == "__main__":
    create_exe()
