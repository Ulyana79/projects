#Цикл while: ask_user со словарём
#* Создайте словарь типа "вопрос": "ответ", например:
  #{"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
#* Напишите функцию ask_user() которая с помощью функции input()
#  просит пользователя ввести вопрос, а затем, если вопрос есть
#  в словаре, программа давала ему соотвествующий ответ. Например:
#    Пользователь: Что делаешь?
#    Программа: Программирую#

questions_and_answers = {'Как дела?': 'Отлично!', 'Что делаешь?':'Программирую.', 'Получается?':'Пока не очень.'}
#print(questions_and_answers)
def ask_user(questions_and_answers):
  while True:
    str1 = input('Введите свой вопрос: ')
    if str1 == 'Как дела?':
      print(questions_and_answers['Как дела?'])
    elif str1 == 'Что делаешь?':
      print(questions_and_answers['Что делаешь?'])
    elif str1 == 'Получается?': 
      print(questions_and_answers['Получается?']) 
    else:
      print(str1)
ask_user(questions_and_answers)

    
    











 