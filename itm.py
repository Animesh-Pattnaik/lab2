import math
import random

def exponential_random(lambda_rate):
    U = random.random()
    return -math.log(1 - U) / lambda_rate

def geometric_random(p):
    U = random.random()
    return math.ceil(math.log(1 - U) / math.log(1 - p))

def uniform_random(a, b):
    return a + (b - a) * random.random()

if __name__ == "__main__":
    random.seed() 

    lambda_rate = float(input('Enter lambda rate: ')) # 1.0 
    exp_value = exponential_random(lambda_rate)
    print(f"Exponential random number with rate {lambda_rate}: {exp_value}")

    p = float(input("enter prob of success: ")) # p :ess than 1, prob of succeess
    geom_value = geometric_random(p)
    print(f"Geometric random number with probability {p}: {geom_value}")

    # a, b = 0, 1 
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    uniform_value = uniform_random(a, b)
    print(f"Uniform random number between {a} and {b}: {uniform_value}")
