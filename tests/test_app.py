import sys
import json
import os
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from rename_replacer import load_config, rename_directory, rename_file, replace_text


def test_load_config(tmp_path):
    config = {
        "directory": str(tmp_path),
        "rename_file": {
            "old": "new"
        },
        "replace_content": {
            "foo": "bar"
        }
    }
    config_path = tmp_path / "config.json"
    with open(config_path, "w") as f:
        json.dump(config, f)
    
    loaded_config = load_config(config_path)
    assert loaded_config == config

def test_rename_directory(tmp_path):
    config = {"rename_file": {"old": "new"}}
    old_dir = tmp_path / "old_dir"
    old_dir.mkdir()
    new_root = rename_directory(config, str(old_dir))
    assert os.path.basename(new_root) == "new_dir"

def test_rename_file(tmp_path):
    config = {"rename_file": {"old": "new"}}
    old_file = tmp_path / "old.txt"
    old_file.write_text("Sample text")
    new_filename = rename_file(config, str(tmp_path), "old.txt")
    assert new_filename == "new.txt"
    assert not old_file.exists()
    assert (tmp_path / "new.txt").exists()

def test_replace_text(tmp_path):
    config = {"replace_content": {"foo": "bar"}}
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a foo test")
    replace_text(config, str(tmp_path), "test.txt")
    updated_content = test_file.read_text()
    assert updated_content == "This is a bar test"
