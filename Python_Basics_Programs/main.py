num = 0
sum = 0
count = 0
while True:
    num = input("Enter a Number :")
    if num == 'exit':
        break

    else:
        try:
            num = int(num)
            int(sum)
            sum = sum + num
            count = count+1

        except:
            print("Enter the valid number")
            continue

print("sum:", sum)
print("total valid inputs: ", count)
print("Average:", sum/count)



