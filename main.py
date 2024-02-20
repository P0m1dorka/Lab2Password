import system
import passwor
import bf 

"""
 Генерация файла passwords.txt с помощью функции generate_passwords_file
 Перемещение кода SystemStub в отдельный модуль stubs
 Создание модуля bf с функцией для чтения файла построчно
 Разработка функции do_bruteforce, которая с помощью модуля bf осуществляет перебор паролей из файла к тестовой системе -> 
 При успешном подборе пароля функция должна вернуть значение пароля.
 Проверка корректности работы функции do_bruteforce

"""



passwor.generate_passwords_file()
s = system.SystemStub()
for i in range(1, 100):
    message = s.auth(i)
    print(message) 


def do_bruteforce():
    read_lines()