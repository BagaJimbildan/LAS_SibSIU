do_not_know = "???"
not_selected = "не указан"
write_not_active = "Запись на сервер отключена"

os = do_not_know
platform = do_not_know

domain = do_not_know
activate = do_not_know # Активирована ли ОС (если windows)

dhcp = do_not_know

# Параметры сети (net - сокращение от network)
net_ip_addr = do_not_know
net_mask = do_not_know
net_gateway = do_not_know
net_dns = [do_not_know, do_not_know]


net_interface = "Ethernet"
# Нужно будет сделать выбор интерфейса в программе,
# так как для ПК с внешними сетевыми картами он отличается


# Имя ПК
name_PC = do_not_know
name_PC_standard = do_not_know
# Включена ли встроенная учетная запись администратора
admin_active = do_not_know

admin_current_user = do_not_know

default_note = "нет"

# Пути установщиков программ и драйверов
path_office2010 = ["path_office2010",not_selected]
path_office2010A = ["path_office2010A",not_selected]
path_office2016 = ["path_office2016",not_selected]
path_fineReader = ["path_fineReader",not_selected]
path_7zip = ["path_7zip",not_selected]
path_AcrobatReader = ["path_AcrobatReader",not_selected]
path_drivers = ["path_drivers",not_selected]

path_program = [path_office2010,
                path_office2010A,
                path_office2016,
                path_fineReader,
                path_7zip,
                path_AcrobatReader,
                path_drivers]
