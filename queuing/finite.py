def finite_queue_model(lamda, mu, K):
    if lamda >= mu:
        return "System is unstable (λ >= μ). The arrival rate must be less than the service rate."
    
    rho = lamda / mu
    P0 = (1 - rho) / (1 - rho**(K + 1))
    L = sum(n * P0 * rho**n for n in range(K + 1))
    PB = P0 * rho**K
    Lq = L - (1 - PB)
    W = L / (lamda * (1 - PB))
    Wq = W - 1 / mu
    
    return {
        "Utilization (ρ)": rho,
        "Probability of 0 customers (P0)": P0,
        "Average number in system (L)": L,
        "Average number in queue (Lq)": Lq,
        "Average time in system (W)": W,
        "Average time in queue (Wq)": Wq,
        "Blocking probability (PB)": PB
    }

lamda = float(input("Enter arrival rate (λ): "))
mu = float(input("Enter service rate (μ): "))
K = int(input("Enter system capacity (K): "))

result = finite_queue_model(lamda, mu, K)
if isinstance(result, str):
    print(result)
else:
    for metric, value in result.items():
        print(f"{metric}: {value:.4f}")
