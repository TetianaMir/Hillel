# Узнать кол-во USD
amount_of_currency = float(input("Введите сумму UAH которую хотите обменять: "))
# Узнать актуальный курс обмена
actual_exchange_rate = float(input("Введите актуальный курс: "))
result = amount_of_currency / actual_exchange_rate
print("Сумма в USD: ", format(result, '.2f'))