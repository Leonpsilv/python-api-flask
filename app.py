from flask import Flask, make_response, request, jsonify
from db import myDb

app = Flask(__name__) # to use the name of current file
app.config['JSON_SORT_KEYS'] = False # to set false the alphabetic organization
myCursor = myDb.cursor()

@app.route('/carros', methods=['GET'])
def getCar():
    myCursor.execute('SELECT * FROM cars')
    myCars = myCursor.fetchall()
    cars = list()
    for eachCar in myCars:
        cars.append(
            {
                'id': eachCar[0],
                'brand': eachCar[1],
                'model': eachCar[2],
                'year': eachCar[3]
            }
        )

    return make_response(
            jsonify(cars)
    )

@app.route('/carros', methods=['POST'])
def createCar():
    car = request.json
    sql = f"INSERT INTO cars (brand, model, year) VALUES ('{car['brand']}', '{car['model']}', {car['year']})"
    myCursor.execute(sql)
    myDb.commit()
    return make_response(
        jsonify(
            message="Success to add car!",
            data=car
        )
    )

app.run() # start server