
from vivacuba_my_librari import listen_command as lk, say_message as sm


def main():
    try:
        sm('скажи свой рост')
        rost = int(lk().replace("см", '').replace('  ', '.'))
        rost = rost/100
        print(rost)
        sm('теперь вес')
        wes = float(lk().replace("кг", '').replace('г', '').replace('грамм', '').strip().replace('  ', '.'))
        print(wes) 

    except ValueError:
        sm('похоже ты не назвал цифру или я с похмелья не разобрала, давай по новой')
        return main()
    
    bmi = (wes/(rost ** 2))  
    print(bmi)

    if bmi >= 10 and bmi <= 18.49:
        sm(" у Вас дефицит массы тела, нужно больше кушать, витамины там всякие, фрукты, овощи, ну и мясо наконец")
       
    elif bmi >= 18.5 and bmi <= 24.9:
        sm(" У Вас нормальная масса тела, ПОЗДРАВЛЯЮ! В здоровом теле, здоровый дух")
       
    elif bmi >= 25 and bmi <= 29.9:
        sm(" У вас избыточная масса тела, похоже после 6ти вечера кушать не стоит")
        
    elif bmi >= 30 and bmi <= 34.9:
        sm(" у вас ожирение первой степени: Ну, что сказать, холодильник на сигнализацию и включить сирену")
       
    elif bmi >= 35 and bmi <= 39.9:
        sm(" У вас ожирение второй степени: похоже нужно обратиться к врачу, со здоровьем не шутят")
        
    elif bmi >= 40:
        sm(" У вас ожирение третьей степени: без комментариев, только к врачу")
        

if __name__ == '__main__':
    sm('как тебя зовут:')
    name = lk().split()[-1]
    sm('привет ' + name + ' давай посчитаем твой индекс?')  
    main() 
