import random, time

winningNumber = 75
positionTortoise, positionHare = 0, 0

def TortoiseProbability(toss):
    toss = random.randint(1, 100)
    if toss >= 1 and toss <= 5:
        return 3
    elif toss > 5 and toss <= 7:
        return -6
    else:
        return 1

def HareProbability(toss):
    toss = random.randint(1,10)
    if toss >= 1 and toss <= 2:
        return 0
    elif toss >= 3 and toss <= 4:
        return 9
    elif toss == 5:
        return -12
    elif toss >= 6 and toss <= 8:
        return 1
    else:
        return -2

numberWinsTortoise = 0
numberWinsHare = 0

count = 0

for i in range(0, 10):

    print("Race number:", count)
    print("BANG! AND THEY'RE OFF!!!!!")
    
    TortoisePlace = 0
    HarePlace = 0

    HarePlace = HareProbability(HarePlace)
    TortoisePlace = TortoiseProbability(TortoisePlace)
    
    while HarePlace < 75 and TortoisePlace < 75:
        if HarePlace<=1:
            HarePlace = 1

        if TortoisePlace<= 1:
            TortoisePlace = 1

        for x in range(1,76):
            if HarePlace == TortoisePlace and TortoisePlace == x:
                print("OUCH!!", end= ' ')
            elif HarePlace == x:
                print("H", end = ' ')
            elif TortoisePlace == x:
                print("T",  end = ' ')
            else:
                print("-", end = ' ')
        print("\n")

        TortoisePlace = TortoisePlace + TortoiseProbability(TortoisePlace)
        HarePlace = HarePlace + HareProbability(HarePlace)

        if TortoisePlace >= 75 and HarePlace < 75:
            print('Tortoise wins!! YAY!!! at position', TortoisePlace)
            print('Hare loses. Yuch! at position', HarePlace)
            numberWinsTortoise+=1

        elif HarePlace >= 75 and TortoisePlace < 75:
            print('Hare wins!!! at position', HarePlace)
            print('Tortoise loses at position', TortoisePlace)
            numberWinsHare+=1

        elif TortoisePlace >= 75 and HarePlace >= 75:
            print("Tie")

    print("\Hare Wins: ", numberWinsHare)
    print("Tortoise Win: ", numberWinsTortoise, "\n")
    i + 1