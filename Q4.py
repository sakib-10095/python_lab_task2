n=int(input("Enter The Range Value:"))


list=[]

for i in range(11):
    i=int(input("Enter {} Items: ".format(i)))
    list.append(i)
print("my mobile Number:",list)



evenlist=[]
oddlist=[]
for i in list:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print(evenlist)
print(oddlist)