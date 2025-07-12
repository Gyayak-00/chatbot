while True:
    age = int(input("Enter your age: "))  
    if age <= 18:
        print("You are not adult")
    else:
        print("OK")
        phone_number = input("Enter your mobile number: ")
        if len(phone_number) == 10 and phone_number.isdigit():
            print("Give OTP")
        else:
            print("Invalid number")
        otp = input("enter the otp")
        if len(otp) == 6 and otp.isdigit():
            print("OK")
        else:
            print("invalid otp")
        adress = input("enter the address: ")
        print("OK")
        monthly_income= int(input("enter your income - "))
        if monthly_income <= 20000:
            print("you are not eligible")
        else:
            print("you are eligible ")
        press= input("press a to view your detail: ")
        if press == "a":
             print(f"""your detalils-AGE-{age}
                             PHONE NUMBER-{phone_number}
                            ADRESS-{adress}
                            MONTHLY INCOME-{monthly_income}""")
        else:
            print("error")
        helpline_number = input("enter h to see helpline number: ")
        if helpline_number == "h":
            print(""" YOU CAN CONTECT FOR YOUR CARD IN THIS NUMBER 
                  HELP LINE NUMBER- 999999999""")
        else:
            print("THNAKYOU")
        