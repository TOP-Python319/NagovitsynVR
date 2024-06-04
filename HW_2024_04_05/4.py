import random

with open('random.txt', 'w') as f:
    for i in range(25):
        f.write(str(random.randint(111,777)) + '\n')

f.close()

# 339
# 370
# 221
# 767
# 541
# 647
# 435
# 738
# 360
# 725
# 276
# 216
# 267
# 158
# 286
# 276
# 220
# 431
# 744
# 737
# 285
# 556
# 542
# 480
# 617
