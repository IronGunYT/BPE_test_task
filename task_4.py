import json
import datetime


def replace_fields(d):
    """
    Modify dictionary that represents JSON file
    """
    for key, value in d.items():
        if key == 'updated':
            d[key] = datetime.datetime.now().isoformat()
        elif isinstance(value, dict):
            replace_fields(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    replace_fields(item)


def correct_json(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)
    replace_fields(data)
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    correct_json('file_4.json')
    print('JSON file was corrected')
