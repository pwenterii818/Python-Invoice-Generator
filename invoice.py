import json
import os

def clientQuestioniare():

    # Asks the user for client information and returns it as a list for the clientSetup function
    client_fname = str(input("Enter your Client's First Name:\n"))
    os.system('cls')
    client_lname = str(input("Enter your Client's Last Name:\n"))
    os.system('cls')
    client_address = str(input("Enter your Client's Address:\n"))
    os.system('cls')
    client_city = str(input("Enter your Client's City:\n"))
    os.system('cls')
    client_state = str(input("Enter your Client's State:\n"))
    os.system('cls')
    client_zip = str(input("Enter your Client's Zip Code:\n"))
    os.system('cls')

    return [client_fname, client_lname, client_address, client_city, client_state, client_zip]

def clientSetup():

    # Keeps asking for client information until the user confirms it's correct
    info = False
    while info == False:
        questioniareInformation = clientQuestioniare()

        # Display the entered information for confirmation
        print(f"Client's First Name: {questioniareInformation[0]}")
        print(f"Client's Last Name: {questioniareInformation[1]}")
        print(f"Client's Address: {questioniareInformation[2]}")
        print(f"Client's City: {questioniareInformation[3]}")
        print(f"Client's State: {questioniareInformation[4]}")
        print(f"Client's Zip Code: {questioniareInformation[5]}\n")

        check = input("Is the information correct? (yes/no):\n")
        if check == "yes" or check == "y":
            print("Information confirmed.")
            os.system('cls')
            info = True
        elif check == "no" or check == "n":
            print("Please re-enter the information.")
            info = False
        else:
            print("Invalid input.")

    # Loads the client information to the JSON file
    with open("src/invoiceData.json", "r") as file:
        invoice_data = json.load(file)
    invoice_data["customerFName"] = questioniareInformation[0]
    invoice_data["customerLName"] = questioniareInformation[1]
    invoice_data["customerAddress"] = questioniareInformation[2]
    invoice_data["customerCity"] = questioniareInformation[3]
    invoice_data["customerState"] = questioniareInformation[4]
    invoice_data["customerZip"] = questioniareInformation[5]
    with open("src/invoiceData.json", "w") as file:
        json.dump(invoice_data, file, indent=4)

def updateInvoiceNumber():

    # Imports the JSON file
    with open("src/invoiceData.json", "r") as file:
        invoice_data = json.load(file)

    # Grabs the headers of the JSON file
    invoices = list(invoice_data.keys())

    # Update the invoice number
    newInvoice = f"invoice00{int(str(invoices[-1:])[-5:-2])+1}"

    # Update the JSON file with the new invoice number
    invoice_data[newInvoice] = {}
    with open("src/invoiceData.json", "w") as file:
        json.dump(invoice_data, file, indent=4)