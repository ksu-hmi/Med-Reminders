#new code with code changes 
def input_patient_data():
    doctor = input('Doctor Name: ')
    patient = input('Patient Name: ')
    dob = input('Patient DOB: ')
    pharmacy = input('Patient Pharmacy Address: ')
    pharmacy_num = input('Pharmacy Phone Number: ')
    pharmacy_name = input('Pharmacy Name: ')
    email = input('Patient Email: ')
    EHR = input('Facility EHR system: ')
    medication1 = input('Patient medication 1: ')
    medication2 = input('Patient medication 2: ')
    medication1_dosage = input('Medication 1 Dosage: ')
    medication2_dosage = input('Medication 2 Dosage: ')
    medication1_time = input('What time does the patient take medication 1: ')
    medication2_time = input('What time does the patient take medication 2: ')

#Formatted the Label output in input_patient_data, enhanced the data output for clarity
    Label = f"""
    Patient Information:
    --------------------
    Patient Name: {patient}
    DOB: {dob}
    Doctor: {doctor}
    Pharmacy: {pharmacy_name} | Address: {pharmacy} | Phone: {pharmacy_num}
    Facility EHR System: {EHR}

    Medications:
    - {medication1}: {medication1_dosage}, Time: {medication1_time}
    - {medication2}: {medication2_dosage}, Time: {medication2_time}

    Patient Email: {email}
    """
    print(Label)

def input_family_info():
    consent = input("Does the patient consent to providing family information? (yes/no): ").strip().lower()
    if consent == 'yes':
        family = input('Family to include: ')
        family_email = input('Family email: ')
        family_num = input('Family phone number: ')
        print(f"Family Information: {family}, Email: {family_email}, Phone: {family_num}")
    else:
        print("No family information collected.")
#Added main function to integrate patient and family data entry
def main():
    print("Enter Patient and Prescription Information")
    input_patient_data()
    print("\nEnter Family Information")
    input_family_info()
#Added a proper call to main() at the end to run the code.
if __name__ == "__main__":
    main()


