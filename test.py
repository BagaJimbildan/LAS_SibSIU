from pathlib import Path

file_path = Path("C:/Users/Baga/Downloads/rufus-4.12p.xls")


if file_path.exists():
    print("Путь существует")

if file_path.is_file():
    print("Это файл")

extension = file_path.suffix.lower()
if extension in ('.xls', '.xlsx', '.xlsm', '.xlsb'):
    print("Это файл Excel")