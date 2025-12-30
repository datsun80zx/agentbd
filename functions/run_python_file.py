import os
import subprocess

from google import genai
from google.genai import types
from config import validate, Path_type

def run_python_file(working_directory, file_path, args=None):
    working_abs_path = os.path.abspath(working_directory)
    try: 
        directory, file_name = os.path.split(file_path)
        if not os.path.isfile(os.path.normpath(os.path.join(working_abs_path, file_name))):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_name.endswith('.py'): 
            return f'Error: "{file_path}" is not a Python file'

        result = validate(working_abs_path, file_path, Path_type.FILE)
        
        command = ["python", result]
        if args: 
            command.extend(args)

        process_object = subprocess.run(
            command,
            capture_output=True,
            cwd=os.path.dirname(result),
            text=True,
            timeout=30
        )

        if process_object.returncode != 0:
            return f'Process exited with code {process_object.returncode}'
        elif process_object.stdout == '' and process_object.stderr == '': 
            return f'No output produced'
        else: 
            return f'STDOUT: {process_object.stdout}\nSTDERR: {process_object.stderr}'
    except Exception as e: 
        return f'Error: executing Python file: {e}'


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the python code found in the file provided by the 'file_path' parameter. May or may not need/have additional arguments to pass into the python script.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of the file to execute the desired Python script. May be the absolute path, relative path, or simply the name of the file in which the path is assumed to be the current working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Possible additional arguments to be passed to the Python script"
                ),
            ),
        },
        required=["file_path"]
    ),
   
)
        
        