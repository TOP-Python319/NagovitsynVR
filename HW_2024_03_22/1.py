def strong_password(password:str) ->bool:
    if len(password) > 8: #длина больше 8
        upperCounter = 0
        lowerCounter = 0
        for i in range(len(password)):
            if password[i].isupper():
                upperCounter += 1
            if password[i].islower():
                lowerCounter += 1
        if upperCounter > 0: #наличие больших букв
            if lowerCounter > 0: #наличие маленьких букв
                counter = 0
                for i in range(len(password)):
                    if password[i] in '0123456789':
                        counter += 1
                if counter >= 2: #наличие цифр
                    chars_counter = 0
                    for i in range(len(password)):
                        if password[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
                            chars_counter += 1
                            
                    if chars_counter >= 1: #наличие спец символов
                        return True    
                    else:
                        return False    
                else:
                    return False            
            else:
                return False
    else:
        return False
print (strong_password('aP3:kD_l3')) #True
print (strong_password('12345678')) #False
