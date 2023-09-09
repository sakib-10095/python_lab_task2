n=int(input("Enter The Range Value:"))


list=[]

for i in range(11):
    i=int(input("Enter {} Items: ".format(i)))
    list.append(i)
print("my mobile Number:",list)


for i in range(len(list)-1):
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("The sortList with ascending number:",list)