
#conicoins = float(input("Please, enter the number of conicoins you have: "))
conicoins = float(input())

rates = {'RUB': 2.98,
         'ARS': 0.82,
         'HNL': 0.17,
         'AUD': 1.9622,
         'MAD': 0.208}

for currency, value in rates.items():
    print(f"I will get {round(conicoins * value, 2)} {currency} from the sale of {conicoins} conicoins.")



