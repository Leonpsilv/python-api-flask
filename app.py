from flask import Flask, make_response, request, jsonify
from bd import Cars

app = Flask(__name__) # to use the name of current file
app.config['JSON_SORT_KEYS'] = False # to set false the alphabetic organization

@app.route('/carros', methods=['GET'])
def getCar():
    return make_response(
            jsonify(Cars)
    )

@app.route('/carros', methods=['POST'])
def createCar():
    car = request.json
    Cars.append(car)
    return make_response(
        jsonify(
            message="Success to add car!",
            data=car
        )
    )

app.run() # start server