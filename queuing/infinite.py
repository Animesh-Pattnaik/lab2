def infinite_queue_model(lamda, mu):
    if lamda >= mu:
        return "System is unstable (λ >= μ). The arrival rate must be less than the service rate."
    
    rho = lamda / mu
    L = rho / (1 - rho)
    Lq = rho**2 / (1 - rho)
    W = 1 / (mu - lamda)
    Wq = rho / (mu - lamda)
    
    return {
        "Utilization (rho)": rho,
        "Average number in system (L)": L,
        "Average number in queue (Lq)": Lq,
        "Average time in system (W)": W,
        "Average time in queue (Wq)": Wq
    }

lamda = float(input("Enter arrival rate (λ): "))
mu = float(input("Enter service rate (μ): "))

result = infinite_queue_model(lamda, mu)
if isinstance(result, str):
    print(result)
else:
    for metric, value in result.items():
        print(f"{metric}: {value:.4f}")
