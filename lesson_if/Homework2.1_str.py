first_str1 = "The first line"
second_str2 = "The second line"

def two_str(first_str1, second_str2):
    if  type(first_str1) == str and type(second_str2) == str:
        return 0
    elif first_str1 == second_str2:
        return 1
    elif first_str1 != second_str2 and len(first_str1)>len(second_str2): 
        return 2   
    elif first_str1 != second_str2 and second_str2 == "learn":
        return 3
    else:
        return 25

print(two_str(first_str1, second_str2))                
   
