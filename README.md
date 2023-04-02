# Directory Renamer and File Content Replacer

This is a python script that can **rename files** and **replace text** within files in a directory and its subdirectories, based on key-value pairs that you specify in a JSON configuration file.

## Prerequisites

- Python 3.x
- A JSON config file with the following structure:

    ```json
    {
        "directory": "/path/to/directory",
        "rename_file": {
            "old_string": "new_string",
            "another_old_string": "another_new_string"
        },
        "replace_content": {
            "old_text": "new_text",
            "another_old_text": "another_new_text"
        }
    }
    ```

### Note
 - The `directory` key should specify the directory that the script will start in.
 - The `rename_file` key is a dictionary where the keys are the strings to be replaced in the filenames of all the files within the directory and subdirectories and the values are the strings to replace them with. 
 - The `replace_content` key is a dictionary where the keys are the strings to be replaced within the contents of all the files in the directory and subdirectories and the values are the strings to replace them with.


## Usage
1. Create/Edit JSON config file with the above structure and save it in the repo's root as `config.json`.

2. Run the script using the following command:
    ```bash
    python rename_replacer.py
    ```

3. The script will walk through the configured directory and its subdirectories, and **rename files** and **replace text** within files based on the key-value pairs specified in the JSON config file.

## Helpful stuff
- `json_reverser.py` has been provided to flip around your `config.json` key-value pairs in the case you need to undo a rename. It creates a new `reversed_config.json` file which you can copy the content of and place into `config.json` 

## License
This script is licensed under the MIT License. See the LICENSE file for more information.

## Contributing
Contributions to this script are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.