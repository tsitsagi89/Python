
i = 0
while i < 50:
    coin = int(input("insert coin: "))
    i = i + coin
    if i < 50:
        print("Amount Due: ", 50 - i)
    else:
        break

print(f"Change Owed: {i - 50}")    
