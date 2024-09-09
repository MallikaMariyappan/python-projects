exp=[]
stop=False
while not stop:
   e=int(input("What is the expence ?(type 0 to stop)"))
   if e!=0:
       exp.append(e)
   else:
       stop=True
print(exp)
print("Total expence:",sum(exp))
print("max:",max(exp))
print("min:",min(exp))
