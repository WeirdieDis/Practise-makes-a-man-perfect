name= input ("Enter your name:")
print("You are requested to enter your marks out of 100.")
sub1= float(input("Enter your marks in Maths:"))
sub2= float(input("Enter your marks in Physics:"))
sub3= float(input("Enter your marks in Chemistry:"))
sub4= float(input("Enter your marks in English:"))
sub5= float(input("Enter your marks in Nepali:"))
#Calculate
total= sub1+sub2+sub3+sub4+sub5
average= total/5
#GradePlease
if average>= 90:
    grade= "A+"
elif average>= 80:
    grade= "A"
elif averag>=70:
    grade= "B+"
elif average>=60:
    grade= "B"
elif average>=50:
    grade="C+"
elif average>=40:
    grade="C"
else:
    grade="NG"
#LetsDisplay
print("\n ***** REPORT CARD *****")
print(f"Name    :{name}")
print(f"Total   :{total}")
print(f"Average :{average:.2f}")
print(f"Grade   :{grade}")