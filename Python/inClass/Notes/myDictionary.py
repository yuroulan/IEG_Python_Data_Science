# py dict also called as JSON -->> javascript object notation
# dict is represented using {}
# dict is ordered (retain its position)
# dict is index using key(s) not number
# dict does not allow to duplicate keys but duplicate value

# "firstname":"Peter"
foreigner = {
   "firstname":"Peter",
   "lastname":"Parker",
   "passportNum":"E4854754",
   "incometaxNUm":"SG3839434",
   "lastmonth":5,
   "lastyear":2024,
   "lastamount":854,
   "transaction":[(4,2024,852),(3, 2024, 850),(2, 2024, 853),(1,10,854)],
   "adressess": {
       "office": {
           "street":"15 Lorong",
           "taman":"Eqi Park"
        },
        "home": {
            "street": "2if82jl",
            "taman":"mkdjiwd"
        }
    }
}

print(f"First Name: {foreigner["firstname"]}")
print(f"Last Name: {foreigner["lastname"]}")
print(f"Passport Number: {foreigner['passportNum']}")
print(f"Incom Tax Number: {foreigner['incometaxNUm']}")
print(f"Last Paid Month: {foreigner['lastmonth']}")
print(f"Last paid Year: {foreigner['lastyear']}")
print(f"Last Amount Paid: {foreigner['lastamount']}")

for month, year, amount in foreigner["transaction"]:
    print(f"{month} - {year} = RM{amount}")

officeadress = foreigner["adressess"]["office"]
print(officeadress["street"])
print(officeadress["taman"])

officeadress = foreigner["adressess"]["home"]
print(officeadress["street"])
print(officeadress["taman"])

# how to add new key
foreigner['car'] = {
    "brand":"Proton",
    "model":"SAGA",
    "carplateNum":"JDU3843"
}
print(foreigner)

foreigner['contact'] = "0193574883"
print(foreigner)

# modifiy existing data in dict
# it will update data

foreigner['contact'] = "01385475948"

# to drop a key
foreigner.pop('car')
print(foreigner)

foreigner['car'] = {
    "brand":"Proton",
    "model":"SAGA",
    "carplateNum":"JDU3843"
}

for key in foreigner.keys():
    print(key, foreigner[key])

for key in foreigner.keys():
    if(isinstance(foreigner[key], list)):
        for item in foreigner[key]:
            print(item)
    elif(isinstance(foreigner[key], dict)):
        for innerkeys in foreigner[key].keys():
            print(foreigner[key][innerkeys])
    else:
        print(key, foreigner[key])

'''for key, item in foreigner.items():
    print(key, item)'''

foreigner.clear()
print(foreigner)






