
#Исключения: KeyboardInterrupt
#* Перепишите функцию hello_user() из задания while1, чтобы она 
 # перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
 # и завершала работу при помощи оператора break

def hello_user():
    try:
        while True:
            b = input('Как дела?\n')
            if b == 'Хорошо':
                break
    except KeyboardInterrupt:
        print('Пока!') 
hello_user()

       
      
        
            


