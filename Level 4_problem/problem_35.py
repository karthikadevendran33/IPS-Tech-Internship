def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a, b = map(int, input("Enter two numbers: ").split())
answer = lcm(a, b)
print(answer)
