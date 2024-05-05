import Lab2.Lab2 as L2

print("Test Lab 2")

def test_find_min_max():
    numlist = [1, 2, 3, 4, 5]
    assert L2.find_min_max(numlist) == (1,5)
    
def test_calc_average():
    numlist = [1, 3]
    assert L2.calc_average(numlist) == 2
    
def test_calc_median_temp():
    numlist = [1,2,3,4,5]
    assert L2.calc_median_temp(numlist) == 3
       
