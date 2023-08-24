def minimumBribes(q):
    n = len(q)
    bribes = 0
    valid = True

    for i in range(n):
        if q[i] - (i + 1) > 2:
            valid = False
            print("Too chaotic")
            break

        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    if valid:
        print(bribes)
