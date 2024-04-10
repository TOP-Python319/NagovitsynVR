def symbols_remover(text):
    without_symbols = ''
    symbols = '.,:;!?–—\'\|"()*/'
    for i in range(len(text)):
        if text[i] not in symbols:
            without_symbols += text[i]
    return without_symbols

print(symbols_remover('Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.'))

# Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство он 
# спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита   


# всё верно