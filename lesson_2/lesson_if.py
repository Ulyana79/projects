


age=int(input("Введите Ваш возраст"))
def type_of_activity(age):
    if  age <= 6:
        return "Вы ходите в детский сад"
    elif 7 <= age <= 17:
        return "Вы учитесь в школе" 
    elif 18 <= age <= 22:
        return "Вы учитесь в университете"  
    else:

        return "Вы работаете"   

print(type_of_activity(age))             
