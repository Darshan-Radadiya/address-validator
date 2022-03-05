import json

address_data = [{"Country":"India", "State":"Delhi", "Address_line_1":"12/7, Mile Stone,", "Address_Line_2":"Mathura ""Road","Zipcode":"121003", "ph_no":"951292276514"}, \
                 {"Country":"India", "State":"Andhra Pradesh", "Address_line_1":"17-3-897/9", "Address_Line_2":"Yakutpura Hyderabad","Zipcode":"500023", "ph_no":"04024577644"}]

with open("Address_details.json", "w") as address_object:
    json.dump(address_data,address_object)
    print("JSON file created")

filename = 'Address_details.json'
entry = {"Country":"India", "State":"Goa", "Address_line_1":" H no : 1134 second floor", "Address_Line_2":"Panaji Goa","Zipcode":"144424", "ph_no":"999999999"}
with open(filename,'r') as file:
    data = json.load(file)
data.append(entry)
with open(filename,'w') as file:
    json.dump(data,file)

