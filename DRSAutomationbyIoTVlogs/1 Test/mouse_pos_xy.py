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
import pyautogui
import time

# you have to find mouse coordinates based on your screen resolution
# preset (111, 345)
# add to render queue (836, 1904)
# render all (3639, 987)

def print_coordinates():
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        # Print the coordinates
        print(f"Mouse coordinates: ({x}, {y})")
        # Pause execution for 1 second
        time.sleep(1)

try:
    print("Press Ctrl-C to stop printing coordinates.")
    # Call the print_coordinates function
    print_coordinates()
except KeyboardInterrupt:
    print("\nProgram stopped.")
