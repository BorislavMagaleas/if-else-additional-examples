food_1_name      = 'Pizza'
food_1_price     = 100
food_1_available = 5
food_1_quantity  = int(input('How many ' + food_1_name + ' do you want ? '))
if food_1_quantity > 0 and food_1_quantity <= food_1_available:
    food_1_cost  = food_1_quantity * food_1_price
else:
    food_1_cost  = 0
    print('There is not sufficient quantity of ' + food_1_name)

food_2_name      = 'Salad'
food_2_price     = 40
food_2_available = 20
food_2_quantity  = int(input('How many ' + food_2_name + ' do you want ? '))
if food_2_quantity > 0 and food_2_quantity <= food_2_available:
    food_2_cost  = food_2_quantity * food_2_price
else:
    food_2_cost  = 0
    print('There is not sufficient quantity of ' + food_2_name) 

drink_name       = 'Green Tea'
drink_price      = 20
drink_available  = 50
drink_quantity   = int(input('How many ' + drink_name + ' do you want ? '))
if drink_quantity > 0 and drink_quantity <= drink_available:
    drink_cost   = drink_quantity * drink_price
else:
    drink_cost   = 0  
    print('There is not sufficient quantity of ' + drink_name)

if food_1_cost > 0:
    print('You have ordered ' + str(food_1_quantity) + ' x ' + food_1_name + ' = ' + str(food_1_cost))
if food_2_cost > 0:
    print('You have ordered ' + str(food_2_quantity) + ' x ' + food_2_name + ' = ' + str(food_2_cost))
if drink_cost > 0: 
    print('You have ordered ' + str(drink_quantity) + ' x ' + drink_name + ' = ' + str(drink_cost))

products_cost       = food_1_cost + food_2_cost + drink_cost

delivery         = input('Do you need the delivery? ')
if delivery == 'Yes' and products_cost > 1000:
    print('You have to pay ' + str(products_cost) + ' for your order.')
elif delivery == 'Yes' and products_cost < 1000:
    delivery_cost = 150
    total_cost    = products_cost + delivery_cost
    print('You have to pay ' + str(total_cost) + ' for your order.')
elif delivery == 'No':
    print('You have to pay ' + str(products_cost) + ' for your order.') 
else:
    print('Incorrect data was introduced.')