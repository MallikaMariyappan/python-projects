exp=-1
total=0
maxexp=0
minexp=1
while exp!=0:
    exp=int(input("What is the expence ?(type 0 to stop)"))
    total=total+exp
    if exp>maxexp:
         maxexp = exp
    elif exp>minexp:
        minexp=exp

print("Your total expenditure is:"+str(total))
print("the maximum you spent is"+str(maxexp))
print("the minimum you spent is"+str(minexp))