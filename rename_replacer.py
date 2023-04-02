import os
import json

# Load configuration from JSON file
with open('config.json') as f:
    config = json.load(f)

# Confirm that the user wants to run the script
print("WARNING: This script is potentially destructive and may irreversibly modify files in the specified directory and its subdirectories. Do you want to continue?")
print("We recommend version control be enabled prior to running")
response = input("[y/N] > ")
if response.lower() != 'y':
    print("Exiting script.")
    exit()

# Walk through directory and subdirectories
for root, dirs, files in os.walk(config['directory']):
    # Ignore hidden files and directories
    files = [f for f in files if not f.startswith('.')]
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    # Rename directories if key-value pair is found in config
    for key, value in config['rename_file'].items():
        if key in os.path.basename(root):
            new_dirname = os.path.join(os.path.dirname(root), os.path.basename(root).replace(key, value))
            os.rename(root, new_dirname)
            root = new_dirname
    
    for filename in files:
        # Rename file if key-value pair is found in config
        for key, value in config['rename_file'].items():
            if key in filename:
                new_filename = filename.replace(key, value)
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                filename = new_filename

        # Replace text within file if key-value pair is found in config
        try:
            with open(os.path.join(root, filename), encoding="utf-8-sig") as f:
                file_contents = f.read()
        except Exception as e:
            print(f"Failed to open file {os.path.join(root, filename)}: {str(e)}")
            continue
        for key, value in config['replace_content'].items():
            file_contents = file_contents.replace(key, value)
        with open(os.path.join(root, filename), 'w') as f:
            f.write(file_contents)
