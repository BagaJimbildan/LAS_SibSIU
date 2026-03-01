import static_info as stat_inf

username = ["user", ""]  # логин того, кто работает с программой
ip_server = ["server", ""]  # сервер, где хранится файл-отчет с записанными действиями
file_server = ["file_server", ""]

ping_global = ["ping_global", stat_inf.not_selected]
ping_local = ["ping_local", stat_inf.not_selected]

ticket = stat_inf.do_not_know  # номер заявки по которой работает
owner = stat_inf.do_not_know  #  владелец ПК по которому работают
subdivision = stat_inf.do_not_know  # подразделение где ПК числится
room = stat_inf.do_not_know  # кабинет где будет находится ПК
current_room = stat_inf.do_not_know  # текущий кабинет, где находится ПК