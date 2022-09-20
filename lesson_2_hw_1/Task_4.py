# Узнать кол-во USD
import decimal

amount_of_currency = decimal.Decimal(input("Введите сумму UAH которую хотите обменять: "))
# Узнать актуальный курс обмена
actual_exchange_rate = decimal.Decimal(input("Введите актуальный курс: "))
result = amount_of_currency / actual_exchange_rate
print("Сумма в USD: ", format(result, '.2f'))