#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<h1>Marcopolo paradiso g8 1800 dd 8x2 scania</h1><p>The model presented at Busworld Europe 2023 has a Scania K 500C B6x2*4NI Euro 6 chassis, with a Scania DC13 engine, 13 liters and 500 hp of power, Opticruise transmission, air suspension and 500 liter fuel tank. Fifteen meters long, 2.6 meters wide and 4.23 m high, the bus has the capacity to carry 35 passengers, 29 people on the top floor and six on the bottom floor. All seats are sleeper seats, with individual monitors and USB ports (type A and C), and, on the bottom floor, the seats also have a massage system.</p>"
if __name__=='__main__':
    app.run(debug=True)