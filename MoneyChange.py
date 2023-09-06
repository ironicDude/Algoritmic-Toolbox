def leastAmountOfChangeCoins(amount, coins):
    counter = 0
    coins.sort(reverse = True)
    for coin in coins:
        if coin <= amount:
            currentAmount = int(amount/coin)
            counter = counter + (currentAmount)
            amount = amount - (coin * currentAmount)
    return counter

amount = int(input())
print(leastAmountOfChangeCoins(amount,[1,5,10]))