def isHappy(n):
    squares = {
        "0": 0,
        "1": 1,
        "2": 4,
        "3": 9,
        "4": 16,
        "5": 25,
        "6": 36,
        "7": 49,
        "8": 64,
        "9": 81,

    }
    digits = str(n)
    count = 0
    while len(digits) > 1 or count < 2:
        count += 1
        sum = 0
        for digit in digits:
            sum += squares[digit]
        digits = str(sum)
    return int(digits) == 1
