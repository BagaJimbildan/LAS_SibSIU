adapter_ethernet = ["адаптер ethernet", "ethernet adapter"]
ans_yes = ["yes", "да"]
ans_no = ["no", "нет"]
enabled = ["включен", "включена"]
enabled_no = ["выключен", "выключена"]
activate_status = ["активировано"]
activate_status_no = ["не активировано"]
matching_yes = ["соответствует стандарту имен"]
matching_no = ["не соответствует стандарту имен"]

# Если часовой пояс в программе будет меняться, то требуется перенести это поле в user_info
# Программа для СибГИУ, часовой пояс один, менять смысла нет
hour_zone = ['North Asia Standard Time', "(UTC+07:00) Красноярск"]


def find_phras(line: str, dictionary: []):
    line = line.lower()
    for phras in dictionary:
        if phras in line:
            return True
    return False