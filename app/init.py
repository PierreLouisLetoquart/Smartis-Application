from model import CNNModel

# Initialize the model
cnn_model = CNNModel()

# Split the data into training and test sets
train_data, test_data = cnn_model.training_data[:int(len(cnn_model.training_data) * 0.8)], cnn_model.training_data[int(len(cnn_model.training_data) * 0.8):]
train_labels, test_labels = cnn_model.training_labels[:int(len(cnn_model.training_labels) * 0.8)], cnn_model.training_labels[int(len(cnn_model.training_labels) * 0.8):]

# Train the model
cnn_model.train(train_data, train_labels)

# Evaluate the model
cnn_model.evaluate(test_data, test_labels)

# Use the model to predict labels for the evaluation data
predictions = [cnn_model.predict(img) for img in cnn_model.evaluate_data]
