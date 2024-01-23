import system
import passwor
passwor.generate_passwords_file()
s = system.SystemStub()
for i in range(1, 100):
    message = s.auth(i)
    print(message)