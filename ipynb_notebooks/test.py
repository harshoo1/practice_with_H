import sys
sys.path.append('/home/theghost001/Pictures/practice_with_H/.py')
from logger import get_logger, log_function

logger = get_logger(name = 'test_logging', log_file = 'test.log')


@log_function(logger)
def test_add_func(a,b):
    return a+b

@log_function(logger)
def test_sub_func(a,b):
    return a-b

@log_function(logger)
def test_mul_func(a,b):
    return a*b  

@log_function(logger)
def test_div_func(a,b):
    return a/b  


result1 = test_add_func(2,3)
result2 = test_sub_func(2,3)
result3 = test_mul_func(2,3)
result4 = test_div_func(2,3)
