
n=int(input("Enter The Range Value:"))


list=[]

for i in range(11):
    i=int(input("Enter {} Items: ".format(i)))
    list.append(i)
print("my mobile Number:",list)




max = list[0]
for i in list:
    if i>max:
        max=i

print("Maximum number from list is : ",max)


min = list[0]
for i in list:
    if i <min:
        min = i
print("Minimum number from list is : ",min)