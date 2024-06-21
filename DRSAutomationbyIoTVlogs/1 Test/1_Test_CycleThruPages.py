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

import sys
import time

# Append the required module path
sys.path.append(r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')
import DaVinciResolveScript as dvr

# Connect to DaVinci Resolve
resolve = dvr.scriptapp("Resolve")
if resolve:
    print("Successfully connected to DaVinci Resolve")
else:
    print("Failed to connect to DaVinci Resolve")
    sys.exit()

# Function to switch pages
def switch_page(page_name):
    try:
        resolve.OpenPage(page_name)
        print(f"Switched to {page_name} page")
        time.sleep(1)  # Adding a short delay for visibility
    except Exception as e:
        print(f"Failed to switch to {page_name} page: {e}")

# List of pages to navigate through
pages = ["media", "cut", "edit", "fusion", "color", "fairlight", "deliver"]

# Loop to switch between pages 3 times
for i in range(2):
    for page in pages:
        switch_page(page)

print("Completed switching pages")
