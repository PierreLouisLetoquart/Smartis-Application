import json
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class CNNModel:
    def __init__(self):
        # load the label information from labels.json
        with open('./preprocessedDataset/labels.json', 'r') as f:
            self.labels = json.load(f)
        # Create a list of image file paths
        self.image_paths = ['./preprocessedDataset/{}.{}'.format(label['image'], label['extension']) for label in self.labels]
        self.num_classes = len(set([label['image'] for label in self.labels]))
        self.data = self.load_data()
        self.model = self.create_model()

    def load_data(self):
        data = []
        for path in self.image_paths:
            image = keras.preprocessing.image.load_img(path, target_size=(100, 100))
            x = keras.preprocessing.image.img_to_array(image)
            data.append(x)
        return data

    def create_model(self):
        model = keras.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        # compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, train_data, train_labels, epochs=10):
        self.model.fit(train_data, train_labels, epochs=epochs)
    
    def evaluate(
        self, test_data, test_labels):
        test_loss, test_acc = self.model.evaluate(test_data, test_labels)
        print('Test accuracy:', test_acc)
    
    def predict(self, image_path):
        image = keras.preprocessing.image.load_img(image_path, target_size=(100, 100))
        x = keras.preprocessing.image.img_to_array(image)
        x = x.reshape((1,) + x.shape)
        return self.model.predict(x)

if name == 'main':
    cnn_model = CNNModel()
    train_images, test_images = cnn_model.data[:int(len(cnn_model.data) * 0.8)], cnn_model.data[int(len(cnn_model.data) * 0.8):]
    cnn_model.train(train_images, train_labels)
    cnn_model.evaluate(test_images, test_labels)
    while True:
    # prompt the user to input an image file path
    image_path = input("Enter an image file path: ")
    # predict the label of the image
    prediction = cnn_model.predict(image_path)
    # print the prediction
    print("Predicted label: ", prediction)
