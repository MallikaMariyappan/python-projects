num=int(input("enter a number which table u want?"))
val=[(x+1)*num for x in range(20)]
val2=[str(x+1)+'x'+str(num)+'='+str((x+1)*num) for x in range(20)]
print(val2)
