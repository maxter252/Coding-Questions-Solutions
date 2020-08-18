def minimumBribes(q):
    bribes = {}
    total_bribes = 0
    sorted = False
    while not sorted:
        switches_made = False
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                switches_made = True
                if q[i] in bribes:
                    bribes[q[i]] += 1
                else:
                    bribes[q[i]] = 1

                if bribes[q[i]] > 2:
                    print ("Too chaotic")
                q[i], q[i+1] = q[i+1], q[i]
                total_bribes += 1
        if switches_made is False:
            sorted = True
    return total_bribes

minimumBribes([1,2,5,3,7,8,6,4])