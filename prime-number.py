def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primes_up_to(limit):
    """Return a list of prime numbers from 2 up to limit (inclusive)."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


def main():
    choice = input("Enter a number to check or a range like 10-50 to list primes: ").strip()

    if "-" in choice:
        try:
            start_str, end_str = choice.split("-", 1)
            start = int(start_str)
            end = int(end_str)
            if start < 2:
                start = 2
            if end < start:
                print("Invalid range. The end must be greater than or equal to the start.")
                return
            primes = [p for p in primes_up_to(end) if p >= start]
            print(f"Primes between {start} and {end}:")
            print(primes)
        except ValueError:
            print("Please enter a valid range in the format start-end, such as 10-50.")
    else:
        try:
            number = int(choice)
            if is_prime(number):
                print(f"{number} is a prime number.")
            else:
                print(f"{number} is not a prime number.")
        except ValueError:
            print("Please enter a valid integer or a range like 10-50.")


if __name__ == "__main__":
    main()
