# Q4) 
'''A toy vendor supplies three types of toys: Battery Based Toys, Key-based
Toys, and Electrical Charging Based Toys. The vendor gives a discount of
10% on orders for battery-based toys if the order is for more than Rs. 1000.
On orders of more than Rs. 100 for key-based toys, a discount of 5% is
given, and a discount of 10% is given on orders for electrical charging based
toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the product code and the order
amount and prints out the net amount that the customer is required to pay
after the discount.'''

def calculate_net_amount(product_code, order_amount):
  discount = 0.0

  if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
      discount = 0.10 * order_amount
  elif product_code == 2:  # Key-based Toys
    if order_amount > 100:
      discount = 0.05 * order_amount
  elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
      discount = 0.10 * order_amount
  else:
    print("Invalid product code. No discount applied.")
    return order_amount  # Return original amount if code is invalid

  net_amount = order_amount - discount
  return net_amount

# Get user input for product code and order amount
try:
  product_code = int(input("Enter product code (1: Battery, 2: Key-based, 3: Electrical): "))
  order_amount = float(input("Enter order amount: "))

  # Calculate and print the net amount
  net_payable = calculate_net_amount(product_code, order_amount)
  print(f"Net amount to pay: Rs. {net_payable:.2f}")

except ValueError:
  print("Invalid input. Please enter numeric values for product code and amount.")


'''
OutPut:- 
Enter product code (1: Battery, 2: Key-based, 3: Electrical): 2
Enter order amount: 5
Net amount to pay: Rs. 5.00
'''
