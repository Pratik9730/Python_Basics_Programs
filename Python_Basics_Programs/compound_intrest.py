def compound_intrest(p,t,r):
    print('The Principal Amount is: ', p)
    print('The time Period is: ', t)
    print('The rate of Intrest is: ', r)
    ci =p*(pow(((1+ r/100)), t))
    print('The Compund Intrest is: ', ci)

p_amount = float(input("Enter Principal Amount: "))
time = float(input("Enter Time Period: "))
rate = float(input("Enter Rate of Intrest: "))
compound_intrest(p_amount, time, rate)


