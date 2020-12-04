def discounted(price, discount, max_discount=20):
    try: 
        price = abs(float(price)) 
    except TypeError:
        print('Неверный тип данных в price')
        return - 1
    except ValueError:
        print('Неверное значение в price')
        return - 1     
    try:       
        discount = abs(float(discount))
    except TypeError: 
        print('Неверный тип данных  в discount')
        return - 1
    except ValueError:
        print('Неверное значение в discoun')
        return - 1      
    try:     
        max_discount = abs(int(max_discount))
    except TypeError:   
        print('Неверный тип данных  в max_discount')
        return - 1
    except ValueError:
        print('Неверное значение в max_discoun')
        return - 1  
    if max_discount > 99:
        print('Слишком большая максимальная скидка')
    elif discount >= max_discount:
        return price
    else:
        return(price - (price * discount / 100))         
    


print(discounted(100, 2))
print(discounted(100, "3"))
print(discounted("100", "4.5"))
print(discounted("five", 5))
print(discounted("сто", "десять"))
print(discounted(100.0, 5, "10"))   
#discounted(120,10)



    #Перепишите функцию discounted(price, discount, max_discount=20)
  #из урока про функции так, чтобы она перехватывала исключения,
  #когда переданы некорректные аргументы.
 #Первые два нужно приводить к вещественному числу при помощи float(),
  #а третий - к целому при помощи int() и перехватывать исключения
  #ValueError и TypeError, если приведение типов не сработало.
    

    
