def adder(*nums):                    # функция сложения принимает любое колличество аргументов 
           
    for n in nums:               # цикл по количеству аргументов(в нашем случае количества элементов картежа os) 
        if type(n) == tuple:
            g = ()               # кортеж
            g = g + n            # заполнения картежа g с первого аргумента до последнего
            h = 0
            for i in g:          # цикл 
                h += i
            print("Sum: ", h)    # если сразу вставляю g то выводит (n, n+1, и тд) поэтому еще один цикл
        else:
            print("Sum: ", 0)

a = '0'
os = ()                              #tuple 

while a != "x":                      #цикл для ввода аргументов которые заполнят картеж os
   
    x = input('введите аргумент для сложения: ')
    try:
        x = int(x) 
        os = os + (x,)            
    except ValueError:
        print("Это не правильный ввод. Это не число! Либо вы не ввели аргументы.Ппопробуйте еще раз.")
    a = input('Нажмите Enter для продолжения ввода или Наберите \"x\" для выхода: ')

    j = os[0:] 
    adder(j)


