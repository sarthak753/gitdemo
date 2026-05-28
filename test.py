def is_even(n):
    return n % 2 == 0


if __name__ == "__main__":
    try:
        value = int(input("Enter a number: ").strip())
        print(f"{value} is even." if is_even(value) else f"{value} is odd.")
    except ValueError:
        print("Please enter a valid integer.")
