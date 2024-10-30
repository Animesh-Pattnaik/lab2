import numpy as np

def calculate_d_statistic(sample):
    n = len(sample)
    sorted_sample = np.sort(sample)
    
    d_plus, d_min = 0, 0
    for i in range(n):
        d_plus = max(d_plus, (i/n - sorted_sample[i]))
        d_min = max(d_min, (sorted_sample[i] - (i - 1)/n))
    
    D = max(d_min, d_plus)
    return D

if __name__ == "__main__":
    n = int(input("Enter the number of sample values: "))
    
    sample = []
    print("Enter sample values (between 0 and 1):")
    for _ in range(n):
        value = float(input())
        sample.append(value)

    critical_value = float(input("Enter the critical value for the K-S test: "))

    D_statistic = calculate_d_statistic(sample)

    print(f"D-statistic: {D_statistic}")
    print(f"Critical value: {critical_value}")

    if D_statistic < critical_value:
        print("The null hypothesis is accepted. The sample follows the uniform distribution.")
    else:
        print("The null hypothesis is rejected. The sample does not follow the uniform distribution.")