import pandas as pd
import numpy as np

# Load Data
df = pd.read_csv('Iris.csv')

# Select Class 2 (Iris-versicolor) and Class 3 (Iris-virginica)
# 25 rows each to make 50 rows
df_versicolor = df[df['Species'] == 'Iris-versicolor'].head(25)
df_virginica = df[df['Species'] == 'Iris-virginica'].head(25)
df_subset = pd.concat([df_versicolor, df_virginica]).reset_index(drop=True)

# Features (4 features)
X = df_subset[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values

# Labels: class 2 -> [1, 0], class 3 -> [0, 1]
y = np.zeros((50, 2))
for i, species in enumerate(df_subset['Species']):
    if species == 'Iris-versicolor':
        y[i] = [1, 0] # Neuron 1
    else:
        y[i] = [0, 1] # Neuron 2

# Sigmoid Activation and Derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# MLP Class
class MLP:
    def __init__(self, input_size=4, hidden_size=2, output_size=2, learning_rate=0.1):
        self.lr = learning_rate
        # Initialize weights with fixed seed for reproducibility
        np.random.seed(42)
        self.W1 = np.random.uniform(-0.5, 0.5, (input_size, hidden_size))
        self.b1 = np.random.uniform(-0.5, 0.5, (1, hidden_size))
        
        self.W2 = np.random.uniform(-0.5, 0.5, (hidden_size, output_size))
        self.b2 = np.random.uniform(-0.5, 0.5, (1, output_size))
        
    def train(self, X, y, epochs):
        for epoch in range(epochs):
            # Feedforward
            hidden_input = np.dot(X, self.W1) + self.b1
            hidden_output = sigmoid(hidden_input)
            
            final_input = np.dot(hidden_output, self.W2) + self.b2
            final_output = sigmoid(final_input)
            
            # Backpropagation
            error = y - final_output
            
            d_final = error * sigmoid_derivative(final_output)
            error_hidden = d_final.dot(self.W2.T)
            d_hidden = error_hidden * sigmoid_derivative(hidden_output)
            
            # Update weights and biases
            self.W2 += hidden_output.T.dot(d_final) * self.lr
            self.b2 += np.sum(d_final, axis=0, keepdims=True) * self.lr
            
            self.W1 += X.T.dot(d_hidden) * self.lr
            self.b1 += np.sum(d_hidden, axis=0, keepdims=True) * self.lr
            
    def predict(self, X):
        hidden_input = np.dot(X, self.W1) + self.b1
        hidden_output = sigmoid(hidden_input)
        final_input = np.dot(hidden_output, self.W2) + self.b2
        final_output = sigmoid(final_input)
        return final_output

# Grid Search
epochs_list = [10, 100, 500]
lr_list = [0.1, 0.01, 0.001]

results = []
for epochs in epochs_list:
    for lr in lr_list:
        mlp = MLP(learning_rate=lr)
        mlp.train(X, y, epochs)
        predictions = mlp.predict(X)
        
        # Calculate accuracy
        predicted_classes = np.argmax(predictions, axis=1)
        true_classes = np.argmax(y, axis=1)
        accuracy = np.mean(predicted_classes == true_classes) * 100
        
        results.append((epochs, lr, accuracy))

print("Hasil Pencarian Parameter (Grid Search):")
print(f"{'Epochs':<10} | {'Learning Rate':<15} | {'Akurasi (%)':<10}")
print("-" * 45)
for res in results:
    print(f"{res[0]:<10} | {res[1]:<15} | {res[2]:.2f}%")
