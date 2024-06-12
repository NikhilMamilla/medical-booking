import hashlib
import json
import os
import re
import sqlite3
import sys
import random
import time
import qrcode
import getpass

# Establish a connection to the SQLite database
conn = sqlite3.connect('user_database.db')
c = conn.cursor()

# Create a table for users if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, email TEXT UNIQUE, phone TEXT UNIQUE, password TEXT)''')
conn.commit()

CONFIG_FILE = 'user_config.json'

def save_credentials(email, phone, password):
    """Save user credentials to a JSON file."""
    with open(CONFIG_FILE, 'w') as file:
        json.dump({'email': email, 'phone': phone, 'password': password}, file)

def load_credentials():
    """Load user credentials from a JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as file:
            return json.load(file)
    return None

def clear_credentials():
    """Clear the saved user credentials by removing the JSON file."""
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)

def register(email, phone, password):
    """Register a new user with hashed password."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("INSERT INTO users (email, phone, password) VALUES (?, ?, ?)", (email, phone, hashed_password))
    conn.commit()
    print("User registered successfully!")
    save_credentials(email, phone, password)  # Save credentials

def login(email_phone, password):
    """Check if the provided credentials match any user in the database."""
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE email=? OR phone=?", (email_phone, email_phone))
    user = c.fetchone()
    if user and user[3] == hashed_password:
        print("Login successful!")
        save_credentials(user[1], user[2], password)
        return True
    else:
        print("Invalid email/phone or password.")
        clear_credentials()
        return False

def validate_email(email):
    """Validate email format."""
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def validate_phone(phone):
    """Validate phone number format."""
    return re.match(r'^[0-9]{10}$', phone)

def check_existing(email, phone):
    """Check if email or phone number already exists in the database."""
    c.execute("SELECT * FROM users WHERE email=? OR phone=?", (email, phone))
    user = c.fetchone()
    return bool(user)

def sign_up():
    """Prompt the user to sign up with email, phone number, and password."""
    while True:
        email = input("Enter your email: ")
        if not validate_email(email):
            print("Invalid email format. Please enter a valid email.")
            continue

        phone = input("Enter your phone number: ")
        if not validate_phone(phone):
            print("Invalid phone number format. Please enter a 10-digit phone number.")
            continue

        password = input("Enter your password: ")
        if check_existing(email, phone):
            print("Email or phone number already exists. Please use different credentials.")
            return False

        register(email, phone, password)
        return True

def prompt_login():
    """Prompt the user to login with email or phone number and password."""
    email_phone = input("Enter your email or phone number: ")
    password = input("Enter your password: ")
    return login(email_phone, password)

print("Welcome to the login system!")
while True:
  print("1. Sign up")
  print("2. Login")
  print("3. Exit")
  choice = input("Enter your choice: ")

  if choice == '1':
      if sign_up():
          print("Please login to continue.")
  elif choice == '2':
      if prompt_login():
          print("Proceeding to the next step...")
          break
      else:
          print("Please sign up if you don't have an account.")
  elif choice == '3':
      print("Exiting the program.")
      sys.exit()
  else:
      print("Invalid choice. Please try again.")

# Close the database connection when done
conn.close()

#Homepage of appointment scheduling solut
print('Welcome to BOOKITNOW')
print('1. Book an appointment')
print('2. View appointments')
print('3. Exit')
choices = int(input('Enter your choice: '))
if choices == 1:
  import calendar

  def generate_calendar(year):
      cal = calendar.TextCalendar(calendar.SUNDAY)
      months = []
      for month in range(1, 13):
          months.append(cal.formatmonth(year, month))
      return months

  def select_date_and_month():
      global year
      year=2024
      count = 0
      print("Calendar for the year 2024:")
      months = generate_calendar(year)
      while count != 1:
          print("Select a month (1-12) or enter '0' to exit:")
          global month
          month = int(input())
          if month == 0:
              break
          if month < 1 or month > 12:
              print("Invalid month. Please enter a number between 1 and 12.")
              continue
          print("Select a date:")
          print(months[month - 1])
          while True:
              global date
              date = int(input())
              if date < 1 or date > calendar.monthrange(year, month)[1]:
                  print("Invalid date. Please enter a valid date for the selected month.")
              print(f"You have selected: {calendar.month_name[month]} {date}, {year}")
              count = count + 1
              break
  select_date_and_month()
else:
  try:
      rec = int(input('Enter your receipt no: '))
      with open(f'{rec}.txt', 'r') as f:
          print(f.read())
  except FileNotFoundError:
      print(f'Receipt number {rec} not found.')
  except ValueError:
      print('Invalid input. Please enter a valid receipt number.')
  finally:
      sys.exit()   
patient_name=input(str('Enter your name: '))
age=int(input('Enter your age: '))
gender=input(str('Enter your gender: '))
rec=random.randint(10000,99929)
filename = f'{rec}.txt'
with open(filename,'a') as file:
    file.write("\n ")
    file.write("-----------------------------------------------")
filename = f'{rec}.txt'
with open(filename,'a') as file:
  file.write(f"\n\t\t\t\treciept no: {rec}\t\t\t\t\n")
  file.write("\n")
  file.write(f"Patient Name: {patient_name}\t\t")
  file.write(f"Age: {age}\n\n")
  file.write(f"Gender: {gender}\t\t")
  file.write(f"Appointment Date: {date} {month} {year}\n\n")

def disease():
    print('Hello! What is your problem?')
    print('1. Heart related problem')
    print('2. Teeth related problem')
    print('3. Skin related problem')
    print('4. Sexual health related problem')
    print('5. Fever, cold, and cough')
    print('6. Mental, emotional, and behavioral disorders')
    print('7. Traumatic injuries and physical abnormalities')
    print('8. BP and sugar related problems')
    print('9. Brain and nervous system related problem')
    print('10. Eyes nose and Throat related problems')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        while True:
            print('1. It is better to consult a cardiologist')
            print('Available cardiac specialists:')
            print('1. Dr. Sanjay Shetty, MBBS,M.C.D,MD-General medicine')
            print('2. Dr. Rajesh Kumar, DNB-Cardiology')
            print('3. Dr. Rohit Varma, MD-Cardiology,General medicine')
            print('4. Dr. Madhavi, DM-Cardiology')
            print('5. Dr. Raj Kumar, MBBS,DNB-Cardiothoracic surgery')

            doctor_choice = int(input('Enter your choice: '))

            if doctor_choice == 1:
                filename = f'{rec}.txt' 
                with open(filename,'a') as file:

                  file.write('Dr. Sanjay Shetty\n')
                  file.write('19 years of overall experience\n')
                  file.write('Specialization: Cardiology\n')
                  file.write('KIMS Hospital\n')
                  file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA.\n')
                  file.write('Hospital contact: +91-40-4488 5000 / +91-40-4488 5184')
                  break
            elif doctor_choice == 2:
                filename = f'{rec}.txt'
                with open(filename,'a') as file:

                  file.write('Dr. Rajesh Kumar\n')
                  file.write('21 years of overall experience\n')
                  file.write('Specialization: Cardiology\n')
                  file.write('APOLLO Hospital\n')
                  file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n')

                  file.write('Hospital contact: 040-23607777; 1860 258 1066')
                  break
            elif doctor_choice == 3:
                filename = f'{rec}.txt' 
                with open(filename,'a') as file:

                  file.write('Dr. Rohit Varma\n')
                  file.write('20 years of overall experience\n')
                  file.write('Specialization: Cardiology\n')
                  file.write('YASHODA Hospital\n')
                  file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n')

                  file.write('Hospital contact: +91 7353001899, +91 40 – 2770 3999')
                  break
            elif doctor_choice == 4:
                filename = f'{rec}.txt'
                with open(filename,'a') as file:

                  file.write('Dr. Madhavi\n')
                  file.write('19 years of overall experience\n')
                  file.write('Specialization: Cardiology\n')
                  file.write('CONTINENTAL Hospital\n')
                  file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
                  file.write('Hospital contact: 040 67000 000 / 04067000 111')
                  break
            elif doctor_choice == 5:
                filename = f'{rec}.txt'
                with open(filename,'a') as file:

                  file.write('Dr. Raj Kumar\n')
                  file.write('18 years of overall experience\n')
                  file.write('Specialization: Cardiology\n')
                  file.write('SUNSHINE Hospital\n')
                  file.write('Address: 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n')
                  file.write('Hospital contact: 040-44885000 / 040-4488 5184')
                  break

    elif choice == 2:
      while True:
        print('1. It is better to consult a dentist')
        print('Available dental specialists:')
        print('1. Dr. Neeraj Reddy, MDS-Orthodonist')
        print('2. Dr. Kiran Kumar, MDS-Prosthodonist And Crown Bridge BDS')
        print('3. Dr. Druvitha, MDS-Orthodontist')
        print('4. Dr. Sree Mouna, BDS,MDS-Oral & Maxillofacial Surgeon')
        print('5. Dr. Nikhil Kumar, Dental surgeon MDS-prosthodontist')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Neeraj Reddy\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Dental\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA.\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break
        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Kiran Kumar\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: Dental\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 258 1066,')
            break
        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Druvitha\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: Dental\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break
        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Sree Mouna\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Dental\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break
        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Nikhil Kumar\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: Dental\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachib \n')
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

    elif choice == 3:
      while True:
        print('1. It is better to consult a dermatologist')
        print('Avaliable dermatologists: ')
        print('1. Dr. Anup kumar, MDS-Dermatologist')
        print('2. Dr. Saravana, MBBS,DDVL')
        print('3. Dr. Kuldeep, MBBS,MD-Dermatology,Venerology')
        print('4. Dr. Rishi shetty, MBBS,DDVL')
        print('5. Dr. Keerthana, MBBS,Verenology & Leprosy')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Anup kumar\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Dermatology\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA.\n' )

            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break
        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Saravana\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: Dermatology\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 258 1066,')
            break
        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Kuldeep\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: Dermatology\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break
        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Rishi shetty\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Dermatology\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break
        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write(' Dr. Keerthana\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: Dermatology\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break


    elif choice == 4:
      while True:
        print('1. It is better to consult a gynecologist')
        print('Avaliable gynecologists: ')
        print('1. Dr. Divya, MBBS,Obsterician,DGO')
        print('2. Dr. Madhuri, MBBS,Gynecologist')
        print('3. Dr. Hansika, MBBS,Gynecologist')
        print('4. Dr. Nandan chowdary, Gynecologist,Laproscopic')
        print('5. Dr. Pawan, MBBS,Gynecologist')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write(' Dr. Divya\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Gynecology\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break
        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('You have selected Dr. Madhuri')
            file.write('21 years experience overall')
            file.write('Specialization: Gynecology')
            file.write('APOLLO Hospital')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033' )
            file.write('Hospital contact : 040-23607777; 1860 258 1066,')
            break

        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write(' Dr. Hansika\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: Gynecology\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break
        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Nandan chowdary\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Gynecology\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break
        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write(' Dr. Pawan\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: Gynecology\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

    if choice == 5:
      while True:
        print('1. It is better to consult a General Physician')
        print('Avaliable General Physicists: ')
        print('1. Dr. Karthik, General Physician')
        print('2. Dr. Shiva kumar, MBBS,General Physician')
        print('3. Dr. Pavani, MBBS,MD-General Physician')
        print('4. Dr. Hasini, MBBS,MD-General Physician')
        print('5. Dr. Narasimha reddy, MBBS,General Medicine')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Karthik\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: General medicine\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break

        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Shiva kumar\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: General medicine\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break
        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Pavani\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: General medicine\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break

        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Hasini\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: General medicine\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break

        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Narasimha reddy\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: General medicine\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break


    if choice == 6:
      while True:

        print('1. It is better to consult a Psychiatrist')
        print('Avaliable Psychiatrists: ')
        print('1. Dr. Vikram, Adult Psychiatry')
        print('2. Dr. Shiva Anoop, Child and Adolscence Psychiatry')
        print('3. Dr. Shanthi Mohan, Forensic Psychiatry')
        print('4. Dr. Sree Mouna, MBBS,Neuro psychiatry')
        print('5. Dr. Narasimha rao, Old age psychiatry')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Vikram\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Psychology\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break

        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Shiva Anoop\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: Psychology\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 258 1066,')
            break

        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Shanthi Mohan\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: Psychology\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break

        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Sree mouna\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Psychology\n')
            file.write('CONTINENTAL Hospital\n')
            ('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break

        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Narasimha rao\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: Psychology\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

    if choice == 7:
      while True:

        print('1. It is better to consult a General Surgeon')
        print('Avaliable General Surgeons: ')
        print('1. Dr. J Reddy, Pediatric Surgeon')
        print('2. Dr. Prudhviraj, Orthopedic Surgeon')
        print('3. Dr. Anil kumar, MBBS,critical Care Surgeon')
        print('4. Dr. Kalyan krishna, Cardiothoracic Surgeon')
        print('5. Dr. Nithya sree, MBBS,Neuro Surgeon')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. J Reddy\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: MBBS\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break

        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Prudhviraj\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: MBBS\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 258 1066,')
            break

        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Anil kumar\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: MBBS\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break

        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Kalyan krishna\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: MBBS\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break

        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Nithya sree\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: MBBS\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

    if choice == 8:
      while True:
        print('1. It is better to consult a Endocrinologist')
        print('Avaliable Pediatricians: ')
        print('1. Dr. Priyanka, Endocrinology')
        print('2. Dr. Thakur, MBBS,Endocrinology')
        print('3. Dr. Mahesh chowdary, Pediatric Endocrinology')
        print('4. Dr. Haneesha, MBBS,Endocrinology')
        print('5. Dr. Anusha Seethu, MBBS,Endocrinology')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Priyanka\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: MBBS,MD\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break
        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Thakur\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: MBBS,MD\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 21066,')
            break

        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Mahesh chowdary\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: MBBS,MD\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break

        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:
            file.write('Dr. Haneesha\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: MBBS,MD\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break

        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Anusha Seethu\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: MBBS,MD\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

    if choice == 9:
      while True:
        print('1. It is better to consult a Neurologist')
        print('Avaliable Neurologists: ')
        print('1. Dr. Siddarth Reddy, Child Neurology')
        print('2. Dr. Srinivas, Vascular Neurology')
        print('3. Dr. Naveen chandra, MBBS,Dementia')
        print('4. Dr. Mrudula, Neuromuscular Disabilities')
        print('5. Dr. Kashyap sai, BrainTumors')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:
            file.write('Dr. Siddarth Reddy\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Neurology\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break

        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Srinivas\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: Neurology\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 258 1066,')
            break

        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Naveen chandra\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: Neurology\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break

        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Mrudula\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Neurology\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break

        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Kashyap sai\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: Neurology\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

    if choice == 10:
      while True:
        print('1. It is better to consult a ENT Specialist')
        print('Avaliable Pulmonary Specialists: ')
        print('1. Dr. Vishnu, ENT/Otohinolarygologist')
        print('2. Dr. Chandrakanth, ENT/Otohinolarygologist')
        print('3. Dr. Raghava, MBBS,MS-ENT')
        print('4. Dr. Satya Prakesh, ENT/Otohinolarygologist')
        print('5. Dr. Priyanka Reddy, MBBS,MS-ENT')
        choice = int(input('Enter your choice: '))
        if choice == 1:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:

            file.write('Dr. Vishnu\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Pulmanology\n')
            file.write('KIMS Hospital\n')
            file.write('Address: KIMS Secunderabad. 1-8-31/1, Minister Rd, Krishna Nagar Colony, Begumpet, Secunderabad - 500003 Telangana INDIA\n' )
            file.write('Hospital contact : +91-40-4488 5000 / +91-40-4488 5184')
            break

        elif choice == 2:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:
            file.write('Dr. Chandrakanth\n')
            file.write('21 years experience overall\n')
            file.write('Specialization: Pulmanology\n')
            file.write('APOLLO Hospital\n')
            file.write('Address: Rd Number 72, opposite Bharatiya Vidya Bhavan School, Film Nagar, Hyderabad, Telangana 500033\n' )
            file.write('Hospital contact : 040-23607777; 1860 21066,')
            break

        elif choice == 3:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:
            file.write('Dr. Raghava\n')
            file.write('20 years experience overall\n')
            file.write('Specialization: Pulmanology\n')
            file.write('YASHODA Hospital\n')
            file.write('Address: Alexander Road, Secunderabad, Hyderabad – 500003\n' )
            file.write('Hospital contact : +91 7353001899. +91 40 – 2770 3999')
            break

        elif choice == 4:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:
            file.write('Dr. Satya Prakesh\n')
            file.write('19 years experience overall\n')
            file.write('Specialization: Pulmanology\n')
            file.write('CONTINENTAL Hospital\n')
            file.write('Address: Plot No 3, Road No. 2, Financial District, Gachibowli, Hyderabad, Telangana 500032\n')
            file.write('Hospital contact : 040 67000 000 / 04067000 111')
            break

        elif choice == 5:
          filename = f'{rec}.txt'
          with open(filename,'a') as file:
            file.write('Dr. Priyanka Reddy\n')
            file.write('18 years experience overall\n')
            file.write('Specialization: Pulmanology\n')
            file.write('SUNSHINE Hospital\n')
            file.write('Address: Address. 7-56/19, Dargah Road, LIG Chitrapuri Colony, Radhe Nagar, Rai Durg. Landmark: Near Vaishnoi Honda. Gachibowli, Hyderabad\n' )
            file.write('Hospital contact : 040-44885000 / 040-4488 5184')
            break

disease()

#slot booking
def slot_booking():
  print('1. Book a slot')
  print('2. Cancel a slot')
  print('3. View a slot')
  print('4. Exit')
  choice = int(input('Enter your choice: '))
  if choice == 1:
    print(date,month,year)
    print('1. Morning')
    print('2. Afternoon')
    print('3. Evening')
    print('4. Night')
    choice = int(input('Enter your choice: '))
    if choice == 1:
      print('Avaliable slots: ')
      print('1. 9:00 AM')
      print('2. 10:00 AM')
      print('3. 11:00 AM')
      choice = int(input('Enter your choice: '))
      if choice == 1:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
          file.write('9:00 AM\n')
        print('Your slot has been booked')
        print('Your slot is from 9:00 AM')
        print('Thank you for booking')
      elif choice == 2:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('10:00 AM\n')
        print('Your slot has been booked')
        print('Your slot is from 10:00 AM')
        print('Thank you for booking')
      elif choice == 3:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('11:00 AM\n')
        print('Your slot has been booked')
        print('Your slot is from 11:00 AM')
        print('Thank you for booking')
      else:
        print('Invalid choice')
    elif choice == 2:
      print('Avaliable slots: ')
      print('4. 1:00 PM')
      print('5. 2:00 PM')
      print('6. 3:00 PM')
      choice = int(input('Enter your choice: '))
      if choice == 4:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('1:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 1:00 PM')
        print('Thank you for booking')
        
      elif choice == 5:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('2:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 2:00 PM')
        print('Thank you for booking')
        
      elif choice == 6:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('3:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 3:00 PM')
        print('Thank you for booking')
      
      else:
        print('Invalid choice')
        
    elif choice == 3:
      print('Avaliable slots: ')
      print('7. 5:00 PM')
      print('8. 6:00 PM')
      print('9. 7:00 PM')
      choice = int(input('Enter your choice: '))
      if choice == 7:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('5:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 5:00 PM')
        print('Thank you for booking')
       
      elif choice == 8:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('6:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 6:00 PM')
        print('Thank you for booking')
        
      elif choice == 9:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('7:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 7:00 PM')
        print('Thank you for booking')
       
      else:
        print('Invalid choice')

    elif choice == 4:
      print('Avaliable slots: ')
      print('10. 9:00 PM')
      print('11. 10:00 PM')
      print('12. 11:00 PM')
      choice = int(input('Enter your choice: '))
      if choice == 10:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('9:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 9:00 PM')
        print('Thank you for booking')
        
      elif choice == 11:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('10:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 10:00 PM')
        print('Thank you for booking')
      
      elif choice == 12:
        filename = f'{rec}.txt'
        with open(filename,'a') as file:
            file.write('11:00 PM\n')
        print('Your slot has been booked')
        print('Your slot is from 11:00 PM')
        print('Thank you for booking')
   
      else:
        print('Invalid choice')
    
    else:
      print('Invalid choice')
     
  elif choice == 2:
    print('Enter the slot time you want to cancel: ')
    cancelled_slot = int(input('Enter your choice: '))
    if cancelled_slot == 1:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('9:00 AM\n')
        print('Your slot has been cancelled')
     
    elif cancelled_slot == 2:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('10:00 AM\n')
        print('Your slot has been cancelled')
 
    elif cancelled_slot == 3:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('11:00 AM\n')
        print('Your slot has been cancelled')
        
    elif cancelled_slot == 4:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('1:00 PM\n')
        print('Your slot has been cancelled')
     
    elif cancelled_slot == 5:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('2:00 PM\n')
        print('Your slot has been cancelled')
  
    elif cancelled_slot == 6:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('3:00 PM\n')
        print('Your slot has been cancelled')
    
    elif cancelled_slot == 7:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('5:00 PM\n')
        print('Your slot has been cancelled')
 
    elif cancelled_slot == 8:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('6:00 PM\n')
        print('Your slot has been cancelled')

    elif cancelled_slot == 9:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('7:00 PM\n')
        print('Your slot has been cancelled')
  
    elif cancelled_slot == 10:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('9:00 PM\n')
        print('Your slot has been cancelled')
  
    elif cancelled_slot == 11:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('10:00 PM\n')
        print('Your slot has been cancelled')
   
    elif cancelled_slot == 12:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('11:00 PM\n')
        print('Your slot has been cancelled')
 
    else:
      print('Invalid choice')

  elif choice == 3:
    print('Enter the slot time you want to view: ')
    view_slot = int(input('Enter your choice: '))
    if view_slot == 1:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('9:00 AM\n')
        print('Your slot is from 9:00 AM')
       
    elif view_slot == 2:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('10:00 AM\n')
        print('Your slot is from 10:00 AM')
     
    elif view_slot == 3:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('11:00 AM\n')
        print('Your slot is from 11:00 AM')
     
    elif view_slot == 4:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('1:00 PM\n')
        print('Your slot is from 1:00 PM')

    elif view_slot == 5:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('2:00 PM\n')
        print('Your slot is from 2:00 PM')
    
    elif view_slot == 6:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('3:00 PM\n')
        print('Your slot is from 3:00 PM')
     
    elif view_slot == 7:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('5:00 PM\n')
        print('Your slot is from 5:00 PM')
    
    elif view_slot == 8:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('6:00 PM\n')
        print('Your slot is from 6:00 PM')
    
    elif view_slot == 9:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('7:00 PM\n')
        print('Your slot is from 7:00 PM')
 
    elif view_slot == 10:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('9:00 PM\n')
        print('Your slot is from 9:00 PM')

    elif view_slot == 11:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('10:00 PM\n')
        print('Your slot is from 10:00 PM')
        
    elif view_slot == 12:
      filename = f'{rec}.txt'
      with open(filename,'a') as file:
        file.write('11:00 PM\n')
        print('Your slot is from 11:00 PM')
        
    else:
      print('Invalid choice')
    
  elif choice == 4:
    print('Thank you for visiting')
   
  else:
    print('Invalid choice')
   
slot_booking()

def choose_payment_method(reason, amount_to_pay):
    filename = f'transaction_record.txt'
    with open(filename, 'a') as file:
        file.write('\n')
        file.write('Reason: ' + reason)

    print(f'The amount to be paid is {amount_to_pay} INR')

    while True:
        print("Select payment method:")
        print("1. UPI")
        print("2. Debit Card")
        print("3. Credit Card")
        payment_method = input("Enter your choice: ")

        if payment_method == '1':
            make_upi_payment(amount_to_pay)
            break
        elif payment_method == '2':
            make_debit_card_payment(amount_to_pay)
            break
        elif payment_method == '3':
            make_credit_card_payment(amount_to_pay)
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def make_upi_payment(amount):
    while True:
        upi_id = input("Enter your UPI ID: ")
        filename = f'transaction_record.txt'
        with open(filename, 'a') as file:
            file.write('UPI ID: ' + upi_id + '\n')
        print(f"Initiating payment of {amount} INR via UPI to {upi_id}...")

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=1,
            border=1,
        )
        qr.add_data(f"upi://{upi_id}")
        qr.make(fit=True)

        qr.print_tty()

        print("QR code will be visible for 15 seconds for scanning.")
        start_time = time.time()
        while time.time() - start_time < 15:
            time_left = int(15 - (time.time() - start_time))
            print(f"Time left to scan: {time_left} seconds")
            time.sleep(1)
            if input("Would you like to request a new QR code? (yes/no): ").lower() == "yes":
                break
        else:
            print("Payment successful.")
            break

def make_debit_card_payment(amount):
    while True:
        card_number = input("Enter your debit card number: ")
        if card_number.isdigit() and len(card_number) == 16:
            break
        else:
            print("Invalid card number. Please enter a 16-digit number.")

    while True:
        expiry_date = input("Enter card expiry date (MM/YY): ")
        if len(expiry_date) == 5 and expiry_date[2] == '/' and expiry_date[:2].isdigit() and expiry_date[3:].isdigit():
            break
        else:
            print("Invalid expiry date format. Please enter in MM/YY format.")

    while True:
        cvv = getpass.getpass("Enter CVV: ")
        if cvv.isdigit() and len(cvv) == 3:
            break
        else:
            print("Invalid CVV. Please enter a 3-digit number.")

    filename = 'transaction_record.txt'
    with open(filename, 'a') as file:
        file.write('Card Number: ' + card_number + '\n')
        file.write('Expiry Date: ' + expiry_date + '\n')
        file.write('CVV: ' + cvv + '\n')
    print(f"Initiating payment of {amount} INR via Debit Card {card_number}...")
    time.sleep(10)
    print("Payment successful!")

def make_credit_card_payment(amount):
    while True:
        card_number = input("Enter your credit card number: ")
        if card_number.isdigit() and len(card_number) == 16:
            break
        else:
            print("Invalid card number. Please enter a 16-digit number.")

    while True:
        expiry_date = input("Enter card expiry date (MM/YY): ")
        if len(expiry_date) == 5 and expiry_date[2] == '/' and expiry_date[:2].isdigit() and expiry_date[3:].isdigit():
            break
        else:
            print("Invalid expiry date format. Please enter in MM/YY format.")

    while True:
        cvv = input("Enter CVV: ")  
        if cvv.isdigit() and len(cvv) == 3:
            break
        else:
            print("Invalid CVV. Please enter a 3-digit number.")

    filename = 'transaction_record.txt'
    with open(filename, 'a') as file:
        file.write('Card Number: ' + card_number + '\n')
        file.write('Expiry Date: ' + expiry_date + '\n')
        file.write('CVV: ' + cvv + '\n')

    print(f"Initiating payment of {amount} INR via Credit Card {card_number}...")
    time.sleep(10)
    print("Payment successful!")

reason = input("Enter the reason:")
amount_to_pay = random.randint(800, 1000)
choose_payment_method(reason, amount_to_pay)
