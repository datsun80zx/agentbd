import os

from config import validate, Path_type

def write_file(working_directory, file_path, content): 
    working_abs_path = os.path.abspath(working_directory)
    try: 
        if os.path.isdir(os.path.normpath(os.path.join(working_abs_path, file_path))):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        directory, file_name = os.path.split(file_path)
        result = validate(working_abs_path, directory, Path_type.DIR)
        
        os.makedirs(result, exist_ok=True)
        validated_file_path = os.path.normpath(os.path.join(result, file_name))

        with open(validated_file_path, "w") as f: 
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e: 
        return f'Error: {e}'
