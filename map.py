# In the previous problem - we wrote the program to accept 5 inputs on 5 separate lines.

# What will we do if we expect 100 inputs or test cases?
# What about 100,000 inputs or test cases?
# For taking a lot of test cases as input, we use loops.
# In the last problem, we told you that the number of test cases was 5.
# Usually the number of test cases is the first input you take and then take that input for each test case.

# Consider this test case

x = int(input())

for i in range(x):
       d = int(input())
       print(d)