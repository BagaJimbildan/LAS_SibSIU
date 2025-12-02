import platform
import re

pattern = r'^[a-zA-Z0-9]+-\d{5}-[cCnNpP]$'
matching = bool(re.match(pattern, platform.node().strip()))


pc_name = platform.node()
print(f"Имя ПК через platform.node(): '{pc_name}'")
print(f"Длина строки: {len(pc_name)}")
print(f"Коды символов: {[ord(c) for c in pc_name]}")

test_name = "hihi-66688-С"
print(f"Ручной ввод: '{test_name}'")
print(f"Длина ручного ввода: {len(test_name)}")
print(f"Коды символов: {[ord(c) for c in test_name]}")
print(f"Соответствует шаблону? {bool(re.match(pattern, test_name))}")