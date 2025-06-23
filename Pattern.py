#PatternPrinting
rows= int(input("Enter a number of rows: "))
print("\n Your Pattern is \n")
for i in range (1, rows+1):
    for j in range(i):
        print("*", end= " ")
    print ()
    
