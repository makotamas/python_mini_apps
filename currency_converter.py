from forex_python.converter import CurrencyRates

def display_supported_currencies():
    print("Elérhető pénznemek:")
    print("---------------------")
    print("USD - Amerikai dollár")
    print("EUR - Euró")
    print("GBP - Brit font")
    # További pénznemek hozzáadhatók

def main():
    display_supported_currencies()

    amount = float(input("Kérem adja meg az összeget: "))
    from_currency = input("Kérem adja meg a kezdő pénznemet (pl. USD): ").upper()
    to_currency = input("Kérem adja meg a célpénzt (pl. EUR): ").upper()

    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)

    print(f"{amount} {from_currency} = {result} {to_currency}")

if __name__ == "__main__":
    main()
