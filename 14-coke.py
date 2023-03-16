
i = 0
while i < 50:
    coin = int(input("insert coin: "))
    if coin == 10 or coin == 5 or coin == 25:
         i = i + coin
    else:
        i = i + 0
    if i < 50:
        print("Amount Due: ", 50 - i)
    else:
        break

print(f"Change Owed: {i - 50}")    
