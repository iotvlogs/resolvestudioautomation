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
import pyautogui

# Append the required module path
sys.path.append(r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')
import DaVinciResolveScript as dvr


##########################################################

# Hardcoded output folder path
output_folder = r"C:\Users\IoT Vlogs\Desktop\OUTPUT"

###########################################################

# Connect to DaVinci Resolve
resolve = dvr.scriptapp("Resolve")
if resolve:
    print("Successfully connected to DaVinci Resolve")
else:
    print("Failed to connect to DaVinci Resolve")
    sys.exit()

# Assuming the DaVinci Resolve is pinned third in the taskbar
pyautogui.hotkey('win', '3')
resolve.OpenPage('deliver')

# Get the project manager
projectManager = resolve.GetProjectManager()
# Get the current project
project = projectManager.GetCurrentProject()
if not project:
    print("No project is currently open")
    sys.exit()

# Get the current timeline
currentTimeline = project.GetCurrentTimeline()
if not currentTimeline:
    # Try to get the first timeline and set it to current
    if project.GetTimelineCount() > 0:
        currentTimeline = project.GetTimelineByIndex(1)
        project.SetCurrentTimeline(currentTimeline)
    else:
        print("No timelines available")
        sys.exit()

render_job = {
    'TargetDir': output_folder
}

# Set the render settings
project.SetRenderSettings(render_job)
project.SetPreset('H.264 Master')
pid = project.AddRenderJob()
project.StartRendering(pid)


print("JobId data type", type(pid))
print("JobId>>>>>>>", str(pid))

status = project.GetRenderJobStatus(pid)
print("status >>>>>", status)
render_task = project.GetRenderJobList()
print("Render task >>>>>>>", render_task)

