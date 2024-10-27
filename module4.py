# Function to find the index of X in the list of N numbers
def find_index():
    # Read the value of N
    N = int(input("Enter a positive integer N: "))

    # Initialize an empty list to store the numbers
    numbers = []

    # Read N numbers from the user
    for i in range(N):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Read the integer X
    X = int(input("Enter the integer X to find: "))

    # Check if X is in the list and output the result
    if X in numbers:
        index = numbers.index(X) + 1  # +1 to convert to 1-based index
        print(index)
    else:
        print(-1)

# Run the function
find_index()
