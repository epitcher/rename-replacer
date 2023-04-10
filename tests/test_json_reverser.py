import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from json_reverser import switch_key_pairs

def test_switch_key_pairs():
    input_data = {
        "config": {
            "replace_file": {
                "file1": "file2",
                "file3": "file4"
            },
            "replace_content": {
                "content1": "content2",
                "content3": "content4"
            }
        }
    }

    expected_output = {
        "config": {
            "replace_file": {
                "file2": "file1",
                "file4": "file3"
            },
            "replace_content": {
                "content2": "content1",
                "content4": "content3"
            }
        }
    }

    fields_to_switch = ['replace_file', 'replace_content']
    modified_data = switch_key_pairs(input_data, fields_to_switch)
    assert modified_data == expected_output
