import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def read_employees_from_json(file_path):
    employees_list = []

    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for emp_data in data['employees']:
            employee = Employee(emp_data['Name'],
                                emp_data['DOB'],
                                emp_data['Height'],
                                emp_data['City'],
                                emp_data['State'])
            employees_list.append(employee)

    return employees_list

if __name__ == "__main__":
    employees_data_file = "employee.json"
    employees_list = read_employees_from_json(employees_data_file)

   
    for employee in employees_list:
        print(f"Name: {employee.name}")
        print(f"DOB: {employee.dob}")
        print(f"Height: {employee.height}")
        print(f"City: {employee.city}")
        print(f"State: {employee.state}")
        print()

indian_states_capitals = {
    "Andhra Pradesh": "Amaravati",
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar",
    "Rajasthan": "Jaipur"
}
with open("indian_states_capitals.json", "w") as json_file:
    json.dump(indian_states_capitals, json_file)
