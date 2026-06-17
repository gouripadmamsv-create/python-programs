#''' number = 1
# 1>0 is true
# remainder = 1%10 = 1
# reverse = 56*10+1 = 561
# number = 1//10 = 0
# exit while'''


count=0
for number in range(1,101):
    temp=number
    while temp>0:
        digit=temp%10
        if digit == 9:
            count+=1
        temp//=10
print("Total Number of 9's: ",count)            

