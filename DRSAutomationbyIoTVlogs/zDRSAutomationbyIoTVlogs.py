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
import os
import subprocess
import webbrowser
import sys
import datetime
import time
import shutil
import tkinter as tk
from tkinter import ttk
sys.path.append(r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules')
import DaVinciResolveScript as dvr_script

# OBS recording naming convention MUST -SR-%b-%DD-%CCYY-%I-%mm-%ss-%p
# Settings --> Advanced --> Filename Formatting 

# C:\Users\IoT Vlogs\Desktop\DR Media Backup 
#####################################################################

# Specify the parent directory containing the subfolders with .py files
parent_directory = "C:\\Users\\IoT Vlogs\\Documents\\DRSAutomationbyIoTVlogs"
# Define the template and its path. 
templateRoot = r'C:\Users\IoT Vlogs\Documents\DRSAutomationbyIoTVlogs'
templateFile = os.path.join(templateRoot, 'Empty Timeline V2 A2.drp')

#####################################################################
show_cmd_window = False
project_name_entry = None

def get_scripts_by_folder(directory):
    # Get all subdirectories in the specified directory
    subfolders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
    scripts_by_folder = {}
    for folder in subfolders:
        folder_path = os.path.join(directory, folder)
        # Get all .py files in the subdirectory
        scripts = [f for f in os.listdir(folder_path) if f.endswith('.py')]
        scripts_by_folder[folder] = scripts
    return scripts_by_folder

def execute_script(script_path):
    # Execute the selected Python script in a new command window
    if show_cmd_window:
        subprocess.Popen(["start", "cmd", "/k", "python", script_path], shell=True)
    else:
        subprocess.Popen(["python", script_path], shell=True)

def toggle_cmd_window():
    global show_cmd_window
    show_cmd_window = cmd_window_var.get()

def generate_project():
    # Function to generate project based on the input in the text box
    global media_path, templateRoot, templateFile
    
    # Open Resolve software
    resolve_exe_path = r'C:\Program Files\Blackmagic Design\DaVinci Resolve\Resolve.exe'
    subprocess.Popen([resolve_exe_path])
    time.sleep(30)
    
    media_path = project_name_entry.get()
    media_path = r"{}".format(media_path)
    print('Media Location:', media_path)
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%I_%M_%S%p_%B_%d_%Y")

    # Get a list of all files in the directory
    files = os.listdir(media_path)

    # Filter files based on the naming convention
    matching_files = [file for file in files if "-SR-" in file]

    # Extract the project ID name from the matching file
    if matching_files:  # Check if there are matching files
        project_id_name = matching_files[0].split("-SR-")[0]
        print("The project ID name:", project_id_name)
        # Set project name
        projectName = project_id_name + "_" + timestamp + "_OUTPUT"
        print("The project name:", projectName)
    else:
        print("No file with the specified naming convention found.")

    # Determine default project directory based on operating system
    if os.name == 'posix':  # Unix-like system
        default_project_dir = os.path.expanduser("~/Movies/DaVinci Resolve/Projects")
    elif os.name == 'nt':  # Windows
        default_project_dir = os.path.join(os.getenv('USERPROFILE'), 'Documents', 'DaVinci Resolve', 'Projects')
    else:
        print("Unsupported operating system")
        return

    # Create the default project directory if it doesn't exist
    if not os.path.exists(default_project_dir):
        os.makedirs(default_project_dir)

    # Destination directory for the copied project template
    projectFile = os.path.join(default_project_dir, projectName + '.drp')

    # Make a copy of the project template with the new project filename 
    shutil.copy2(templateFile, projectFile)

    # Load project
    resolve = dvr_script.scriptapp("Resolve") 
    projectManager = resolve.GetProjectManager()

    # Import the project that we just created. 
    projectManager.ImportProject(projectFile)

    # Load the project we just created. 
    project = projectManager.LoadProject(projectName)

    if not project:
        print("Unable to load project")
        sys.exit()
    
    timeline = project.GetCurrentTimeline()
    project_name = project.GetName()
    timeline.SetName(project_name)
    
    # Get mediaPool and mediaStorage Objects 
    mediaPool = project.GetMediaPool() 
    mediaStorage = resolve.GetMediaStorage()
    mp = media_path
    clips = mediaStorage.AddItemListToMediaPool(mp)
    # Append Clips to the timeline
    appended = mediaPool.AppendToTimeline(clips)    
    
def on_entry_click(event):
    # Function to paste clipboard content when entry is clicked
    try:
        clipboard_text = root.clipboard_get()
        event.widget.delete(0, tk.END)
        event.widget.insert(0, clipboard_text)
    except tk.TclError:
        pass

def open_url(event):
    webbrowser.open_new("https://www.youtube.com/@iotvlogs/playlists")

def render_gui(root, directory):
    global project_name_entry  # Declare project_name_entry as global
    
    scripts_by_folder = get_scripts_by_folder(directory)

    # Define font styles
    label_font = ("Segoe UI", 14)
    entry_font = ("Segoe UI", 14)
    button_font = ("Segoe UI", 14)
    checkbox_font = ("Segoe UI", 14)
    tab_font = ("Segoe UI", 14)
    footer_font = ("Segoe UI", 10)
    link_font = ("Segoe UI", 10, "underline")

    # Define colors
    bg_color = "#2b2b2b"
    fg_color = "#f0f0f0"
    btn_color = "#4CAF50"
    btn_fg_color = "#ffffff"
    tab_bg_color = "#3c3c3c"
    tab_active_bg_color = "#4CAF50"
    link_color = "#4CAF50"

    # Set the root window background color
    root.configure(bg=bg_color)

    # Checkbox for showing command prompt window
    global cmd_window_var
    cmd_window_var = tk.BooleanVar(value=show_cmd_window)
    checkbox = tk.Checkbutton(root, text="Show Command Prompt Window", variable=cmd_window_var, command=toggle_cmd_window, font=checkbox_font, bg=bg_color, fg=fg_color, selectcolor=bg_color)
    checkbox.pack(anchor='w', padx=10, pady=5)

    # Tabs for each folder containing scripts
    tab_control = ttk.Notebook(root)
    style = ttk.Style()
    style.theme_use('default')
    style.configure('TNotebook', background=bg_color, borderwidth=0)
    style.configure('TNotebook.Tab', font=tab_font, background=tab_bg_color, foreground=fg_color, padding=[10, 5])
    style.configure('TFrame', background=bg_color)
    style.map('TNotebook.Tab', background=[('selected', tab_active_bg_color)], foreground=[('selected', '#ffffff')])
    
    # Add Import tab at the beginning
    import_tab = ttk.Frame(tab_control)
    tab_control.add(import_tab, text="Import")
    
    # Text box for project name
    project_name_label = tk.Label(import_tab, text="Media Location:", font=label_font, bg=bg_color, fg=fg_color)
    project_name_label.pack(anchor='w', padx=10, pady=5)
    #project_name_entry = tk.Entry(import_tab, font=entry_font)
    project_name_entry = tk.Entry(import_tab, font=entry_font, bg="#353535", fg="#f0f0f0")

    project_name_entry.pack(fill='x', padx=10, pady=5)  # Make the text box span the width
    project_name_entry.bind("<FocusIn>", on_entry_click)
    
    # Assign project_name_entry to the global variable
    project_name_entry = project_name_entry
    
    # Button to generate project
    generate_project_button = tk.Button(import_tab, text="Generate Project", command=generate_project, font=button_font, bg=btn_color, fg=btn_fg_color, activebackground=btn_color, activeforeground=btn_fg_color)
    generate_project_button.pack(anchor='w', padx=10, pady=10)
    
    for folder, scripts in scripts_by_folder.items():
        tab = ttk.Frame(tab_control)
        tab_control.add(tab, text=folder)
        
        for script in scripts:
            script_path = os.path.join(directory, folder, script)
            button = tk.Button(tab, text=script, command=lambda sp=script_path: execute_script(sp), font=button_font, bg=btn_color, fg=btn_fg_color, activebackground=btn_color, activeforeground=btn_fg_color)
            button.pack(anchor='w', padx=10, pady=5)
    
    tab_control.pack(expand=1, fill='both', padx=10, pady=10)

# Footer
    footer_frame = tk.Frame(root, bg=bg_color)
    footer_frame.pack(fill='x', padx=10, pady=10)

    footer_text = tk.Label(footer_frame, text="Visit the IoT Vlogs for more: ", font=footer_font, bg=bg_color, fg=fg_color)
    footer_text.grid(row=0, column=0, sticky='e')

    link_label = tk.Label(footer_frame, text="https://www.youtube.com/@iotvlogs/playlists", font=link_font, bg=bg_color, fg=link_color, cursor="hand2")
    link_label.grid(row=0, column=1, sticky='w')
    link_label.bind("<Button-1>", open_url)

    copyright_label = tk.Label(footer_frame, text="© 2024 IoT Vlogs. All rights reserved.", font=footer_font, bg=bg_color, fg=fg_color)
    copyright_label.grid(row=1, column=0, columnspan=2)

    # Center the footer content
    footer_frame.grid_columnconfigure(0, weight=1)
    footer_frame.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('DRS Automation Framework by IoT Vlogs')
    root.geometry('800x600')
    root.attributes('-topmost', True)  # Ensure the window is always on top
    render_gui(root, parent_directory)
    root.mainloop()




