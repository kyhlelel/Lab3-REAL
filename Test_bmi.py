import Lab2.bmi as bmi

print("Test BMI")


def test_bmi_normal_weight():
    assert bmi.calculate_bmi(1.73, 74) == 0

def test_bmi_under_weight():
    assert bmi .calculate_bmi(1.73, 20) == -1

def test_bmi_overweight():
    assert bmi.calculate_bmi(1.73, 100) == 1