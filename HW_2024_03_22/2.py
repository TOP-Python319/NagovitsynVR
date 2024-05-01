import math
def taxi_cost(len_of_ride:int, time_of_waiting:int=0):
    if len_of_ride < 0 or time_of_waiting < 0:
        return 'Error, try again'
    else:
        cost_of_waiting = time_of_waiting * 3
        cost_of_150 = 6 * len_of_ride//150
        if len_of_ride == 0:
            return 80 + cost_of_waiting
        else:
            return 80 + cost_of_waiting + cost_of_150
print(taxi_cost(0)) #80
print(taxi_cost(160))#86
print(taxi_cost(1500))#140
