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

# Append the required module path
sys.path.append(r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')


########################################################################
# LUT file path
lut_path = r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT\MySepia 65 Point Cube.cube" 
# Apply the LUT to all clips in the specified video track (e.g., 1 for V1, 2 for V2)
track_number = 2
########################################################################
# eg. Sepia Sat 25; Offset R 40, G 20, B 2; Film Looks Rec709 Kodak 2383 D65
# Right click on the clip --> Generate LUT --> 65 Point Cube 

try:
    import DaVinciResolveScript as dvr
except ImportError:
    print("Could not import DaVinciResolveScript module")
    sys.exit()

# Connect to DaVinci Resolve
resolve = dvr.scriptapp("Resolve")
if not resolve:
    print("Failed to connect to DaVinci Resolve")
    sys.exit()

# Access the current project
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()

if not project:
    print("No project opened")
    sys.exit()

# Switch to the Color page
resolve.OpenPage("color")

# Function to apply LUT to all clips in a specific track
def apply_lut_to_track(lut_path, track_number):
    # Get the current timeline
    timeline = project.GetCurrentTimeline()
    if not timeline:
        print("No timeline found")
        return False

    # Get all clips in the specified video track
    clips = timeline.GetItemListInTrack("video", track_number)
    if not clips or len(clips) == 0:
        print(f"No clips found in video track V{track_number}")
        return False

    # Apply LUT to each clip in the track
    nodeIndex = 1
    for clip in clips:
        if not clip:
            print(f"Failed to get clip in track V{track_number}")
            continue

        success = clip.SetLUT(nodeIndex, lut_path)
        if success:
            print(f"LUT applied successfully to clip in track V{track_number}")
        else:
            print(f"Failed to apply LUT to clip in track V{track_number}")
    
    return True
if not apply_lut_to_track(lut_path, track_number):
    sys.exit()
