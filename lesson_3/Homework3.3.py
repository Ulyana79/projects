def file_size(ref):
    with open ('referat.txt', 'r', encoding='utf8') as referat:
        text = referat.read()
    return len(text)

print(file_size('data.txt'))


#Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки.

#return len(referat.read())
#print(file_size('data.txt'))


       