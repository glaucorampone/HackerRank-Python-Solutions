def superDigit(n, k):
    # Write your code here
    while len(n) > 1:
        s = 0
        for digit in n:
            s += int(digit)
        n = str(s)
    s = s*k
    n = str(s)
    if s >= 10:
        s = int(n[0]) + int(n[1])
    return(s)

