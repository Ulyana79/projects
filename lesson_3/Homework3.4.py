inFile = open('referat.txt', 'r', encoding='utf8')
a = str(inFile.readlines())
print(len(set(a.split())))
inFile.close()

#Подсчитайте количество слов в тексте.