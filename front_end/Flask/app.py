from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json, sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

def make_dict(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route("/")
def read():
    db_path = r'D:\Code\project\segTorch\use_sqlite\DBtest2.db'
    mydb = sqlite3.connect(db_path)
    mydb.row_factory = make_dict # make output to type dictionary(key:value)
    mycursor = mydb.cursor() 
    sqlQuery = "SELECT * FROM cctv"
    mycursor.execute(sqlQuery)
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult), 200)

@app.route("/<number>")
def readbyid(number):
    db_path = r'D:\Code\project\segTorch\use_sqlite\DBtest2.db'
    mydb = sqlite3.connect(db_path)
    mydb.row_factory = make_dict
    mycursor = mydb.cursor() 
    sqlQuery = "SELECT * FROM cctv WHERE number = {}".format(number)
    mycursor.execute(sqlQuery)
    myresult = mycursor.fetchall()
    return make_response(jsonify(myresult), 200)

@app.route("/", methods = ['POST'])
def create():
    data = request.get_json() # get data from POSTMAN ***
    db_path = r'D:\Code\project\segTorch\use_sqlite\DBtest2.db'
    mydb = sqlite3.connect(db_path)
    mydb.row_factory = make_dict
    mycursor = mydb.cursor()
    # sqlQuery = """ INSERT INTO cctv ("number", "rtspLink", "IPaddress", "Area", "Px", "LP", "Plot") VALUES (?, ?, ?, ?, ?, ?, ?) """
    # val = (data["number"], data["rtspLink"], data["IPaddress"], data["Area"], data["Px"], data["LP"], data["Plot"]) 
    sqlQuery = """ INSERT INTO cctv ("number", "rtspLink", "IPaddress", "Area") VALUES (?, ?, ?, ?) """
    val = (data["number"], data["rtspLink"], data["IPaddress"], data["Area"])
    mycursor.execute(sqlQuery, val)
    # print(val)
    mydb.commit()
    return make_response(jsonify({"create rowcount": mycursor.rowcount}), 200)

@app.route("/<number>", methods = ['PUT'])
def update(number):
    data = request.get_json()
    db_path = r'D:\Code\project\segTorch\use_sqlite\DBtest2.db'
    mydb = sqlite3.connect(db_path)
    mydb.row_factory = make_dict
    mycursor = mydb.cursor()
    sqlQuery = """ UPDATE cctv SET rtspLink = ?, IPaddress = ?, Area = ?, Px = ?, LP = ?, Plot = ? WHERE number = ? """
    val = (data["rtspLink"], data["IPaddress"], data["Area"], data["Px"], data["LP"], data["Plot"], number)
    mycursor.execute(sqlQuery, val)
    mydb.commit()
    return make_response(jsonify({"update rowcount": mycursor.rowcount}), 200)

@app.route("/<number>", methods = ['DELETE'])
def delete(number):
    # data = request.get_json() # dont use json already
    db_path = r'D:\Code\project\segTorch\use_sqlite\DBtest2.db'
    mydb = sqlite3.connect(db_path)
    mydb.row_factory = make_dict
    mycursor = mydb.cursor()
    sqlQuery = """ DELETE FROM cctv WHERE number = {} """.format(number)
    mycursor.execute(sqlQuery)
    mydb.commit()
    return make_response(jsonify({"delete rowcount": mycursor.rowcount}), 200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)