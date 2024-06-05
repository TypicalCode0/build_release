while True:
    cmd = input("Выберите команду:\nexit - выход из программы\nprint - вывести введённое вами слово\n-> ")
    if cmd == "exit":
        break
    if cmd == "print":
        s = input("Введите слово -> ")
        print(f'Введенное слово: {s}')
