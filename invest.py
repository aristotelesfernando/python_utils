def invest(amount, rate, years):
    for n in range(1, (years+1)):
        amount = amount + (amount * (rate/100))
        print(f"year {n} : {amount:,.2f}")


_amount = float(input("Informe a quantia: "))
_rate = float(input("Informe a taxa de juros: "))
_years = int(input("Informe a quantidade de anos: "))

invest(_amount, _rate, _years)
             
             
                
                
