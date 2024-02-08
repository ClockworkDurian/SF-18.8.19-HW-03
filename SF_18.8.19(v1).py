sum=0
qnt=int(input("Введите количество билетов:"))
for i in range(qnt):
    age=int(input("Введите возраст посетителя:"))
    if age<18:
        sum+=0
    elif 18<=age<=25:
        sum+=990
    elif age>25:
        sum+=1390
if qnt>3:
    sum=sum*0.9
print("Стоимость билетов составляет:",int(sum))