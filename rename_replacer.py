import os
import json


def load_config(file_path):
    with open(file_path) as f:
        return json.load(f)


def get_confirmation():
    print("WARNING: This script is potentially destructive and may irreversibly modify files in the specified directory and its subdirectories. Do you want to continue?")
    print("We recommend version control be enabled prior to running")
    response = input("[y/N] > ")
    return response.lower() == 'y'


def process_directory(config):
    for root, dirs, files in os.walk(config['directory']):
        files = [f for f in files if not f.startswith('.')]
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        root = rename_directory(config, root)

        for filename in files:
            filename = rename_file(config, root, filename)
            replace_text(config, root, filename)


def rename_directory(config, root):
    for key, value in config['rename_file'].items():
        if key in os.path.basename(root):
            new_dirname = os.path.join(os.path.dirname(root), os.path.basename(root).replace(key, value))
            os.rename(root, new_dirname)
            return new_dirname
    return root


def rename_file(config, root, filename):
    for key, value in config['rename_file'].items():
        if key in filename:
            new_filename = filename.replace(key, value)
            os.rename(os.path.join(root, filename), os.path.join(root, new_filename))
            return new_filename
    return filename


def replace_text(config, root, filename):
    try:
        with open(os.path.join(root, filename), encoding="utf-8-sig") as f:
            file_contents = f.read()
    except Exception as e:
        print(f"Failed to open file {os.path.join(root, filename)}: {str(e)}")
        return
    for key, value in config['replace_content'].items():
        file_contents = file_contents.replace(key, value)
    with open(os.path.join(root, filename), 'w') as f:
        f.write(file_contents)


if __name__ == "__main__":
    config = load_config('config.json')
    if get_confirmation():
        process_directory(config)
    else:
        print("Exiting script.")
        exit()
