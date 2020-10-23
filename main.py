def calc_stats(stat):
    result = 0

    if(stat == 1):
        result =- 2
    elif(stat == 2):
        result =- 1
    elif(stat == 3):
        result =+ 1
    elif(stat == 4):
        result =+ 2
    elif(stat == 5):
        result =+ 3
    else:
        result = 0

    return result

def calc_marks(marks):
    number_of_marks = []
    rate_of_marks = []

    for mark in range(marks):
        number_of_marks.append(int(input('Оценка от рекламодателя ' + str(mark + 1) + ' (1 - 5): ')))

    for mark in range(marks):
        rate_of_marks.append(calc_stats(number_of_marks[mark]))

    return sum((int(rate_of_marks[i]) for i in range(0, int(len(rate_of_marks)))))

def main():
    quality = int(input('Качество (0-5): '))
    activity = int(input('Активность (0-5): '))
    accepted = int(input('Принято (0 - ~): '))
    canceled = int(input('Отклонил (0 - ~): '))
    timeout = int(input('Просрочил (0 - ~): '))
    ambassador = int(input('Амбассадор (0 - ~): '))
    er = int(input('ER (1 - ~): '))
    marks = int(input('Количество оценок (0 - ~): ')) 

    quality = calc_stats(quality)
    activity = calc_stats(activity)
    marks = calc_marks(marks)
    
    return quality + activity + accepted + marks + ambassador + er - canceled - timeout * 2

print('Оценка: ' + str(main()))