#01-07-2021 administrator tool to create a new tickit database

#Import JSON
import json

filename = "database.txt"

ticketdatabase = [
    {
        "dateordered" : "",
        "price" : "",
        "ticket0" : {
            "datevisit" : "",
            "age" : "",
            "qr" : ""
        },
        "ticket1" : {
            "datevisit" : "",
            "age" : "",
            "qr" : ""
        },
        "ticket2" : {
            "datevisit" : "",
            "age" : "",
            "qr" : ""
        }
    }
]    

with open(filename, "w") as output_file:
    json.dump(ticketdatabase, output_file)

input_file = open(filename)
tickets = json.load(input_file)
print(tickets)
