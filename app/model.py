class CNNModel:
    def init(self):
        # load the label information from labels.json
        with open('./dataset/training/labels.json', 'r') as f:
        self.training_labels = json.load(f)
        with open('./dataset/test/labels.json', 'r') as f:
        self.test_labels = json.load(f)
        with open('./dataset/evaluate/labels.json', 'r') as f:
        self.evaluate_labels = json.load(f)
        # Create a list of image file paths
        self.training_image_paths = ['./dataset/training/images/{}.{}'.format(label['image'], label['extension']) for label in self.training_labels]
        self.test_image_paths = ['./dataset/test/images/{}.{}'.format(label['image'], label['extension']) for label in self.test_labels]
        self.evaluate_image_paths = ['./dataset/evaluate/images/{}.{}'.format(label['image'], label['extension']) for label in self.evaluate_labels]
        # Create a list of labels
        self.num_classes = len(set([label['label'] for label in self.training_labels]))
        # Create a list of labels
        self.training_data = self.load_data(self.training_image_paths)
        self.test_data = self.load_data(self.test_image_paths)
        self.evaluate_data = self.load_data(self.evaluate_image_paths)
        # Call the create_model function
        self.model = self.create_model()

    def load_data(self, image_paths):
        data = []
        for path in image_paths:
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

    def evaluate(self, test_data, test_labels):
        test_loss, test_acc = self.model.evaluate(test_data, test_labels)
        print('Test accuracy:', test_acc)

    def predict(self, image_path):
        image = keras.preprocessing.image.load_img(image_path, target_size=(100, 100))
        x = keras.preprocessing.image.img_to_array(image)
        x = x.reshape((1,) + x.shape)
        return self.model.predict(x)

    def save_model(self):
        self.model.save('model.h5')

    def load_model(self):
        self.model = keras.models.load_model('model.h5')

