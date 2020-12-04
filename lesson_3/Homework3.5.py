with open ('referat.txt', 'r', encoding='utf8') as f1,open('referat2.txt', 'w', encoding='utf8') as f2:    
    #f1.read().replace('.','!')
    line = f1.read().replace('.','!')
    print(line)
    f2.write(line)
    


   
   
#Замените точки в тексте на восклицательные знаки. Результат сохраните в файл referat2.txt






#with open ('referat2.txt', 'w', encoding='utf8') as f2:
    #f2.write()

# -*- coding: utf-8 -*-
# Открываем файл только для чтения
#old_image = open('temp/pro.jpeg', 'r').read()
 
# Создаем новый файл
#new_image = open('new_pro.jpeg', 'w')
 
# Сохраняем данные старой картинки в новую
#new_image.write(old_image)
#new_image.close()


