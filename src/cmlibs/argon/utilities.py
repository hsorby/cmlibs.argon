import json
import os


def is_argon_file(filename):
    if not os.path.isfile(filename):
        return False

    try:
        with open(filename, 'r') as f:
            state = f.read()
    except UnicodeDecodeError:
        return False

    try:
        d = json.loads(state)
    except json.JSONDecodeError:
        return False

    if 'CMLibs Argon Version' not in d:
        return False

    return True
