"""
Services for help
"""


def get_proper_bytes_name(
        file_size: int
) -> str:
    """
    Function for proper file name in bytes
    :param file_size: Размер файла в байтах
    :return:
    """
    if file_size == 0:
        return f"{file_size} B"
    if file_size >= 1024:
        if file_size >= 1048576:
            return f"{round(file_size / 1048576)} MB"  # 2 ** 20
        return f"{round(file_size / 1024)} KB"  # 2 * 10
    return f"{file_size} B"
