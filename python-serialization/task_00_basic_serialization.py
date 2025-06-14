#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it as a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load JSON file and return it as a dictionary."""
    with open(filename, 'r') as f:
        return json.load(f)
