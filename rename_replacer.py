import os
import json

# Load configuration from JSON file
with open('config.json') as f:
    config = json.load(f)

# Walk through directory and subdirectories
for root, dirs, files in os.walk(config['directory']):
    # Ignore hidden files and directories
    files = [f for f in files if not f.startswith('.')]
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    for filename in files:
        # Rename file if key-value pair is found in config
        for key, value in config['rename_file'].items():
            if key in filename:
                new_filename = filename.replace(key, value)
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
                filename = new_filename

        # Replace text within file if key-value pair is found in config
        with open(os.path.join(root, filename)) as f:
            file_contents = f.read()
        for key, value in config['replace_content'].items():
            file_contents = file_contents.replace(key, value)
        with open(os.path.join(root, filename), 'w') as f:
            f.write(file_contents)
