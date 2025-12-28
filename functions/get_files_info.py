import os
 
def get_files_info(working_directory, directory="."):
   # Step 1 validate path of directory is inside working directory
    try: 
        working_dir_abs_path = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(os.path.join(working_dir_abs_path,directory))
        if not os.path.isdir(target_dir): 
            return f'Error: "{directory}" is not a directory'

        valid_target_dir = os.path.commonpath([working_dir_abs_path, target_dir]) == working_dir_abs_path
        if not valid_target_dir: 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        target_dir_contents = os.listdir(target_dir)
        content_data_list = []
        # get name, size, and is_dir
        for item in target_dir_contents:
            item_path = os.path.join(target_dir, item)
            if os.path.isfile(item_path): 
                content_data_list.append(f'- {item}: file_size={os.path.getsize(item_path)}, is_dir=False')
            elif os.path.isdir(item_path): 
                content_data_list.append(f'- {item}: file_size={os.path.getsize(item_path)}, is_dir=True')

        list_string = "\n".join(content_data_list)
    
        
        return list_string

    except Exception as e: 
        return f'Error: {e}'
