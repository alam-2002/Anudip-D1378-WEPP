# Q4) Accept numbers using input() function until the user enters 0. If user input 0 then break the while loop and display the sum of all the numbers.

total_sum = 0  

while True:
    try:
        num = int(input("Enter a number (enter 0 to stop): "))  
        if num == 0:  
            break  
        total_sum = total_sum + num  
    except ValueError:
        print("Invalid input. Please enter a valid number.")  

print("The sum of all the numbers is:", total_sum) 


'''
OutPut:- 
Enter a number (enter 0 to stop): 1
Enter a number (enter 0 to stop): 2
Enter a number (enter 0 to stop): 3
Enter a number (enter 0 to stop): 4
Enter a number (enter 0 to stop): 5
Enter a number (enter 0 to stop): 6
Enter a number (enter 0 to stop): 7
Enter a number (enter 0 to stop): 8
Enter a number (enter 0 to stop): 9
Enter a number (enter 0 to stop): 0
The sum of all the numbers is: 45
'''
