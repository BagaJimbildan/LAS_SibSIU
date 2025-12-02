adapter_ethernet = ["адаптер ethernet", "ethernet adapter"]
ans_yes = ["yes", "да"]
ans_no = ["no", "нет"]
enabled = ["включен", "включена"]
enabled_no = ["выключен", "выключена"]
activate_status = ["активировано"]
activate_status_no = ["не активировано"]
matching_yes = ["соответствует стандарту имен"]
matching_no = ["не соответствует стандарту имен"]

# надо днс сюда и маску


def find_phras(line: str, dictionary: []):
    line = line.lower()
    for phras in dictionary:
        if phras in line:
            return True
    return False