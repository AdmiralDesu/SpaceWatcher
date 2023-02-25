"""
Тестовый модуль для расчета размеров файла в папке
"""
from pprint import pprint

from services.file_services import get_folder_info
from ui.main_window import get_app


# folder = get_folder_info("./folder")
#
# pprint(folder.dict())

app = get_app()

app.mainloop()

