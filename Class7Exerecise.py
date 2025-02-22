import datetime

def print_name_and_date(name):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Name: {name}")
    print(f"Printed on: {formatted_time}")

# Replace 'Your Name' with your actual name
print_name_and_date("shahar moshin")
