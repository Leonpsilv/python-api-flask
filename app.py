from flask import Flask, make_response, request, jsonify
from db import myDb

app = Flask(__name__) # to use the name of current file
app.config['JSON_SORT_KEYS'] = False # to set false the alphabetic organization
myCursor = myDb.cursor()

@app.route('/')
def viewHome():
    return '<h1>Hello world</h1>'

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

@app.route('/carro', methods=['POST', 'GET', 'DELETE', 'PUT'])
def someCar():
    if request.method == 'POST':
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

    if request.method == 'GET':
        carModel = request.json
        sql = f"SELECT * FROM cars WHERE model='{carModel['model']}'"
        myCursor.execute(sql)
        myCar = myCursor.fetchall()
        if myCar == []:
            return make_response(jsonify(message="no car found!", data=[]))
        return make_response(
            jsonify(
                message= f"model {carModel['model']}:",
                data= myCar
            )
        )

    if request.method == 'DELETE':
        car = request.json
        myCursor.execute(f"SELECT * FROM cars WHERE id={car['id']}")
        selectedCar = myCursor.fetchall()
        if selectedCar == []:
            return make_response(jsonify(message="No car found!"))
        
        sql = f"DELETE FROM cars WHERE id={car['id']}"
        myCursor.execute(sql)
        myDb.commit()
        return make_response(jsonify(message=f"successfully deleted car!"))

    if request.method == 'PUT':
        car = request.json
        myCursor.execute(f"SELECT * FROM cars WHERE id={car['id']}")
        selectedCar = myCursor.fetchall()
        if selectedCar == []:
            return make_response(jsonify(message="No car found!"))
        
        sql = f"UPDATE cars SET brand='{car['brand']}', model='{car['model']}', year='{car['year']}' WHERE id='{car['id']}'"
        myCursor.execute(sql)
        myDb.commit()
        return make_response(
            jsonify(
                message="successfully to edit car",
                data=car
            )
        )

app.run() # start server