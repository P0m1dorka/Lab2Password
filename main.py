from stubs import SystemStub
import password
import bf

"""
 Генерация Д passwords.txt с помощью функции generate_passwords_file
 Перемещение кода SystemStub в отдельный модуль stubs
 Создание модуля bf с функцией для чтения Д построчно
 Разработка функции do_bruteforce, которая с помощью модуля bf осуществляет перебор паролей из Д к тестовой системе -> 
 При успешном подборе пароля функция должна вернуть значение пароля.
 Проверка корректности работы функции do_bruteforce

"""
password.generate_passwords_file()
##reader_generator= bf.read_file('passwords.txt')


s = SystemStub()
for i in range(1, 100):
    try_pass=bf.brute("passwords.txt")
    message = s.auth(try_pass)
    if(message=="SUCCESS"):
        print("SUCCESS")
        print(try_pass)
    elif(message=="!!! SUCCESS !!!"):
        break
    else:
        print(message)