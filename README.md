# Increment and Save Shelf Script for Houdini
This tool increments and saves the currently open file. If there is no increment, a 3 digit counter beginning with 001 will be appended to the exisiting file name.
**Examples:**
- file_v1.hip -> file_v2.hip
- file.hip -> file.001.hip
- file.009.hip -> file.010.hip
- filename001_sometext.hip -> filename002_sometext.hip

## Installation
Right click the Houdini shelf you would like the tool in and choose *New Tool*. Name the tool whatever you'd like under the Options tab. I have included a save icon to use - you can upload this image under *Icon*. Paste the contents of the script in the *Script* tag. Make sure the Script Language is set to Python. If you would like, you can set a hotkey for the tool under the *Hotkeys* tab. Then, *Accept* the tool. You can always edit the tool later.
