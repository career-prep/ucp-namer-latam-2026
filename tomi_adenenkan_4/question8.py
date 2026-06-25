def coin_exchange(lst, integer):


    dp = [0] * (integer+1)
    dp[0] = 1
    for each in lst:
        for  i in range(each, integer+1):
            dp[i] += dp[i-each]
            print(dp[i], dp[i-each], i, each)

    return dp
