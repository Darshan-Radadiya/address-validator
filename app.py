import json
from flask import Flask, render_template, request

app = Flask(__name__)

# read Json file
with open('C:/Users/omkar/desktop/address-validator/Address_details.json','r') as file:
    data = json.load(file)

@app.route('/')
def home():
    # Get the list of countries from the json file.
    countries = [a_dict["Country"] for a_dict in data]

    return render_template('app.html', title="Home Page", countries=set(countries))

@app.route('/result_page',  methods=["POST"] )
def show_address():

    Country = request.form.get("country")
    State = request.form.get("State")
    Address_line_1 = request.form.get("Address_line_1")
    Address_Line_2 = request.form.get("Address_Line_2")
    Zipcode = request.form.get("Zipcode")
    ph_no = request.form.get("ph_no")

    address = Country  + State +  Address_line_1 + Address_Line_2 + Zipcode + ph_no 

    return render_template('result.html', title="Result Page", Address = address)

if __name__ == '__main__':
    app.run()

