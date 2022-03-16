def Check_Rates(sales):
    Rates = (0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.0)
    TotalSales = (1000000.0,750000.0,500000.0,250000.0,100000.0,1.0,0)
    for n in range(len(TotalSales)):
        if sales > TotalSales[n]:
            return(Rates[n])

sales = ()
count = 1
Done = True

while Done:
    sale = float(input(f"Enter sale {count}(-1 to exit): "))
    if sale > -1.0:
        sales += (sale,)
        count += 1
    elif sale == -1:
        break

totals = sum(sales)
print(f"Total sales : {totals}")
Rates = Check_Rates(totals)
print(f"Commission Rates : {Rates*100}%")
commision = totals * Rates
print(f"Total commision : {commision}")
    
