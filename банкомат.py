denomination_banknotes = [5000,2000,1000,500,200,100]
money = int(input("Введите сумму"))
    for i in denomination_banknotes:
        count_banknotes = money // i
        money %= i
        print(f"Будет выдано купюр номинал в {i} - {count_banknotes}")
