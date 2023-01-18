from model import CNNModel
import init

if __name__ == "__main__":
    cnn_model = CNNModel()
    init.initialize(cnn_model)
    init.train(cnn_model)
    init.evaluate(cnn_model)
    while True:
        # prompt the user to input an image file path
        image_path = input("Enter an image file path: ")
        # predict the label of the image
        prediction = init.predict(cnn_model, image_path)
        # print the prediction
        print("Predicted label: ", prediction)
