
def chart_porcentage(*args):
    ''' Takes an undefined amount of values, calculates each porcentage for the pie chart 
        in index and returns it as a list. '''
    porcentages = [0]
    total = sum(args)

    for arg in args:
        rule_of_three = round((arg * 100) / total,1)
        porcentages.append(porcentages[-1] + rule_of_three)

    # Remove the first and last element (0 and 100)
    porcentages.remove(0)
    porcentages.pop()

    return porcentages