x = [1, 2, 3, 'lol']

dict_age = {
	'katya':[43, 'ivanova', 'moskow', {'job':'manager', 'habbit':'coffee'}],
	'sonya':{'age':43, 'town':'moskow'}
}



list_name  = ['katya', 'sonya']
list_age = [43, 43]

print(dict_age['katya'])
print(dict_age['katya'][0], dict_age['katya'][2])

print(dict_age['sonya']['town'])

print(list(dict_age.keys()))

print(dict_age['katya'][3]['habbit'])


list_y = [1, 2, 3, ['4', 5, 6], dict_age]

print(list_y[4]['katya'][3]['habbit'])


print(x[0], x[0])
print(x[1], x[1])
print(x[3], x[3])
print(x[2], x[2])

print("----------------------------------------")

for elem in x:
	for elem_inner in list_y:
		print('elem = ', elem, '; elem_inner = ', elem_inner)
		#if type(elem) == int:
	#		print(elem, elem)
		#elif type(elem) == str:
	#		print(elem, elem, elem)
#		else:
			#print('????')
