import flask
from keras.models import load_model


app = flask.Flask(__name__)
model = None


def model_init(): 
    '''load your saved model here'''
    global model
    model = load_model('my_saved_model.h5')


def get_prediction():
    '''Define your prediction login here'''


@app.route("/")
def hello():
    return "send  post requests to /predict and get back results"


@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    if flask.request.method == "POST":
        if flask.request.form.get("test_data"):
            result = get_prediction(flask.request.form.get("test_data"))            
            data["success"] = True
            '''send back the results as response'''
            data["prediction"] = result 
        else: 
            data["msg"] = "Send Data to get prediction"
    return flask.jsonify(data)


if __name__ == "__main__":
    model_init():
    app.run(port=5000)