def generate_pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

if __name__ == "__main__":
    n = 5
    generate_pascal_triangle(n)