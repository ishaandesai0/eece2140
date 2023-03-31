def sumProduct(inMode, nums):
    counter = 0
    if inMode:
        counter = 1
        for i in nums:
            counter *=i
        print("The highest number in this list is: ", max(nums))
        print("The product of these numbers is: ", counter)
    else:
        for i in nums:
            counter += i
        print("The lowest number in this list is: ", min(nums))
        print("The sum of these numbers is: ", counter)

sumProduct(0, [1, 2, 3, 4, 5, 6])
sumProduct(1, [1, 2, 3, 4, 5, 6])