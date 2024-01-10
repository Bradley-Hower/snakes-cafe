
def menu():
  menu = """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
  """
  print(menu)

  order_list = {
    'WINGS': 0,
    'COOKIES': 0,
    'SPRING ROLLS': 0,
    'SALMON': 0,
    'STEAK': 0,
    'MEAT TORNADO': 0,
    'A LITERAL GARDEN': 0,
    'ICE CREAM': 0,
    'CAKE': 0,
    'PIE': 0,
    'COFFEE': 0,
    'TEA': 0,
    'UNICORN TEARS': 0
  }

  total_orders = 0

  while total_orders < 10:
    order = input(
      '''
      ***********************************
      ** What would you like to order? **
      ***********************************
      > '''
    ).upper()

    if order == 'QUIT':
      return

    if order in order_list:
      order_list[order] += 1
      total_orders += 1
    else:
      print('Sorry, we do not serve that here.')

    if total_orders == 1:
      for name, value in order_list.items():
        if value > 0:
          print(f"""
                ** {value} order of {name} has been added to your meal **""")
    elif total_orders > 1:
      for name, value in order_list.items():
        if value > 0:
          print(f"""
                ** {value} order of {name} has been added to your meal **""")
  
menu()



