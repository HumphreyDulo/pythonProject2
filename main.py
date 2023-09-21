import pandas as pd

# Load the Excel file
file_path = '/Users/User/Desktop/Test Files.xlsx'
df = pd.read_excel(file_path)

def generate_email_addresses(df):
    # Create an empty list to store generated email addresses
    email_addresses = []

    # Iterate through each row of the DataFrame
    for student_name in df['Student Name']:
        # Generate the email address from the student's name
        email = generate_email_from_name(student_name)

        # Ensure uniqueness
        while email in email_addresses:
            email += '1'

        # Add the generated email address to the list
        email_addresses.append(email)

    return email_addresses

def generate_email_from_name(student_name):
    # Split the student's name by ',' to separate last name and first/middle name
    last_name, first_middle_name = map(str.strip, student_name.split(','))

    # Extract the first letter of the first name and concatenate with the last name
    first_letter = first_middle_name[0].lower()
    email = f"{first_letter}{last_name.lower()}@gmail.com"

    return email

# Call the function to generate email addresses and store them in a variable
generated_emails = generate_email_addresses(df)

# Print the generated email addresses
for email in generated_emails:
    print(email)

