def lonelyinteger(a):
    # Write your code here
    test = []
    for number in a:
        if number not in test:
            test.append(number)
        else:
            test.remove(number)
    unique = test[0]
    return unique
