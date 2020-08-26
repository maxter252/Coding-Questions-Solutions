def candies(n, arr):
    left_to_right = [1]
    right_to_left = [1]
    rev_arr = arr[::-1]
    sum = 0 
    for i,x in enumerate(arr[1:],1): #range(len(arr))[1:]:
        if arr[i] > arr[i-1]:
            left_to_right.append(left_to_right[i-1] + 1)
        else:
            left_to_right.append(1)
        
    for i in range(len(arr))[1:]:
        if rev_arr[i] > rev_arr[i-1]:
            right_to_left.insert(0,right_to_left[i-1] + 1)
        else: 
            right_to_left.insert(0,1)
    print ("left_to_right:",left_to_right)
    print ("right_to_left:",right_to_left)
    for i in range(len(left_to_right)):
        sum += max (left_to_right[i], right_to_left[i])
    
    return sum



def candies2(n, arr):
    count = [1]
    for i,x in enumerate(arr[1:],1):
        if x <= arr[i-1]:
            count.append(1)
        else:
            count.append(count[i-1]+1)
    for i,x in enumerate(arr[-2::-1],2):
        if x <= arr[n-i+1]:
            count[n-i] = max(count[n-i], 1)
            print(count[n-i], end=' ')
        else:
            print(count[n-i+1]+1, end=' ')
            count[n-i] = max(count[n-i], count[n-i+1]+1)
    return sum(count)

print(candies  (8, [2,503,6,1,1,1,1,1,1]))
print(candies2 (8, [2,503,6,1,1,1,1,1,1]))