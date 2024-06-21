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
# Applies DRX to specified video track in timeline.
# Uses hardcoded path, grade mode, and video track.
# right click on the media viewer, grab still, exprot .drx, make sure path is correct

import sys
sys.path.append(r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')
import DaVinciResolveScript as dvr_script

# 1. Assign Resolve
resolve = dvr_script.scriptapp("Resolve")

# Hardcoded DRX path, grade mode, and video track number
drx_path = r"C:\Users\IoT Vlogs\Documents\DRSAutomationbyIoTVlogs\2 Color Grading\Sepia DRX Still 2024-06-06 132950_1.2.1.drx" 
grade_mode = 0  # Replace with the desired grade mode
video_track = 2  # Replace with the desired video track number (1 for V1, 2 for V2, etc.)

# 2. Define function to apply DRX to specified track in all timelines
def apply_drx_to_specified_track(resolve, path, track, grade_mode=0):
    # 1. Get the project manager
    project_manager = resolve.GetProjectManager()
    
    # 2. Get the current project
    project = project_manager.GetCurrentProject()
    if not project:
        print("No project is currently open.")
        return False
    
    # Get the count of timelines
    timeline_count = project.GetTimelineCount()
    if timeline_count == 0:
        print("No timelines found in the current project.")
        return False

    # Loop through each timeline
    for index in range(timeline_count):
        timeline = project.GetTimelineByIndex(index + 1)
        project.SetCurrentTimeline(timeline)
        
        # Apply the DRX to the specified track in the timeline
        if not apply_drx_to_specified_track_clips(timeline, path, track, grade_mode):
            print(f"Failed to apply DRX to track {track} in timeline: {timeline.GetName()}")
            return False
    
    return True

# 3. Define function to apply DRX to clips in specified track of a timeline
def apply_drx_to_specified_track_clips(timeline, path, track, grade_mode=0):
    # Get the count of video tracks in this timeline
    track_count = timeline.GetTrackCount("video")
    if track_count == 0:
        print("No video tracks found in the current timeline.")
        return False

    # Ensure the specified track is within the range of available tracks
    if track < 1 or track > track_count:
        print(f"Invalid track number: {track}. This timeline has {track_count} video track(s).")
        return False

    # Get the clips from the specified video track
    clips = timeline.GetItemListInTrack("video", track)
    
    # Apply grade from DRX to clips in the specified track
    if not timeline.ApplyGradeFromDRX(path, int(grade_mode), clips):
        print(f"Failed to apply DRX to clips in track {track}.")
        return False
    
    return True

# 4. Call the function to apply the grade to the specified track in all timelines
if not apply_drx_to_specified_track(resolve, drx_path, video_track, grade_mode):
    print("Unable to apply a grade from DRX file to the specified track in all timelines.")
else:
    print(f"Successfully applied DRX to video track {video_track} in all timelines.")

