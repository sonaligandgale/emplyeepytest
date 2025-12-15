from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Alice\n"
        "Employee ID: E101\n"
        "Employee Department: It\n"
        "Employee Salary: 55000\n"
    )

    assert employee_details("Alice", "E101", "It", 55000) == expected_output
