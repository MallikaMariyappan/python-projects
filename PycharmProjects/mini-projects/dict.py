details={
    "name":"mallika",
    "age":23
}

details2=dict(name='mallika',age=23)
print(details2)
print(details)
print(type(details))
print(len(details2))

#Access item
print(details['name'])
print(details.get('age'))

#list all keys
print(details.keys())

#list all values
print(details.values())

#list of key,value pair  as tuples
print(details.items())

#verify a key exit
print("name" in details)

#change values
details['name']='amu'
details.update({'place':'sattur'})

print(details)

#remove items
print(details.pop("place"))
print(details)

