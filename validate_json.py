import json
import os
import jsonschema
from jsonschema import validate

def load_schema(schema_file):
    """Load the JSON schema from file."""
    with open(schema_file, 'r') as f:
        return json.load(f)

def validate_json_file(json_file, schema):
    """Validate a single JSON file against the schema."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    try:
        validate(instance=data, schema=schema)
        return True, None
    except jsonschema.exceptions.ValidationError as e:
        return False, str(e)

def main():
    schema_file = 'screen_schema.json'
    json_dir = 'json'
    
    # Load schema
    schema = load_schema(schema_file)
    
    # Validate each JSON file
    valid_files = 0
    invalid_files = 0
    
    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            json_file = os.path.join(json_dir, filename)
            is_valid, error = validate_json_file(json_file, schema)
            
            if is_valid:
                print(f"✅ {filename} is valid.")
                valid_files += 1
            else:
                print(f"❌ {filename} is invalid:")
                print(f"   Error: {error}")
                invalid_files += 1
    
    # Print summary
    print("\nValidation Summary:")
    print(f"Total files: {valid_files + invalid_files}")
    print(f"Valid files: {valid_files}")
    print(f"Invalid files: {invalid_files}")

if __name__ == "__main__":
    main() 