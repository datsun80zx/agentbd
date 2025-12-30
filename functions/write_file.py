import os

from google import genai
from google.genai import types
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


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided content to a specified file. If file doesn't exist then will create the file and then write the content to that file. If there is already content in that file then it will simply overwrite the existing content with the newly provided content.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to write to. May be the absolute path, relative path, or simply the name of the file in which the path is assumed to be the current working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the desired content for the file specified."
            ),
        },
        required=["file_path"]
    ),
   
)