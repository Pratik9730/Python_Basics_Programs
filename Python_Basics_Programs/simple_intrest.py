def simple_intrest(p,t,r):
    print('The Principal Amount is: ',p)
    print('The time Period is: ',t)
    print('The rate of Intrest is: ',r)
    si = (p*t*r)/100
    print('TheSimple Intrest is: ',si)

p_amount = float(input("Enter Principal Amount: "))
time = float(input("Enter Time Period: "))
rate = float(input("Enter Rate of Intrest: "))
simple_intrest(p_amount, time, rate)


