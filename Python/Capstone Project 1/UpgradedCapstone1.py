import datetime
from os.path import exists

class CustomerManagementSystem:
    def __init__(self):
        self.filename = "customer.txt"
        self.address_filename = "customer_address.txt"
        self.details_filename = "customer_details.txt"
        self.payment_method_filename = "customer_payment_details.txt"

        self.createFile(self.filename)
        self.createAddressFile(self.address_filename)
        self.createDetailsFile(self.details_filename)
        self.createPaymentMethodFile(self.payment_method_filename)

    # Keyboard input function
    def keyboardInput(self, datatype, caption, errorMessage, defaultValue=None):
        value = None
        isInvalid = True
        while isInvalid:
            try:
                if defaultValue is None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if value.strip() == "":
                        value = defaultValue
                    else:
                        value = datatype(value)
            except:
                print(errorMessage)
            else:
                isInvalid = False
        return value

    # Create files if they don't exist
    def createFile(self, filename):
        if not exists(filename):
            try:
                with open(filename, 'xt') as filehandler:
                    filehandler.write("FIRST NAME|LAST NAME|IC NO.|EMAIL ADDRESS|CONTACT NO.\n")
            except Exception as e:
                print("\n<< Something went wrong when we try to create the file! -->> ", e)

    def createAddressFile(self, address_filename):
        if not exists(address_filename):
            try:
                with open(address_filename, 'xt') as filehandler:
                    filehandler.write("IC NO.|ADDRESS LINE 1|ADDRESS LINE 2|CITY|STATE|ZIP CODE\n")
            except Exception as e:
                print("\n<< Something went wrong when we try to create the address file! -->> ", e)

    def createDetailsFile(self, details_filename):
        if not exists(details_filename):
            try:
                with open(details_filename, 'xt') as filehandler:
                    filehandler.write("FIRST NAME|LAST NAME|IC NO.|EMAIL ADDRESS|CONTACT NO.|EMERGENCY CONTACT NO.|NATIONALITY|MEDICAL CONDITION\n")
            except Exception as e:
                print("\n<< Something went wrong when we try to create the details file! -->> ", e)

    def createPaymentMethodFile(self, payment_method_filename):
        if not exists(payment_method_filename):
            try:
                with open(payment_method_filename, 'xt') as filehandler:
                    filehandler.write("IC NO.|PAYMENT METHOD|DETAILS\n")
            except Exception as e:
                print("\n<< Something went wrong when we try to create the payment method file! -->> ", e)

    # Register customer
    def registerCustomer(self):
        try:
            print("                         ")
            print('=' * 120)
            print("CUSTOMER REGISTRATION")
            print('=' * 120)
            firstname = self.keyboardInput(str,    "\nFIRST NAME  : ", "First Name must be a string").upper().strip()
            lastname = self.keyboardInput(str,     "LAST NAME    : ", "Lastname must be a string").upper().strip()
            ic_number = self.keyboardInput(str,    "IC NO.       : ", "IC No. must be in YYMMDDXXXXXX format").strip()
            ic_number = ic_number.replace("-", "")

            # Extracting last two digits of the year
            if len(ic_number) >= 6:
                year = ic_number[:2]  # YY from YYMMDDXXXXXX
                ic_number = year + ic_number[2:]  # Adjusting IC number to YYMMDDXXXXXX format

            email = self.keyboardInput(str,         "EMAIL ADDRESS      : ", "Email Address must be a string").strip()
            contact_no = self.keyboardInput(str,    "CONTACT NO.        : ", "Contact No. must be a string").strip()
            contact_no =contact_no.replace("-", "")

            print('_' * 120)

            # Writing to customer.txt
            with open(self.filename, 'at') as filehandler:
                filehandler.write(f"{firstname}|{lastname}|{ic_number}|{email}|{contact_no}\n")

            # Writing to customer_details.txt with empty fields for additional details
            with open(self.details_filename, 'at') as filehandler:
                filehandler.write(f"{firstname}|{lastname}|{ic_number}|{email}|{contact_no}|||\n")

            # Initialize empty address fields in the address file
            with open(self.address_filename, 'at') as filehandler:
                filehandler.write(f"{ic_number}|||||\n")

            print("\n-->> Customer registered successfully! <<--")
        except Exception as e:
            print("\n<< Something went wrong when we try to register the customer! -->> ", e)

    # Update customer details
    def updateCustomerDetails(self):
        try:
            lines = None
            with open(self.filename, 'rt') as filehandler:
                lines = filehandler.readlines()
            data = [line.strip().split('|') for line in lines]
            ic_number = self.keyboardInput(str, "\nEnter IC number for the customer update: ", "IC Number must be a string")
            ic_number = ic_number.replace("-", "")
            index = next((i for i, customer in enumerate(data) if customer[2] == ic_number), None)
            if index is None:
                print("\n>> Customer not found!")
            else:
                choice = -1
                while choice != 0:
                    print("\n+------------------------------+")
                    print("|                              |")
                    print("| \033[92m>> Update Customer Details\033[0m   |")
                    print("|                              |")
                    print("| 1 - Update Personal Details  |")
                    print("| 2 - Update Address           |")
                    print("| 3 - Update Payment Method    |")
                    print("|                              |")
                    print("| \033[91m0 - Back\033[0m                     |")
                    print("|                              |")
                    print("+------------------------------+\n")
                    

                    choice = self.keyboardInput(int, "\nYour Choice: ", "Choice must be an integer")
                    if choice == 1:
                        self.updatePersonalDetails(data, index)
                    elif choice == 2:
                        self.updateAddress(ic_number)
                    elif choice == 3:
                        self.updatePaymentMethod(ic_number)
                    elif choice == 0:
                        print("\n>> Returning to main menu...")
                    else:
                        print("\n>> Invalid choice. Please try again.")
        except Exception as e:
            print("\n<< Something went wrong when we try to update the customer details! -->> ", e)

    # Update personal details
    def updatePersonalDetails(self, data, index):
        try:
            customer = data[index]

            print("                                  ")
            print('=' * 120)
            print("CURRENT DETAILS")
            print('=' * 120)
            print("                                ")
            print(f"FIRST NAME     : {customer[0]}")
            print(f"LAST NAME      : {customer[1]}")
            print(f"IC NO.         : {customer[2]}")
            print(f"EMAIL ADDRESS  : {customer[3]}")
            print(f"CONTACT NO.    : {customer[4]}")
            print('_' * 120)
            print("\n\nUPDATE PERSONAL DETAILS HERE [OLD RECORDS APPEAR IN HERE]")
            print('_' * 120)
            print("                                                    ")
            
            new_firstname = self.keyboardInput(str,     f"FIRST NAME    [{customer[0]}]: ", "First Name must be a string", customer[0]).upper().strip()
            new_lastname = self.keyboardInput(str,      f"LAST NAME     [{customer[1]}]: ", "Last Name must be a string", customer[1]).upper().strip()
            new_email = self.keyboardInput(str,         f"EMAIL ADDRESS [{customer[3]}]: ", "Email must be a string", customer[3]).strip()
            new_contact_no = self.keyboardInput(str,    f"CONTACT NO.   [{customer[4]}]: ", "Contact No must be a string", customer[4])
            emergency_contact = self.keyboardInput(str, "EMERGENCY CONTACT NO.: ", "Emergency Contact must be a string").strip()
            emergency_contact = emergency_contact.replace("-", "")
            nationality = self.keyboardInput(str,       "NATIONALITY: ", "Nationality must be a string").upper().strip()
            medical_condition = self.keyboardInput(str, "MEDICAL CONDITION (leave blank if not applied): ", "Medical Condition must be a string").upper().strip()

            print('_' * 120)

            # Update customer_details.txt
            lines = None
            with open(self.details_filename, 'rt') as filehandler:
                lines = filehandler.readlines()
            lines[index] = f"{new_firstname}|{new_lastname}|{customer[2]}|{new_email}|{new_contact_no}|{emergency_contact}|{nationality}|{medical_condition}\n"
            with open(self.details_filename, 'wt') as filehandler:
                filehandler.writelines(lines)

            print("\n-->> Customer details updated successfully! <<--")
        except Exception as e:
            print("\n<< Something went wrong when we try to update the personal details! -->> ", e)

    # Update customer address
    def updateAddress(self, ic_number):
        try:
            lines = None
            with open(self.address_filename, 'rt') as filehandler:
                lines = filehandler.readlines()
            data = [line.strip().split('|') for line in lines]
            index = next((i for i, customer in enumerate(data) if customer[0] == ic_number), None)
            if index is None:
                print("\n>> Customer address details not found!")
            else:
                customer = data[index]

                print("                                  ")
                print('=' * 120)
                print("CURRENT ADDRESS")
                print('=' * 120)
                print("                                  ")
                print(f"ADDRESS LINE 1    : {customer[1]}")
                print(f"ADDRESS LINE 2    : {customer[2]}")
                print(f"CITY              : {customer[3]}")
                print(f"STATE             : {customer[4]}")
                print(f"ZIP CODE          : {customer[5]}")
                print('_' * 1200)
                print("\n\nUPDATE DETAILS HERE [OLD RECORDS APPEAR IN HERE]")
                print('_' * 60)
                print("                                  ")

                address_line1 = self.keyboardInput(str,             f"Address Line 1 [{customer[1]}]: ", "Address Line 1 must be a string", customer[1]).upper().strip(',').strip()
                address_line2 = self.keyboardInput(str,             f"Address Line 2 [{customer[2]}]: ", "Address Line 2 must be a string", customer[2]).upper().strip(',').strip()
                city = self.keyboardInput(str,                      f"City           [{customer[3]}]: ", "City must be a string", customer[3]).upper().strip()
                state = self.keyboardInput(str,                     f"State          [{customer[4]}]: ", "State must be a string", customer[4]).upper().strip()
                zip_code = self.keyboardInput(str,                  f"Zip Code       [{customer[5]}]: ", "Zip Code must be a string", customer[5]).strip()

                print('_' * 120)

                data[index][1:] = [address_line1, address_line2, city, state, zip_code]
                with open(self.address_filename, 'wt') as filehandler:
                    for customer in data:
                        filehandler.write('|'.join(customer) + '\n')
                print("\n-->> Address updated successfully! <<--")
        except Exception as e:
            print("\n<< Something went wrong when we try to update the address! -->> ", e)

    # Update payment method
    def updatePaymentMethod(self, ic_number):
        try:
            print("+------------------------------+")
            print("|                              |")
            print("|\033[92m >> Select Payment Method\033[0m     |")
            print("|                              |")
            print("| 1 - Credit / Debit Card      |")
            print("| 2 - Digital Wallet           |")
            print("| 3 - Bank Transfer            |")
            print("| 4 - Cash Payment             |")
            print("|                              |")
            print("+------------------------------+")


            method_choice = self.keyboardInput(int, "\nYour Choice: ", "Choice must be an integer")
            payment_method = None
            details = None

            if method_choice == 1:
                payment_method = "Credit / Debit Card"
                details = self.keyboardInput(str, "\n\nEnter Card Details (with '-'): ", "Card Details must be a string")
                payment_method = payment_method.replace("-", "")
            elif method_choice == 2:
                payment_method = "Digital Wallet"
                details = self.keyboardInput(str, "\n\nEnter Wallet Details: ", "Wallet Details must be a string")
            elif method_choice == 3:
                payment_method = "Bank Transfer"
                details = self.keyboardInput(str, "\n\nEnter Bank Details (with '-'): ", "Bank Details must be a string")
            elif method_choice == 4:
                payment_method = "Cash Payment"
                details = "Meet and pay to driver"
            else:
                print("\n\n>> Invalid choice. Payment method not updated.")

            if payment_method:
                with open(self.payment_method_filename, 'at') as filehandler:
                    filehandler.write(f"{ic_number}|{payment_method}|{details}\n")
                print("\n-->> Payment method updated successfully! <<--")
        except Exception as e:
            print("\nSomething went wrong when we try to update the payment method! -->> ", e)

    # Generate report
    def generateReport(self):
        try:
            ic_number = self.keyboardInput(str, "\nEnter IC number for report: ", "IC Number must be in YYMMDDXXXXXX format")
            ic_number = ic_number.replace("-", "")

            # Read and parse data files
            with open(self.filename, 'rt') as filehandler:
                customer_data = [line.strip().split('|') for line in filehandler.readlines()[1:]]  # Skip header

            with open(self.address_filename, 'rt') as filehandler:
                address_data = [line.strip().split('|') for line in filehandler.readlines()[1:]]  # Skip header

            with open(self.details_filename, 'rt') as filehandler:
                details_data = [line.strip().split('|') for line in filehandler.readlines()[1:]]  # Skip header

            with open(self.payment_method_filename, 'rt') as filehandler:
                payment_data = [line.strip().split('|') for line in filehandler.readlines()[1:]]  # Skip header

            # Create dictionaries for quick lookup
            address_dict = {item[0]: item[1:] for item in address_data}
            details_dict = {item[2]: item for item in details_data}  # using IC Number as key
            payment_dict = {item[0]: item[1:] for item in payment_data}

            # Find the customer data
            customer = next((cust for cust in customer_data if cust[2] == ic_number), None)

            if not customer:
                print("\n>> Customer not found!")
                return

            address = address_dict.get(ic_number, [""] * 5)
            details = details_dict.get(ic_number, [""] * 8)
            payment = payment_dict.get(ic_number, ["", ""])

            # Print customer report directly to console
            
            print("                                ")
            print('=' * 120)
            print("CUSTOMERS DETAILS")
            print('=' * 120)
            print("                                ")
            print("FULL NAME             : " + customer[0] + " " + customer[1])
            print(f"IC NO.                : {customer[2]}")
            print(f"EMAIL ADDRESS         : {customer[3]}")
            print(f"CONTACT NO.           : {customer[4]}")
            print(f"EMERGENCY CONTACT NO. : {details[5]}")
            print(f"NATIONALITY           : {details[6]}")
            print(f"MEDICAL CONDITION     : {details[7]}")
            print("ADDRESS               : " + address[0] + ", " + address[1] + ", " + address[2] + ", " + address[4] + ", " + address[3])
            print(f"PAYMENT METHOD        : {payment[0]}")
            print(f"PAYMENT DETAILS       : {payment[1]}")
            print('_' * 120)

# Check for upcoming birthday
            if len(ic_number) >= 6:
                try:
                    birthdate = datetime.datetime.strptime(ic_number[:6], "%y%m%d").date()
                    today = datetime.date.today()
                    next_birthday = birthdate.replace(year=today.year)
                    if next_birthday < today:
                        next_birthday = next_birthday.replace(year=today.year + 1)
                    days_until_birthday = (next_birthday - today).days

                    if 0 <= days_until_birthday <= 30:
                        print(f"\n-->> Next Birthday: {next_birthday} (in {days_until_birthday} days)")
                        print("\n-->> You are eligible for a birthday discount!")
                    else:
                        print(f"\n-->> No upcoming birthday within the next 30 days.")
                except ValueError:
                    print(f"\n>> Skipping invalid IC Number: {ic_number}")
            else:
                print(f"\n>> Skipping invalid IC Number: {ic_number}")

        except Exception as e:
            print("\n<< Something went wrong when we try to generate the report! -->> ", e)

    # Print customer report
    # this fx will generates and prints a customer report, also saving it to a file
    def printCustomerReport(self):
        try:
            lines = None
            with open(self.details_filename, 'rt') as filehandler:  # open the customer details file for a reading text
                lines = filehandler.readlines() # read all lines into a list

            customers = [line.strip().split('|') for line in lines[1:]] # Skip the first line (assuming it's a header) and split remaining lines by delimiter ('|')
            count_customers = len(customers)
            count_medical_condition = sum(1 for customer in customers if customer[7])   # Count customers with medical condition (assuming 7th element in the list indicates it)

            # print report header
            print("                               ")
            print('=' * 120)
            print("CUSTOMER REPORT")
            print('=' * 120)

            # print customer counts
            print(f"TOTAL CUSTOMERS: {count_customers}")
            print(f"TOTAL CUSTOMERS WITH MEDICAL CONDITION: {count_medical_condition}")
            print('_' * 120)

            # Save the report to a file
            with open("customer_report.txt", 'wt') as report_file:
                report_file.write("CUSTOMER REPORT\n")
                report_file.write('=' * 120 + '\n')
                report_file.write(f"TOTAL CUSTOMERS: {count_customers}\n")
                report_file.write(f"TOTAL CUSTOMERS WITH MEDICAL CONDITION: {count_medical_condition}\n")
                report_file.write('_' * 120 + '\n')
                
        except Exception as e:
            print("\n<< Something went wrong when we try to print the customer report! -->> ", e)

    # Main function
    def main(self):
        choice = None
        while choice != 'E':
            print("\n\n~ Welcome to Car Rental Customer Management System ~")
            print("+------------------------------------+")
            print("|                                    |")
            print("|\033[92m >> Menu\033[0m                            |")
            print("|                                    |")
            print("| 1 - Customer Registration          |")
            print("| 2 - Update Customer Details        |")
            print("| 3 - Generate Report                |")
            print("| 4 - Customer Registered Report     |")
            print("|                                    |")
            print("| \033[91mE - Exit\033[0m                           |")
            print("|                                    |")
            print("+------------------------------------+")

            choice = self.keyboardInput(str, "\nYour Choice: ", "Your choice must only be 1, 2, 3, or E").upper()

            if choice == '1':
                self.registerCustomer()
            elif choice == '2':
                self.updateCustomerDetails()
            elif choice == '3':
                self.generateReport()
            elif choice == '4':
                self.printCustomerReport()
            elif choice == 'E':
                print(">> Exiting the system...")
            else:
                print(">> Invalid choice. Please try again.")

if __name__ == "__main__":
    cms = CustomerManagementSystem()
    cms.main()


