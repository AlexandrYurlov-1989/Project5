def numbers(you_password): # Функция для проверки наличия цифр
    z = 0                  # усли z останится равно 0 то в завершении numbers будет равно 0 и непройдет проверку в функции chek
    for x in you_password: # цикл по количеству символов вашего пароля(you_password)
        if x.isdigit():    # insdigit Возвращает значение True, если проверенный символ представляет собой цифру, в противном случае значение False.
            z += 1         # и если символ строки цифра к z прибавиться 1 
    return z               # и по завершению цикла функция вернет значение z в numbers
 
def lower_case(you_password): # Функция для проверки наличия строчной буквы
    z = 0                     # усли z останится равно 0 то в завершении lower_case будет равно 0 и непройдет проверку в функции chek
    for x in you_password:    # цикл по количеству символов вашего пароля(you_password)
        if x.islower():       # islower возвращает True, если символ буква  нижнего регистра, если верхнего то будет False
            z += 1            # и если символ строки ,буква к z прибавиться 1 
    return z                  # и по завершению цикла функция вернет значение z в lower_case

def upper_case(you_password): #
    z = 0
    for x in you_password:
        if x.isupper():       # isupper возвращает True, если строка является буквой в верхнем регистре, в противном случае значение False.
            z += 1
    return z
               
def chek(you_password):
    you_password = str(you_password)
 
    if len(you_password) < 6: # Len Возвращает количество элементов в контейнере.
        return "Ваш пароль должен состоять не менее чем из 6 символов."
    if numbers(you_password) <= 0:
        return "Ваш пароль должен содержать хотя бы одну цифру."
    if lower_case(you_password) <= 0:
        return "Ваш пароль должен содержать буквы нижнего регистра."
    if upper_case(you_password) <= 0:
        return "Ваш пароль должен содержать заглавные буквы." 

    if you_password.lower() == 'password1': # Lower Возвращает копию строки, преобразованной в нижний регистр.
        return "Ваш пароль не должен содержать слово “password1” в любом регистре."
      
 
    return you_password + ' Хороший пароль'


def test():             # эта функция содержит блок паролей для проверки. Вы можете изменять пароли внутри блока для проверки либо написать вручную при старте программы
    a = chek("Sword")
    b = chek(12345678)
    c = chek("Eskaliburus")
    d = chek("123DKLSDFGS")
    e = chek("123eskaliburus")
    f = chek("PaSSworD1")  # пароль заведомо не проходил проверку из-за отсутствия цифр пришлось для примера работы функции добавить одну цифру
    g = chek("eskaliburus") 
    h = chek("KHFHJKJJ")  
    print("пример недопустимых паролей:")
    print("пароль неверный - Sword - ", a)
    print("пароль неверный - 12345678 -", b)
    print("пароль неверный - Eskaliburus -", c)
    print("пароль неверный - 123DKLSDFGS -", d)
    print("пароль неверный - 123уskaliburus -", e)
    print("пароль неверный - PaSSworD1 -", f)
    print("пароль неверный - eskaliburus -", g)
    print("пароль неверный - KHFHJKJJ -", h)

def input_password():
    a = chek(input("введите пароль: "))
    print("Вашь пароль -", a)
test()
input_password()

