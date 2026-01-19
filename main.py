p1 = 30
p2 = 130

print("Money before Sedning...")
print(f"p1: {p1}")
print(f"p2: {p2}")
send_money = 31

if p1 <send_money:
    print("cannot send money")
else:


    p1 = p1 - send_money
    p2 = p2 + send_money

    print("Money after Sedning...")
    print(f"p1: {p1}")
    print(f"p2: {p2}")