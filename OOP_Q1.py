class SquareNumberSum:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        if isinstance(num, int) and num > 0:
            self.numbers.append(num)
        else:
            raise ValueError("Invalid input. Please provide a positive integer.")

    def calculate_sum(self):
        return sum(num ** 2 for num in self.numbers)

if __name__ == "__main__":
    try:
        square_sum = SquareNumberSum()

        while True:
            input_num = input("Enter a positive integer (or 'done' to finish): ")

            if input_num.lower() == "done":
                break

            try:
                number = int(input_num)
                square_sum.add_number(number)
            except ValueError as e:
                print(e)

        result = square_sum.calculate_sum()
        print("The sum of square numbers is:", result)

    except KeyboardInterrupt:
        print("\nProgram terminated by the user.")
