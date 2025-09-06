# Q5)
'''A transport company charges the fare according to following table:
Distance Charges
1-50 8 Rs./Km
51-100 10 Rs./Km
> 100 12 Rs/Km'''

def calculate_fare(distance):
  if distance < 1:
    return "Invalid distance. Please enter a positive value."
  elif distance <= 50:
    fare = distance * 8
  elif distance <= 100:
    fare = (50 * 8) + ((distance - 50) * 10)  # Calculate fare for first 50km at Rs 8, then rest at Rs 10
  else:  # distance > 100
    fare = (50 * 8) + (50 * 10) + ((distance - 100) * 12)  # Calculate fare for 1-50km, 51-100km, then rest at Rs 12
  return fare

# Get user input for distance
try:
  distance_traveled = float(input("Enter the distance traveled in kilometers: "))

  # Calculate and print the fare
  total_fare = calculate_fare(distance_traveled)

  if isinstance(total_fare, str):  # Check if it's an error message
    print(total_fare)
  else:
    print(f"The total fare is: Rs. {total_fare:.2f}")

except ValueError:
  print("Invalid input. Please enter a numeric value for the distance.")
   


'''
OutPut:- 
5 is =  Positive
-3 is =  Negative
0 is =  Zero
'''
