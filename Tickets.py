visitors = int(input("Сколько билетов вы хотите приобрести?"))

sum_ticket_price = 0
a = 1
for it in range(visitors):
    age = int(input(f"Какой возраст {a} гостя?"))
    if age < 18:
        ticket_price = 0
    elif 18 < age < 25:
        ticket_price = 990
    else:
        ticket_price = 1390
    it += 1
    a += 1
    sum_ticket_price += ticket_price

if visitors > 3:
    sum_ticket_price = sum_ticket_price * 0.9
    print("При покупке более 3 билетов применяется скидка 10%. \nСумма к оплате: ", sum_ticket_price, "р.")
else:
    print("Сумма к оплате: ", sum_ticket_price, "р.")