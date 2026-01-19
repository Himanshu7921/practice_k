def transferToAccount(p1, p2, how_much_to_send):
    if p1 > how_much_to_send:
        print("Money before Sedning...")
        print(f"p1: {p1}")
        print(f"p2: {p2}")

        # Money Sending Logic
        p1 = p1 - how_much_to_send
        p2 = p2 + how_much_to_send

        print(f"Money after Sending...")
        print(f"p1: {p1}")
        print(f"p2: {p2}")
    else:
        print("Unable to send Money, Insufficient Balance!")
    return p1, p2

p1 = 100
p2 = 130
send_money = 30

p1, p2 = transferToAccount(p1, p2, send_money)
print("Sending Again")
p1, p2 = transferToAccount(p1, p2, send_money)