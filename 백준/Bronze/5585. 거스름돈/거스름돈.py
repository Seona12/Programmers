money_list = [500,100,50,10,5,1]
money = int(input())
value = 1000 - money
count = 0
for money_one in money_list:
    count += (value // money_one)
    value %= money_one
print(count)