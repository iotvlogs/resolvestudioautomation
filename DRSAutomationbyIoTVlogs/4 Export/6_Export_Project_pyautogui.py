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
import datetime
import pyautogui

# Append the required module path
sys.path.append(r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')
import DaVinciResolveScript as dvr

##########################################################

# Hardcoded output folder path
output_folder = r"C:\Users\IoT Vlogs\Desktop\OUTPUT"

##########################################################


# Connect to DaVinci Resolve
resolve = dvr.scriptapp("Resolve")
if resolve:
    print("Successfully connected to DaVinci Resolve")
else:
    print("Failed to connect to DaVinci Resolve")
    sys.exit()
    
# assuming the DaVinchi Resolve is pinned third in the taskbar
pyautogui.hotkey('win', '3')
resolve.OpenPage('deliver')

# Get the project manager
projectManager = resolve.GetProjectManager()
# Get the current project
project = projectManager.GetCurrentProject()
if not project:
    print("No project is currently open")
    sys.exit()

# Try to get the current timeline
currentTimeline = project.GetCurrentTimeline()
if not currentTimeline:
    # Try to get the first timeline and set it to current
    if project.GetTimelineCount() > 0:
        currentTimeline = project.GetTimelineByIndex(1)
        project.SetCurrentTimeline(currentTimeline)
    else:
        print("No timelines available")
        sys.exit()

# Get the project name
output_name = project.GetName()

def click_at_coordinates(x, y):
    time.sleep(1)
    pyautogui.click(x, y, button='left')

def type_text(text):
    time.sleep(1)
    pyautogui.typewrite(text, interval=0.1)


#slider
click_at_coordinates(5, 499)

# preset
click_at_coordinates(111, 345)


# click on file name
#click_at_coordinates(542, 564)
# press ctrl+a
#pyautogui.hotkey('ctrl', 'a')
# type the value of variable output_name
#type_text(output_name)

#click on export location
click_at_coordinates(411, 645)
# press ctrl+a
pyautogui.hotkey('ctrl', 'a')
# type the value of variable output_folder
type_text(output_folder)

##########################################


# add to render queue
click_at_coordinates(836, 1904)
# render all
click_at_coordinates(3645, 913)
time.sleep(1)

#### OR 

"""
pid = project.AddRenderJob()
project.StartRendering(pid)
time.sleep(1)

pid = None
render_task = project.GetRenderJobList()
pid = render_task[0]['JobId']
print("JobId data type", type(pid))
print("JobId>>>>>>>", str(pid))

status = project.GetRenderJobStatus(str(pid))
print("status >>>>>", status)

print("Render task >>>>>>>", render_task)
"""
