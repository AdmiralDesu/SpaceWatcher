"""
Schemas for file work
"""
from pydantic import BaseModel


class File(BaseModel):
    """
    Schema for file
    """
    filename: str
    full_path: str
    rel_path: str
    file_size: int
    file_size_in_megabytes: str


class Folder(BaseModel):
    """
    Schema for folder
    """
    folder_name: str
    full_sum: int = 0
    full_sum_in_megabytes: str = ""
    files: list[File] = []
