
def cost_of_telegram(telegram):

    cost = 0

    telegram = telegram.lower().replace(' ', '')

    for i in range(len(telegram)):
        cost += 0.3
    
    rubles = int(cost)
    kopecks = round((cost - rubles) * 10)*10
    print(f'{rubles} руб. {kopecks} коп.')
    
cost_of_telegram('грузите апельсины бочках братья карамазовы')
#11 руб. 40 коп.

cost_of_telegram('один два три четыре')
#4 руб. 80 коп.
