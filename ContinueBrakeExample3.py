# Fibonacci Series with a Twist:
# Generate the Fibonacci series up to the 10th term. 
# However, if a number in the series is even, skip it using continue. 
# Break out of the loop if the generated number exceeds 100.


fab_series=[0,1]

num=int(input("Enter the num:"))

for i in range(2,num):

    third_num =fab_series[-1] + fab_series[-2] 
    print(third_num)

    if third_num % 2==0:

        continue

    elif third_num>100:

        break
    else:
        fab_series.append(third_num)

print(fab_series)
