from unittest import case

from PySide6.QtWidgets import QDialog

from design_ui.ui_ChangeDesign import Ui_DialogChangeDesign
import create_design.name_themes as name_themes
import file_master as file_m
import user_info as user_inf


class DialogChangeDesign(QDialog):
    def __init__(self, change_design_method):
        super().__init__()
        self.ui = Ui_DialogChangeDesign()
        self.ui.setupUi(self)

        self.change_design_method = change_design_method

        self.ui.btn_cancel.clicked.connect(self.close)
        self.ui.btn_ok.clicked.connect(self.change_design)

        if user_inf.design_theme[1] == name_themes.th_light: self.ui.rb_white.setChecked(True)
        else: self.ui.rb_dark.setChecked(True)

        self.rb_name = [[name_themes.c_teal, self.ui.rb_teal],
                        [name_themes.c_amber, self.ui.rb_amber],
                        [name_themes.c_blue, self.ui.rb_blue],
                        [name_themes.c_cyan, self.ui.rb_cyan],
                        [name_themes.c_lightgreen, self.ui.rb_lightgreen],
                        [name_themes.c_pink, self.ui.rb_pink],
                        [name_themes.c_purple, self.ui.rb_purple],
                        [name_themes.c_red, self.ui.rb_red],
                        [name_themes.c_yellow, self.ui.rb_yellow]]

        for i in self.rb_name:
            if user_inf.design_color[1] == i[0]:
                i[1].setChecked(True)
                break

    def change_design(self):
        theme = name_themes.th_light if self.ui.rb_white.isChecked() else name_themes.th_dark
        for i in self.rb_name:
            if i[1].isChecked():
                self.change_design_method(theme, i[0])

                user_inf.design_theme[1] = theme
                user_inf.design_color[1] = i[0]

                file_m.write_info_app(user_inf.design_theme[0], user_inf.design_theme[1])
                file_m.write_info_app(user_inf.design_color[0], user_inf.design_color[1])
                break
