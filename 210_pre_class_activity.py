
not_yet = "We don't ship to that city yet"

def calculateShipping(city, product):
    if city == 'Chicago':
        if product < 10:
            costOfShipping = 5
        elif product < 20:
            costOfShipping = 8
        elif product < 30:
            costOfShipping = 12
        else:
            costOfShipping = 15
    elif city == 'Denver':
        if product < 10:
            costOfShipping = 7
        elif product < 20:
            costOfShipping = 9
        elif product < 30:
            costOfShipping = 13
        else:
            costOfShipping = 20
    else:
        costOfShipping = not_yet
    return costOfShipping

# Example: Product is 13, City is Chicago
productsOfUser = 13  # This is the product number
cityOfUser = 'Chicago'  # This is the city name

amountForShipping = calculateShipping(cityOfUser, productsOfUser)

if amountForShipping == not_yet:
    print('Sorry, we do not ship to', cityOfUser)
else:
    print('It will cost $' + str(amountForShipping) + ' to ship your package')

# Example: Product is 35, City is Denver
productsOfUser = 35  # This is the product number
cityOfUser = 'Denver'  # This is the city name

amountForShipping = calculateShipping(cityOfUser, productsOfUser)

if amountForShipping == not_yet:
    print('Sorry, we do not ship to', cityOfUser)
else:
    print('It will cost $' + str(amountForShipping) + ' to ship your package')

# Example: Product is 5, City is New York
productsOfUser = 5  # This is the product number
cityOfUser = 'New York'  # This is the city name

amountForShipping = calculateShipping(cityOfUser, productsOfUser)

if amountForShipping == not_yet:
    print('Sorry, we do not ship to', cityOfUser)
else:
    print('It will cost $' + str(amountForShipping) + ' to ship your package')

