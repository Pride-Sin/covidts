
def chart_porcentage(*args, decimals=1):
    ''' Takes an undefined amount of values, calculates each porcentage for the pie chart 
        in index and returns it as a list. '''
    porcentages = [0]
    total = sum(args)
    #!print(total)
    # Do rule of three with each arg and the total and append it to the porcentages list
    for arg in args:
        rule_of_three = round((arg * 100) / total, decimals)
        porcentages.append(porcentages[-1] + rule_of_three)

    #!print(porcentages)
    # Remove the first and last element (0 and 100)
    porcentages.remove(0)
    porcentages.pop()

    return porcentages