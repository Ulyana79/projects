def hello_user():
    while True:
        str1= input('Как дела?\n')
        if str1 == 'Хорошо':
            break
hello_user()
#Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  #пользователя “Как дела?”, пока он не ответит “Хорошо”