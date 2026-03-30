# Q6_primes.py

start = int(input("Enter start: "))
end = int(input("Enter end: "))

primes = []

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

print("Prime numbers:", primes)
print("Count:", len(primes))
print("Sum:", sum(primes))