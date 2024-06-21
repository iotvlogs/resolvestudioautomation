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
import time
import pyautogui

# Delay before executing each action (in seconds)
ACTION_DELAY = 0.1

#####################################################

# place the playhead and press i to set the in point
# place the playhead and press o to set the out point
# run the script to delete media inbetween in and out points
# press alt+x to cancel in and out point

#####################################################
# Switch to Resolve Software
time.sleep(ACTION_DELAY)
pyautogui.hotkey('win', '3')

# Simulate pressing Ctrl + B to set the out point
pyautogui.hotkey('ctrl', 'b')
time.sleep(ACTION_DELAY)

# Simulate pressing Ctrl + B to set the in point
pyautogui.hotkey('ctrl', 'b')
time.sleep(ACTION_DELAY)

# Simulate selecting the portion to delete
pyautogui.hotkey('shift', 'right')  # Select right of the timeline
time.sleep(ACTION_DELAY)

# Simulate deleting the selected portion
pyautogui.press('delete')
time.sleep(ACTION_DELAY)

# Move playhead to the start of the trimmed part (previous edit point)
pyautogui.hotkey('up')  # Usually 'up' or 'page up' moves to the previous edit point
time.sleep(ACTION_DELAY)
