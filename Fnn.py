import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load Iris dataset
X, y = load_iris(return_X_y=True)

# One-hot encode target labels
y = OneHotEncoder(sparse_output=False).fit_transform(y.reshape(-1, 1))

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build Feed Forward Neural Network
model = Sequential([
    Dense(10, input_dim=4, activation='relu'),   # hidden layer with 10 neurons
    Dense(8, activation='relu'),                 # another hidden layer
    Dense(3, activation='softmax')               # output layer (3 classes)
])

# Compile model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train model
history = model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=0)

# Evaluate
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"✅ Test Accuracy: {acc:.2f}")
