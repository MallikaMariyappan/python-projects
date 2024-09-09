li=[]
# li.extend([2,3,4])
# print(li)

# num=1
# while num<=100:
#     li.append(num)
#     num=num+1
# for num in range(10):
#     li.append(num)


# l=[num*3 for num in range(20)]
# print(l)

users=['prince','maya','diya']

value=[True,24,'game']
print(value)
#we can store empty list
emptylist=[]
print(emptylist)

#we can add values using append and +=

emptylist.append("beycan")
print(emptylist)
emptylist+=['dev']
print(emptylist)


#to check the values is there or not it will return boolean values
#list accept negative value it return values last to first
print("diya" in users)

print(users[0])#prince
print(users[-1])#diya

#to find index value in list &&& index starts from 0

print(users.index('maya'))




