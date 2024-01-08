
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
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
  }

  total_orders = 0

  while total_orders < 10:
    order = input(
      '''
      ***********************************
      ** What would you like to order? **
      ***********************************
      > '''
    ).capitalize()

    if order == 'Quit':
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



