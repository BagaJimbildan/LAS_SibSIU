import sys
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet

app = QApplication(sys.argv)
apply_stylesheet(app, 'dark_teal.xml')
qss = app.styleSheet()

with open('dark_teal.qss', 'w', encoding='utf-8') as f:
    f.write(qss)

print('Файл dark_teal.qss успешно сохранён')
app.quit()