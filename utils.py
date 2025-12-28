import json
from pathlib import Path
from jsonschema import validate, ValidationError

def save_json(filepath: Path, data: dict | list, indent=2):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

def load_json(filepath: Path) -> dict | list:
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_json(data: dict, schema: dict = None):
    # Basic validation (bonus feature)
    if schema is None:
        return True
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError:
        return False
