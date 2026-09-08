sum=0
count=0
while True:
    num=int(input("Enter number: "))
    if num==-1:
        break
    sum+=num
    count+=1
if count>0:
    avg=sum/count
    print("avg= ",avg)
    print("count= ",count)
else:
    print('no numbers were entered')
