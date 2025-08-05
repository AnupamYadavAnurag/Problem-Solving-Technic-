def is_composite(n):
    if n <= 3:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def print_composites(start, end):
    print(f"Composite numbers between {start} and {end}:")
    for i in range(start, end + 1):
        if is_composite(i):
            print(i, end=' ')

# Example usage:
print_composites(1, 50)
