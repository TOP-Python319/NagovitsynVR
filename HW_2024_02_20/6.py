def is_lucky_ticket(ticket:int):
    ticket = str(ticket)
    sum1 = 0
    sum2 = 0
    first_part = ticket[:3]
    second_part = ticket[3:]
    
    for _ in range(3):
        sum1 += int(first_part[_])
        sum2 += int(second_part[_])
    
    if sum1 == sum2:
        print('да')
    else:
        print('нет')

is_lucky_ticket(123456)
is_lucky_ticket(183534)
