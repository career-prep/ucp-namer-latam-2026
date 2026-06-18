def runningmedian(input):

    if len(input) == 0:
        return 0
    if len(input) == 1:
        return input[0]
    
    dp = [float("inf")] * (len(input))
    dp[0] = input[0]

    for i in range(1, len(input)):
        dp[i] = input[i]
        if (i+1) % 2 == 1:
            temp = sorted(dp[:i+1])
            dp[i] = temp[(i+1)//2]
        else:
            temp = sorted(dp[:i+1])
            dp[i] = (temp[(i+1)//2 - 1] + temp[(i+1)//2]) / 2
    return dp

print(runningmedian([1,11,4,15,12]))