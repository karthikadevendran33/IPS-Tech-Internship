import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

# 1. DATASET
def create_dataset(n_samples=200):
    study_hours = np.round(np.random.uniform(0, 10, n_samples), 1)
    attendance = np.round(np.random.uniform(40, 100, n_samples), 0)
    previous_marks = np.round(np.random.uniform(30, 95, n_samples), 0)
    assignment_score = np.round(np.random.uniform(30, 100, n_samples), 0)
    score = (0.35*study_hours + 0.045*attendance + 0.045*previous_marks
             + 0.035*assignment_score - 10.2)
    probability = 1 / (1 + np.exp(-score))
    noise = np.random.normal(0, 0.25, n_samples)
    result = (probability + noise > 0.5).astype(int)
    return pd.DataFrame({"Study_Hours": study_hours, "Attendance": attendance,
                          "Previous_Marks": previous_marks,
                          "Assignment_Score": assignment_score, "Result": result})

df = create_dataset(200)
df.to_csv("student_dataset.csv", index=False)

# 2. PREPROCESSING (manual — no sklearn)
feature_cols = ["Study_Hours", "Attendance", "Previous_Marks", "Assignment_Score"]
X = df[feature_cols].values.astype(float)
y = df["Result"].values.reshape(-1, 1).astype(float)

def manual_train_test_split(X, y, test_ratio=0.2, seed=42):
    np.random.seed(seed)
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    test_size = int(X.shape[0] * test_ratio)
    test_idx, train_idx = indices[:test_size], indices[test_size:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

X_train, X_test, y_train, y_test = manual_train_test_split(X, y)

def standardize(X, mean=None, std=None):
    if mean is None:
        mean, std = X.mean(axis=0), X.std(axis=0)
    return (X - mean) / std, mean, std

X_train_scaled, train_mean, train_std = standardize(X_train)
X_test_scaled, _, _ = standardize(X_test, train_mean, train_std)

# 3. NEURAL NETWORK
def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(1)
    return {"W1": np.random.randn(input_size, hidden_size) * 0.1,
            "b1": np.zeros((1, hidden_size)),
            "W2": np.random.randn(hidden_size, output_size) * 0.1,
            "b2": np.zeros((1, output_size))}

def relu(Z): return np.maximum(0, Z)
def relu_derivative(Z): return (Z > 0).astype(float)
def sigmoid(Z):
    Z = np.clip(Z, -500, 500)
    return 1 / (1 + np.exp(-Z))

def forward_propagation(X, parameters):
    W1, b1, W2, b2 = parameters["W1"], parameters["b1"], parameters["W2"], parameters["b2"]
    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    return A2, {"Z1": Z1, "A1": A1, "Z2": Z2, "A2": A2}

def compute_loss(y_true, y_pred):
    eps = 1e-8
    y_pred_c = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(y_true*np.log(y_pred_c) + (1-y_true)*np.log(1-y_pred_c))

def backward_propagation(X, y, parameters, cache):
    m = X.shape[0]
    W2 = parameters["W2"]
    A1, A2, Z1 = cache["A1"], cache["A2"], cache["Z1"]
    dZ2 = A2 - y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * relu_derivative(Z1)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m
    return {"dW1": dW1, "db1": db1, "dW2": dW2, "db2": db2}

def update_parameters(parameters, grads, learning_rate):
    parameters["W1"] -= learning_rate * grads["dW1"]
    parameters["b1"] -= learning_rate * grads["db1"]
    parameters["W2"] -= learning_rate * grads["dW2"]
    parameters["b2"] -= learning_rate * grads["db2"]
    return parameters

def train(X, y, hidden_size=8, learning_rate=0.1, epochs=2000, print_every=100):
    parameters = initialize_parameters(X.shape[1], hidden_size, 1)
    loss_history = []
    for epoch in range(1, epochs + 1):
        A2, cache = forward_propagation(X, parameters)
        loss = compute_loss(y, A2)
        loss_history.append(loss)
        grads = backward_propagation(X, y, parameters, cache)
        parameters = update_parameters(parameters, grads, learning_rate)
        if epoch % print_every == 0 or epoch == 1:
            print(f"Epoch {epoch:4d}/{epochs}  -  Loss: {loss:.4f}")
    return parameters, loss_history

def predict(X, parameters, threshold=0.5):
    A2, _ = forward_propagation(X, parameters)
    return (A2 >= threshold).astype(int), A2

def evaluate(X, y, parameters):
    predictions, probabilities = predict(X, parameters)
    accuracy = np.mean(predictions == y) * 100
    print(f"Test Accuracy: {accuracy:.2f}%")
    for i in range(len(y)):
        print(int(y[i][0]), int(predictions[i][0]), round(probabilities[i][0], 4))
    return accuracy, predictions, probabilities

# 4. TRAIN
trained_parameters, loss_history = train(X_train_scaled, y_train,
                                          hidden_size=8, learning_rate=0.1,
                                          epochs=2000, print_every=100)

# 5. PLOT
plt.plot(loss_history)
plt.title("Training Loss Over Epochs")
plt.xlabel("Epoch"); plt.ylabel("Loss (Binary Cross-Entropy)")
plt.savefig("training_loss.png")

# 6. EVALUATE
test_accuracy, test_predictions, test_probabilities = evaluate(X_test_scaled, y_test, trained_parameters)

# 7. PREDICT NEW STUDENT
def predict_new_student(study_hours, attendance, previous_marks, assignment_score,
                         parameters, train_mean, train_std):
    new_data = np.array([[study_hours, attendance, previous_marks, assignment_score]], dtype=float)
    new_data_scaled = (new_data - train_mean) / train_std
    prediction, probability = predict(new_data_scaled, parameters)
    label = "PASS" if prediction[0][0] == 1 else "FAIL"
    print(f"Predicted Probability: {probability[0][0]:.2f}")
    print(f"Prediction: {label}")
    return probability[0][0], label

predict_new_student(6, 85, 72, 80, trained_parameters, train_mean, train_std)