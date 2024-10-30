import math

def poisson_distribution(lamda, n):
    probabilities = []
    for k in range(n + 1):
        p_k = (lamda ** k) * math.exp(-lamda) / math.factorial(k)
        probabilities.append(p_k)
    return probabilities

lamda = float(input('Enter lambda: '))
n = int(input("Enter n: "))
result = poisson_distribution(lamda, n)
for k, p in enumerate(result):
    print(f"P(X = {k}) = {p:.5f}")
