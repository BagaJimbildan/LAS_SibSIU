adapter_ethernet = ["адаптер ethernet", "ethernet adapter"]
ans_yes = ["yes", "да"]
ans_no = ["no", "нет"]


def find_phras(line: str, dictionary: []):
    line = line.lower()
    for phras in dictionary:
        if phras in line:
            return True
    return False