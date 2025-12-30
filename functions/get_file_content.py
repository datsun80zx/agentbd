import os

from google import genai
from google.genai import types
from config import MAX_CHARS, validate, Path_type

def get_file_content(working_directory, file_path): 
    working_abs_path = os.path.abspath(working_directory)
    try: 
        """
        target_file = os.path.normpath(os.path.join(working_abs_path, file_path))
        if not os.path.isfile(target_file): 
            return f'Error: File not found or is not a regular file: "{file_path}"'

        valid_target_file = os.path.commonpath([working_abs_path, target_file]) == working_abs_path
        if not valid_target_file: 
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
        """
        target_file = validate(working_abs_path, file_path, Path_type.FILE)
        with open(target_file, "r") as f: 
            file_content_string = f.read(MAX_CHARS)
            if f.read(1): 
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e: 
        return f'Error: {e}'


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the content of a specified file in a specified directory relative to the working directory, providing either the entire contents of that file or the contents of the file up to a preset character limit.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file in which to read the contents of. May be the absolute path, relative path, or simply the name of the file in which the path is assumed to be the current working directory."
            )
        },
        required=["file_path"]
    ),
    
)