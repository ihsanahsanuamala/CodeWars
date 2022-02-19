def solution(number):
    # Initial Variable for Sum Process
    sum = 0
    # Do looping from 1 to number-1
    for i in range (1, number):         
        # If number divisible by 3 or 5 do sum process
        if i % 3==0 or i % 5==0:
            sum+=i
    return sum
print(solution(10))