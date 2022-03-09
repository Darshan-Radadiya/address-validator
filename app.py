import json
from pickle import TRUE
from flask import Flask, render_template, request

app = Flask(__name__)

# read Json file
with open('./Address_details.json', 'r') as file:
# with open('C:/Users/omkar/desktop/address-validator/Address_details.json', 'r') as file:
    data = json.load(file)

@app.route('/')
def home():
    # Get the list of countries from the json file.
    countries = [a_dict["Country"] for a_dict in data]
    return render_template('app.html', title="Home Page", countries=sorted(set(countries)))

@app.route('/result_page',  methods=["POST"])
def show_address():

    # get the address detail from HTML form .
    Address_line_1 = request.form.get("Address_line_1")
    Address_Line_2 = request.form.get("Address_Line_2")
    State = request.form.get("State")
    County = request.form.get("county")
    Zipcode = request.form.get("Zipcode")
    Country = request.form.get("country")
    ph_no = request.form.get("ph_no")
    
    if County == None:
        County = ""
    
    match_found = False
    matching_add = ""

    user_entered_address = {"Address_line_1":Address_line_1.title(), "Address_Line_2":Address_Line_2.title(), "State":State.title(), "County":County.title(), "Zipcode":Zipcode.title(), "Country":Country, "ph_no":ph_no}    

    for i  in data:
        if i == user_entered_address:
            match_found = TRUE
        if i["Address_line_1"] == Address_line_1.title():
            matching_add = ", ".join(i.values())

    return render_template('result.html', title="Result Page", Address_line_1_value=Address_line_1, Address_Line_2_value=Address_Line_2, State_value=State, County_value=County, Zipcode_value=Zipcode, Country_value=Country, ph_no_value=ph_no, address_match = match_found, matching = matching_add)

if __name__ == '__main__':
    app.run(debug=True)
