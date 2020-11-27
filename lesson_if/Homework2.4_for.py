all_school = [{'school_clacc':'1а', 'scores': [5, 4, 4, 5, 5]}, 
              {'school_clacc':'2а', 'scores': [4, 4, 3, 5, 5]},
              {'school_clacc':'3б', 'scores': [5, 5, 4, 5, 5]},
              {'school_clacc':'4а', 'scores': [5, 3, 4, 5, 2]}
              ]
l1a = (len(all_school[0] ['scores']))
l2a = (len(all_school[1] ['scores']))
l3b = (len(all_school[2] ['scores']))
l4a = (len(all_school[3] ['scores']))

a = sum(all_school[0] ['scores'])
b = sum(all_school[1] ['scores'])
c = sum(all_school[2] ['scores']) 
d = sum(all_school[3] ['scores'])
#print (a)
print (f'Средний балл 1а класса:{a/l1a}')
print (f'Средний балл 2а класса:{b/l2a}')
print (f'Средний балл 3б класса:{c/l3b}')
print (f'Средний балл 4а класса:{d/l4a}')

all_class = [a, b, c, d]
classes_sum = 0
for score in all_class:
    classes_sum += score
#print(classes_sum)




all_len = sum([l1a, l2a, l3b, l4a])
#print(all_len)
print (f'Средний балл по всей школе: {classes_sum/all_len}')

