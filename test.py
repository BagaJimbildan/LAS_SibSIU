import threading
import time

def delayed_action():
    print("Прошло 10 секунд, выполняю действие")

print("Начало программы")
# Запускаем таймер: через 10 секунд вызовется delayed_action
timer = threading.Timer(10.0, delayed_action)
timer.start()

# Основной поток продолжает работу
for i in range(20):
    print(f"Основной поток работает... {i}")
    time.sleep(1)  # имитация полезной работы

# Если нужно дождаться выполнения таймера перед завершением программы,
# можно вызвать timer.join() (но это заблокирует основной поток до конца таймера)
# timer.join()
print("Программа завершена")