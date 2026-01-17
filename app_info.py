import static_info as stat_inf
import file_master as file_m

is_first = stat_inf.do_not_know  # первый ли запуск данного экземпляра программы
write_server = stat_inf.do_not_know  # записываем ли на сервер
asking_write = True  # по умолчанию выводим экран о том, записывать ли на сервер

def start_info_app():  # чтение информации и смена параметров
    print("hell")