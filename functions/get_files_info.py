import os 

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.normpath(os.path.join(working_dir_abs, directory))
        
        # Check if target_dir falls within working_directory path
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        files_list = os.listdir(target_dir)
        file_info = []

        for file_name in files_list:
            file_path = os.path.join(target_dir, file_name)
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            file_info.append(f"- {file_name}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(file_info)
    except Exception as e:
        return f"Error: {str(e)}"