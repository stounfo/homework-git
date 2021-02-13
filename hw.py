def sum_two_smallest_numbers(numbers):
    #your code here

    lowest1 = numbers[0]
    lowest2 = numbers[1]

    for i in numbers: 
          if i < lowest1:
                lowest1 = i

    for i in numbers:
          if i < lowest2:
                if i != lowest1:
                      lowest2 = i

    return lowest1 + lowest2