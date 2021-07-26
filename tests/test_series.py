from math_series import __version__

from math_series.series import fibonacci,lucas,sum_series



def test_fibonacci_num():
    expected = 55 
    
    actual = fibonacci(10)

    assert  expected == actual


def test_lucas_num():
    expected = 76 
    
    actual = lucas(9)

    assert  expected == actual    



def test_sum_series_first():
    expected=5
    actual=sum_series(2,3,2)
    assert expected==actual


def test_sum_series_second():
    expected=66
    actual=sum_series(7, 5, 2)
    assert expected==actual
