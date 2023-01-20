import numpy as np
number=np.random.randint(1,101)
count=0
while True:
    count+=1
    predict_number=int(input("Угадай чмсло от 1 до 100 :"))
    if predict_number > number:
        print("Не, надо помене ...")
    if predict_number < number:
        print("Не, поболе чуток ...")
    if predict_number == number:
        print("Угадал, чертяка !!!!!!!!")
        break
    if count >10 :
        print("Ну ты совсем чего-то тупой .")
        break
    