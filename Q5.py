
n=int(input("Enter The Range Value:"))

count=0
for i in range(2,n):
    if n%i==0:
        count=1
if count==0:
    print("Prime number")
else:
    print("not prime")