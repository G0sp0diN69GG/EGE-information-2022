import biblia as bib
y= True
def start() :
    global y
    y= True
    print("Даров, я программа решаюящая какое-то задание из егэ\nЯ помогаю людям подготовиться к ЕГЭ по информатике! \nСейчас я основана на ЕГЭ 2022, но в будущем будут дополнения\nЕсли хочешь выйти введи 00")
    exes = int(input("Какое задание ты хочешь решить?"))
    if exes==00:
        y=False
    elif exes ==1:
        bib.ex1()
    elif exes ==2:
        bib.ex2()
    elif exes==3:
        bib.ex3()
    elif exes==4:
        bib.ex4()
    elif exes==5:
        bib.ex5()
    elif exes==6:
        bib.ex6()
    elif exes==7:
        bib.ex7()
    elif exes==8:
        bib.ex8()
    elif exes==9:
        bib.ex9()
    elif exes==10:
        bib.ex10()
    elif exes==11:
        bib.ex11()
    elif exes==12:
        bib.ex12()
    elif exes==13:
        bib.ex13()
    elif exes==14:
        bib.ex14()
    elif exes==15:
        bib.ex15()
    elif exes==16:
        bib.ex16()
    elif exes==17:
        bib.ex17()
    elif exes==18:
        bib.ex18()
    elif exes==19:
        bib.ex19()
    elif exes==20:
        bib.ex20()
    elif exes==21:
        bib.ex21()
    elif exes==22:
        bib.ex22()
    elif exes==23:
        bib.ex23()
    elif exes==24:
        bib.ex24()
    elif exes==25:
        bib.ex25()
    elif exes==26:
        bib.ex26()
    elif exes==27:
        bib.ex27()
    else:
        print("Нет такого задания!")


while y:
    start()