

from math_operation import multiply, divide, modulus

def get_number(prompt):
	"""Get a number from the user with the given prompt"""
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Invalid Input. Please enter a numeric value.")


def main():
	print("Welcome to the basic calculator")

	while True:
		print("\n Select Operation : ")
		print("1. Multiply")
		print("2. Divide")
		print("3. Modulus")
		print("4. Exit")

		choice = input("Enter choice(1/2/3/4) : ")

		if choice=='4':
			print("Exiting the Calculator. Good Bye!")
			break

		elif choice in ['1','2','3']:
			operation = ""
			if choice == '1':
				operation = "Multiply"
			elif choice == '2':
				operation = "Divide"
			elif choice == '3':
				operation = "Modulus"
            
			print(f"You chose to {operation}.")	

			num1 = get_number("Enter the first number : ")
			num2 = get_number("Enter the second number : ")

			if choice =='1':
				print(f"\n Multiplication of {num1} and {num2} = {multiply(num1,num2)}")

			elif choice =='2':
				print(f"\n Division of {num1} and {num2} = {divide(num1,num2)}")

			elif choice =='3':
				print(f"\n Modulus of {num1} and {num2} = {modulus(num1,num2)}")

		else:
			print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
	main()