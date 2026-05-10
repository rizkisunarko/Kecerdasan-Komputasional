import numpy as np
import pandas as pd

def step_function(net):
    return 1 if net >= 0 else 0

def train_perceptron(logic_name, X, y, alpha):
    w = np.zeros(X.shape[1])
    b = 0
    
    epoch = 0
    max_epochs = 1000
    
    print(f"--- Training {logic_name} Logic with Learning Rate {alpha} ---")
    
    while epoch < max_epochs:
        error_count = 0
        
        print(f"Epoch {epoch+1}")
        
        for i in range(len(X)):
            x = X[i]
            target = y[i]
            
            net = np.dot(w, x) + b
            net = round(net, 6)
            output = step_function(net)
            error = target - output
            
            print(f"  x={x}, target={target}, net={net:.4f}, output={output}, error={error}", end="")
            
            if error != 0:
                error_count += 1
                w = w + alpha * error * x
                b = b + alpha * error
                print(f" -> UPDATE: w={w}, b={b:.4f}")
            else:
                print(" -> No update")
                
        epoch += 1
        if error_count == 0:
            return epoch, w, b
            
    return epoch, w, b

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])
y_or = np.array([0, 1, 1, 1])

learning_rates = [0.1, 0.01, 0.001]
results = []

for alpha in learning_rates:
    epochs_and, w_and, b_and = train_perceptron("AND", X, y_and, alpha)
    results.append({
        "Logic": "AND",
        "Alpha": alpha,
        "Epochs": epochs_and,
        "Weights": w_and,
        "Bias": b_and
    })
    
    epochs_or, w_or, b_or = train_perceptron("OR", X, y_or, alpha)
    results.append({
        "Logic": "OR",
        "Alpha": alpha,
        "Epochs": epochs_or,
        "Weights": w_or,
        "Bias": b_or
    })

print("=== SUMMARY ===")
for r in results:
    print(f"Logic: {r['Logic']}, Alpha: {r['Alpha']} -> Converged in {r['Epochs']} epochs, Weights: {r['Weights']}, Bias: {r['Bias']:.4f}")
