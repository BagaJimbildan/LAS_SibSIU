from datetime import datetime
import os
import subprocess

from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QMainWindow

import methods.start_info as start_inf
import static_info as stat_inf
import methods.program_setup as prog_set
import file_master as file_m
import app_info as app_inf
import user_info as user_inf
import key_phrases as k_phras
import server_setting as serv_set
import methods.server_logs as serv_log
import methods.other as other

import methods.create_standart as create_standard
from design_ui.ui_CreatePass_script import DialogCreatePass
from design_ui.ui_DataServer_script import DialogDataServer
from design_ui.ui_DisableUser_script import DialogDisableUser
from design_ui.ui_DomainName_script import DialogDomainName
from design_ui.ui_EditNetwork_script import DialogEditNetwork
from design_ui.ui_EditPath_script import DialogEditPath
from design_ui.ui_EditPing_script import DialogEditPing
from design_ui.ui_Error_script import DialogError
from design_ui.ui_LoopFunction_script import DialogLoopFunction
from design_ui.ui_ParamNet_script import DialogParamNet
from design_ui.ui_Programs_script import DialogPrograms
from design_ui.ui_StandardName_script import DialogStandardName
from design_ui.ui_Success_script import DialogSuccess
from design_ui.ui_YesNo_script import DialogYesNo
from design_ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    buttons_admin: list[QPushButton]  # кнопки, которые доступны только админу


    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons_admin = \
        [
            self.ui.btn_enable_admin,
            self.ui.btn_pass_admin,
            self.ui.btn_edit_name,
            self.ui.btn_edit_network,
            self.ui.btn_disable_user,
            self.ui.btn_domain,
            self.ui.btn_programs,
            self.ui.btn_drivers,
            self.ui.btn_activate_windows,
            self.ui.btn_activate_office,
            self.ui.btn_loop
        ]

        self.buttons_no_linux = \
            [
                self.ui.btn_enable_admin,
                self.ui.btn_pass_admin,
                self.ui.btn_disable_user,
                self.ui.btn_domain,
                self.ui.btn_programs,
                self.ui.btn_drivers,
                self.ui.add_path,
                self.ui.disconnect,
                self.ui.info_server,
                self.ui.btn_activate_windows,
                self.ui.btn_activate_office,
                self.ui.btn_loop
            ]

        self.ui.lbl_os.setText(stat_inf.platform)
        self.ui.lbl_domen.setText(stat_inf.domain)
        self.ui.lbl_os_activate.setText(stat_inf.activate)
        self.ui.lbl_dhcp.setText(stat_inf.dhcp)
        self.ui.lbl_admin_active.setText(stat_inf.admin_active)
        self.ui.lbl_name.setText(stat_inf.name_PC)
        self.ui.lbl_name_is_standart.setText(stat_inf.name_PC_standard)

        self.ui.btn_net_1.clicked.connect(self.parameters_net)
        self.ui.btn_enable_admin.clicked.connect(self.enable_admin_param)
        self.ui.btn_pass_admin.clicked.connect(self.open_window_password)
        self.ui.btn_edit_name.clicked.connect(self.dialog_edit_name_show)
        self.ui.btn_edit_network.clicked.connect(self.dialog_edit_network_show)
        self.ui.btn_disable_user.clicked.connect(self.disable_user)
        self.ui.btn_domain.clicked.connect(self.enter_domain)
        self.ui.btn_programs.clicked.connect(self.programs)

        self.ui.btn_loop.clicked.connect(self.loop_function_show)

        self.ui.btn_drivers.clicked.connect(self.setup_driver_pack)

        self.ui.btn_activate_windows.clicked.connect(self.activate_windows)
        self.ui.btn_activate_office.clicked.connect(self.activate_office)

        self.ui.btn_ping_global.clicked.connect(self.update_network_status_global)
        self.ui.btn_ping_local.clicked.connect(self.update_network_status_local)

        self.ui.add_path.triggered.connect(self.addPath_window)
        self.ui.info_server.triggered.connect(self.status_connect_server_show)
        self.ui.disconnect.triggered.connect(self.connect_disconnect)
        self.ui.test_write.triggered.connect(self.send_test_write_server)
        self.ui.open_logs_server.triggered.connect(self.open_server_file_logs)
        self.ui.test_global.triggered.connect(lambda: self.change_host_ping(False))
        self.ui.test_local.triggered.connect(lambda: self.change_host_ping(True))

        if stat_inf.admin_current_user == 0:
            self.unenable_buttons_admin()
            self.ui.lbl_status_user.setText("Программа запущена НЕ от администратора")
        elif stat_inf.admin_current_user == 1:
            self.ui.lbl_status_user.setText("Программа запущена от администратора")

        if stat_inf.os.lower() == "linux":
            self.unenable_buttons_linux()

        if stat_inf.activate == k_phras.activate_status[0]:
            self.ui.btn_activate_windows.setEnabled(False)

        # Отключение кнопки "Включить учетную запись админа"
        if stat_inf.admin_active == k_phras.enabled[1] and self.ui.btn_enable_admin.isEnabled():
            self.ui.btn_enable_admin.setEnabled(False)

        # Записываем логи на сервер только если ОС windows
        if stat_inf.os.lower() == "windows":
            self.write_server_asking()

        if not app_inf.write_server:
            self.ui.disconnect.setText("Подключиться")

        # Проверка соединения
        self.update_network_status_global(True)
        self.update_network_status_local(True)



    def change_host_ping(self, local: bool):
        if local: param = [self.ui.lbl_local_net_name, self.ui.lbl_local_net_time, self.ui.lbl_local_net_status]
        else: param = [self.ui.lbl_global_net_name, self.ui.lbl_global_net_time, self.ui.lbl_global_net_status]

        self.dialog_edit_ping = DialogEditPing(local, param[0], param[1], param[2])

        name_net = "локальной" if local else "глобальной"
        self.dialog_edit_ping.setWindowTitle("Изменение " + name_net+ " сети")
        self.dialog_edit_ping.ui.lbl_name_net.setText(name_net + " сети:")

        self.dialog_edit_ping.show()

    def update_network_status(self, name_label, time_label, status_label, address):
        name_label.setText(address)
        if address == stat_inf.not_selected:
            time_label.setText(stat_inf.default_note)
            status_label.setText(stat_inf.default_note)
        else:
            status = other.ping(address)
            time_label.setText(datetime.now().strftime("%H:%M:%S"))
            status_label.setText(stat_inf.success if status else stat_inf.fail)

    def update_network_status_global(self, start = False):
        if not start:
            if user_inf.ping_global[1] == stat_inf.not_selected:
                self.dialog_error_show("Глобальный адрес не указан")
                return
        self.update_network_status(self.ui.lbl_global_net_name,
                                   self.ui.lbl_global_net_time,
                                   self.ui.lbl_global_net_status,
                                   user_inf.ping_global[1])

    def update_network_status_local(self, start = False):
        if not start:
            if user_inf.ping_local[1] == stat_inf.not_selected:
                self.dialog_error_show("Локальный адрес не указан")
                return
        self.update_network_status(self.ui.lbl_local_net_name,
                                   self.ui.lbl_local_net_time,
                                   self.ui.lbl_local_net_status,
                                   user_inf.ping_local[1])


    def activate_windows(self):
        create_standard.activate_windows(self.dialog_error_server_show)
        start_inf.check_activate()

        self.ui.lbl_os_activate.setText(stat_inf.activate)

        if stat_inf.activate == k_phras.activate_status[0]:
            self.ui.btn_activate_windows.setEnabled(False)

    def activate_office(self):
        create_standard.activate_office(self.dialog_error_server_show)

    def loop_function_show(self):
        self.dialog_loop = DialogLoopFunction(self.enable_admin_param,
                                              self.open_window_password,
                                              self.disable_user,
                                              self.activate_windows,
                                              self.activate_office,
                                              self.dialog_edit_name_show,
                                              self.enter_domain,
                                              self.dialog_edit_network_show)
        self.dialog_loop.show()


    def send_test_write_server(self):
        if not app_inf.write_server:
            self.dialog_error_show(stat_inf.write_not_active)
        else:
            status = serv_log.test_open_excel()
            if status[0] == 1:
                self.dialog_error_show("Проверка записи на сервер завершена с ошибкой:" + "\n"+ str(status[1]))
            else:
                self.dialog_success_show("Проверка записи на сервер завершена успешно")

    def open_server_file_logs(self):
        if not app_inf.write_server:
            self.dialog_error_show(stat_inf.write_not_active)
        else:
            try:
                os.startfile(serv_log.path_log)
            except Exception as e:
                self.dialog_error_show(str(e))

    def connect_disconnect(self):
        if not app_inf.write_server:
            self.dialogDataServer = DialogDataServer(self.dialog_error_show, self.dialog_success_show, self.dialog_error_server_show, self.ui.disconnect)

            fields = ['ticket', 'subdivision', 'owner', 'room', 'current_room']

            for field in fields:
                value = getattr(user_inf, field)
                if value != stat_inf.do_not_know:
                    widget = getattr(self.dialogDataServer.ui, f'tb_{field}')
                    widget.setText(value)

            self.dialogDataServer.ui.btn_cancel.setText("Отмена")


            self.dialogDataServer.show()
        else:
            self.disconnect_server()

    def status_connect_server_show(self):
        if not app_inf.write_server:
            self.dialog_error_show(stat_inf.write_not_active)
        else:
            self.dialogDataServer = DialogDataServer(self.dialog_error_show, self.dialog_success_show, self.dialog_error_server_show)
            self.dialogDataServer.setWindowTitle("Информация о соединении")



            self.dialogDataServer.ui.tb_server.setReadOnly(True)
            self.dialogDataServer.ui.tb_file_server.setReadOnly(True)
            self.dialogDataServer.ui.tb_username.setReadOnly(True)
            self.dialogDataServer.ui.tb_pass.setEnabled(False)
            self.dialogDataServer.ui.label_8.setEnabled(False)

            self.dialogDataServer.ui.tb_ticket.setReadOnly(True)
            self.dialogDataServer.ui.tb_subdivision.setReadOnly(True)
            self.dialogDataServer.ui.tb_owner.setReadOnly(True)
            self.dialogDataServer.ui.tb_room.setReadOnly(True)
            self.dialogDataServer.ui.tb_current_room.setReadOnly(True)

            self.dialogDataServer.ui.tb_ticket.setText(user_inf.ticket)
            self.dialogDataServer.ui.tb_subdivision.setText(user_inf.subdivision)
            self.dialogDataServer.ui.tb_owner.setText(user_inf.owner)
            self.dialogDataServer.ui.tb_room.setText(user_inf.room)
            self.dialogDataServer.ui.tb_current_room.setText(user_inf.current_room)


            self.dialogDataServer.ui.btn_ok.clicked.disconnect()
            self.dialogDataServer.ui.btn_cancel.clicked.disconnect()

            self.dialogDataServer.ui.btn_ok.clicked.connect(self.dialogDataServer.close)
            self.dialogDataServer.ui.btn_cancel.clicked.connect(self.disconnect_server)
            self.dialogDataServer.ui.btn_cancel.clicked.connect(self.dialogDataServer.close)
            self.dialogDataServer.ui.btn_cancel.setText("Отключиться")

            self.dialogDataServer.show()

    def disconnect_server(self, force = False):
        serv_set.disconnect_server()
        app_inf.write_server = False
        self.ui.disconnect.setText("Подключиться")
        if not force:
            self.dialog_success_show("Запись на сервер отключена")


    def setup_driver_pack(self):
        prog_set.setup_program(self, "Драйвер пак", stat_inf.path_drivers)

    def addPath_window(self):
        self.dialog_path_window = DialogEditPath()
        self.dialog_path_window.show()


    def select_write_server_yes(self):
        self.dialogWriteServer.close()
        self.dialogDataServer = DialogDataServer(self.dialog_error_show, self.dialog_success_show, self.dialog_error_server_show)

        self.dialogDataServer.exec()

    def write_server_asking(self):
        self.dialogWriteServer = DialogYesNo()
        self.dialogWriteServer.setWindowTitle("Фиксировать изменения")
        self.dialogWriteServer.ui.tb_text.setText("Записывать изменения на сервере?")
        self.dialogWriteServer.ui.btn_ok.setText("Да")
        self.dialogWriteServer.ui.btn_close.setText("Нет")
        self.dialogWriteServer.ui.btn_ok.clicked.connect(self.select_write_server_yes)
        self.dialogWriteServer.exec()

    def programs(self):
        self.dialogPrograms = DialogPrograms(self)
        self.dialogPrograms.show()

    def enter_domain(self):
        self.dialogDomainName = DialogDomainName(self.dialog_error_show, self.dialog_success_show, self.ui.lbl_domen, self.dialog_error_server_show)
        self.dialogDomainName.exec()

    def disable_user(self):
        self.dialogDisableUser = DialogDisableUser(self.dialog_error_show, self.dialog_success_show, self.dialog_error_server_show)
        self.dialogDisableUser.exec()

    def parameters_net(self):
        self.dialogParamNet = DialogParamNet()
        self.dialogParamNet.show()

    def enable_admin_param(self):
        status = create_standard.enable_admin(self.ui.lbl_admin_active, self.ui.btn_enable_admin, self.dialog_error_server_show)

        if status[0] == 1:
            self.dialog_error_show(status[1])
        else:
            self.dialog_success_show("Учетная запись администратора успешно включена")


    # Отключение кнопок которые не могут быть выполнены не админом
    def unenable_buttons_admin(self):
        for i in self.buttons_admin:
            i.setEnabled(False)

    # Отключение кнопок которые не нужно выполнять на Linux
    # исходя из задач отдела
    def unenable_buttons_linux(self):
        for i in self.buttons_no_linux:
            i.setEnabled(False)

    def open_window_password(self):
        self.dialogPassAdmin = DialogCreatePass()
        self.dialogPassAdmin.ui.btn_ok.clicked.connect(self.start_change_pass)
        self.dialogPassAdmin.setWindowTitle("Задать пароль администратора")
        self.dialogPassAdmin.ui.lb_info.setText("Введите и подтвердите пароль встроенной учетной записи администратора")
        self.dialogPassAdmin.exec()

    def start_change_pass(self):
        pass1 = self.dialogPassAdmin.ui.tb_pass1.text()
        pass2 = self.dialogPassAdmin.ui.tb_pass2.text()

        if pass1 == pass2:
            status = create_standard.pass_admin(pass1, self.dialog_error_server_show)
            if status[0] == 1:
                self.dialog_error_show(status[1])
            else:
                self.dialog_success_show("Пароль администратора успешно изменен")
                self.dialogPassAdmin.close()

        else:
            self.dialog_error_show("Введеные пароли не совпадают")

    def dialog_error_show(self, text: str):
        self.dialogError = DialogError()
        self.dialogError.ui.tb_error.setText(text)
        self.dialogError.exec()

    def dialog_error_server_show(self, text):
        self.dialogError = DialogError()
        self.dialogError.setWindowTitle("Предупреждение")
        self.dialogError.ui.tb_error.setText("Ошибка записи информации на сервер" + "\n"+
                                             "Соединение с сервером разорвано" + "\n" + str(text))
        self.disconnect_server(True)
        self.dialogError.exec()

    def dialog_success_show(self, text: str):
        self.dialogSuccess = DialogSuccess()
        self.dialogSuccess.ui.tb_info.setText(text)
        self.dialogSuccess.exec()

    def dialog_edit_name_show(self):
        self.dialogEditName = DialogStandardName(self.ui.lbl_name, self.ui.lbl_name_is_standart, self.dialog_success_show, self.dialog_error_show, self.dialog_error_server_show)
        self.dialogEditName.exec()

    def dialog_edit_network_show(self):
        self.dialogEditNetwork = DialogEditNetwork(self.ui.lbl_dhcp, self.dialog_error_show, self.dialog_success_show, self.dialog_error_server_show)
        self.dialogEditNetwork.exec()