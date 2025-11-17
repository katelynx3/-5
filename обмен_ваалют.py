def convert_usd_to_rub (usd):
    """конвертирует введенную сумму $ в руб
    args:
        amount_usd(float)
    returns:
        float: сумма руб"""
    usd_to_rub = 95.50
    rub = amount_usd * usd_to_rub
    return rub
usd = float(input("введите кол-во $ "))
print(convert_usd_to_rub(usd))
