def luckBalance(k, contests):
    contests.sort(reverse=True)
    luck = 0
    for contest in contests:
        print (contest)
        if k > 0:
            luck += contest[0]
            k -= 1
        elif contest[1] == 0:
            luck += contest[0]
        elif k == 0:
            luck -= contest[0]
    
    print (luck)

luckBalance(1,[[5,1],[4,1],[10,0]])