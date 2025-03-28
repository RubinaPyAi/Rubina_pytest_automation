def interest(p,t=2,r=0.10):
    s=(p*r*t)/100
    return s

prin=int(input("enter the principal: "))
simpleInterest=interest(prin)
print("simple interest with default ROI and time value is:",simpleInterest)
time=float(input("enter the time:"))
rate=float(input("enter the rate: "))
SI=interest(prin,time,rate)
print("The calculated simple interest with your provided ROI and time values is=",SI)









   

