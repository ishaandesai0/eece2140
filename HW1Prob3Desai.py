limit = 1000
for firstSide in range (1,limit):
    for secondSide in range (1,limit):
        for hypotenuse in range (1,limit):
            fs= firstSide
            ss = secondSide
            hpo = hypotenuse
            if(((fs*fs) + (ss*ss)) == hpo*hpo):
                print(fs, ss, hpo)


