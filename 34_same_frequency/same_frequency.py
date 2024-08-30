def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    counter1 = {}
    counter2 = {}
    for digit in num1:
        counter1[digit] = counter1.get(digit, 0) + 1
    for digit in num2:
        counter2[digit] = counter2.get(digit, 0) + 1

    return counter1 == counter2