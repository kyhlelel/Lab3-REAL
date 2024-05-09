import employee_info as EI

def test_get_employees_age_range():
    u_age = 31
    L_age = 22
    
    emp = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}    
    ]
    
    assert EI.get_employees_by_age_range(L_age, u_age) == emp
    
def test_calculate_average_salary():
    assert EI.calculate_average_salary() == 60166.67