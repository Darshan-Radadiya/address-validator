import json

address_data = '[{"Country":"India", "State":"Delhi", "Address_line_1":"12/7, Mile Stone,", "Address_Line_2":"Mathura ""Road","Zipcode":"121003", "ph_no":"951292276514"}, \
                 {"Country":"India", "State":"Andhra Pradesh", "Address_line_1":"17-3-897/9", "Address_Line_2":"Yakutpura Hyderabad","Zipcode":"500023", "ph_no":"04024577644"}]'

with open("Address_details.json", "w") as address_object:
    json.dump(address_data,address_object)
    print("JSON file created")