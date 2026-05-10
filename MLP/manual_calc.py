import pandas as pd
import numpy as np

df = pd.read_csv('Iris.csv')
df_versicolor = df[df['Species'] == 'Iris-versicolor'].head(25)
df_virginica = df[df['Species'] == 'Iris-virginica'].head(25)
df_subset = pd.concat([df_versicolor, df_virginica]).reset_index(drop=True)

X = df_subset[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
y = np.zeros((50, 2))
y[0] = [1, 0] # First row is versicolor

def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x): return x * (1 - x)

np.random.seed(42)
W1 = np.random.uniform(-0.5, 0.5, (4, 2))
b1 = np.random.uniform(-0.5, 0.5, (1, 2))
W2 = np.random.uniform(-0.5, 0.5, (2, 2))
b2 = np.random.uniform(-0.5, 0.5, (1, 2))

lr = 0.1
x0 = X[0:1] # (1, 4)
y0 = y[0:1] # (1, 2)

print("=== INIT ===")
print("Input x:", x0)
print("Target y:", y0)
print("W1:\n", W1)
print("b1:\n", b1)
print("W2:\n", W2)
print("b2:\n", b2)

# Feedforward
hidden_input = np.dot(x0, W1) + b1
hidden_output = sigmoid(hidden_input)

final_input = np.dot(hidden_output, W2) + b2
final_output = sigmoid(final_input)

print("\n=== FEEDFORWARD ===")
print("hidden_input (z1) = x * W1 + b1 =\n", hidden_input)
print("hidden_output (a1) = sigmoid(z1) =\n", hidden_output)
print("final_input (z2) = a1 * W2 + b2 =\n", final_input)
print("final_output (a2) = sigmoid(z2) =\n", final_output)

# Backprop
error = y0 - final_output
d_final = error * sigmoid_derivative(final_output)

error_hidden = d_final.dot(W2.T)
d_hidden = error_hidden * sigmoid_derivative(hidden_output)

print("\n=== BACKPROPAGATION ===")
print("Error = target - a2 =\n", error)
print("d_final (delta2) = Error * a2 * (1 - a2) =\n", d_final)
print("Error hidden = delta2 * W2.T =\n", error_hidden)
print("d_hidden (delta1) = Error hidden * a1 * (1 - a1) =\n", d_hidden)

# Update
W2_new = W2 + hidden_output.T.dot(d_final) * lr
b2_new = b2 + d_final * lr

W1_new = W1 + x0.T.dot(d_hidden) * lr
b1_new = b1 + d_hidden * lr

print("\n=== UPDATE WEIGHTS (lr = 0.1) ===")
print("W2_new = W2 + a1.T * delta2 * lr =\n", W2_new)
print("b2_new = b2 + delta2 * lr =\n", b2_new)
print("W1_new = W1 + x.T * delta1 * lr =\n", W1_new)
print("b1_new = b1 + delta1 * lr =\n", b1_new)
