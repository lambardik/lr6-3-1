strings = [   
    "Джинсы Saint Laurent, она позвала в гости",
    "Прошли так много улиц, мы с кварталов, homie",
    "Шёл в дорогих педалях и я стёр подошву",
    "Скурил свои мозги, теперь мне стало проще, what?",
    "Е, весь мой гэнг со мной со школы",
    "Мы с тобою не похожи"
]
letters= "Вв"   
count = 0   
for line in strings:    
    for letter in letters:   
        if letter in line:  
            count += 1      
print("Кол-во строк,которые содержат букву 'в': ",count)