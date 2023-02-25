"""
Services for file work
"""
from pathlib import Path

from schemas.file_schemas import File, Folder
from services.help_services import get_proper_bytes_name


def get_folder_info(
        path_to_folder: str
) -> Folder:
    """
    Function for getting folder info
    :param path_to_folder: Path to folder
    :return: object of Folder class
    """
    root_directory = Path(path_to_folder)
    folder = Folder(
        folder_name=root_directory.parts[-1]
    )
    for file in root_directory.glob("**/*"):
        if file.is_file():
            file_size = file.stat().st_size
            new_file = File(
                filename=file.name,
                full_path=str(file.absolute()),
                rel_path=str(file),
                file_size=file_size,
                file_size_in_megabytes=get_proper_bytes_name(file_size=file_size)
            )
            folder.full_sum += file_size
            folder.files.append(new_file)
    folder.full_sum_in_megabytes = get_proper_bytes_name(file_size=folder.full_sum)
    return folder
