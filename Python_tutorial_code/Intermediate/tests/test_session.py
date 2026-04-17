''' Below scripts show some basic functions and ways to test them

#pytest works by looking for a 'tests' folder and files including that uses functions with a prefix of 'test'
import pytest

import pandas as pd

# function returns sum of x + y
def sum_xy(x, y):
    return x + y

# function to test function sum_xy
def test_sum_xy():
    result = sum_xy(x=1, y=1)
    assert result == 2

# function returns sum of x * y
def multiply_xy(x, y):
    return x * y

# function to test function sum_xy
def test_multiply_xy():
    assert multiply_xy(x=2, y=2) == 4

def summult(x,y):
    return sum_xy(x,y), multiply_xy(x,y)

def test_summult():
    sum, prod = summult(4,9)

    assert sum == 13
    assert prod == 36


def df_slicer(df, age):
    age_or_over = df[df['Age']] >= age
    return age_or_over

'''

import pytest
import pandas as pd

# run these in the cmd line using python -m pytest <filepath>


######### Function and test 1
def sum_xy(x, y):
    return x + y


def test_sum_xy():
    assert sum_xy(1, 1) == 2


######## Function and test 2
def prod_xy(x, y):
    return x * y


def sumprod(x, y):
    return sum_xy(x, y), prod_xy(x, y)


def test_sumprod():
    sum, prod = sumprod(1, 1)

    assert sum == 2
    assert prod == 1


########## Function and test 3
def df_slicer(df):
    over_5 = df[df["Age"] >= 5]
    return over_5


# There are more advanced ways to do this, for instance if we are running tests on
# the same dataframe over and over we can set it as a fixture but that's a bit advanced for here
def test_df_slicer():
    test_df = pd.DataFrame(
        [
            {"ChildId": "child1", "Age": 6},
            {"ChildId": "child3", "Age": 10},
            {"ChildId": "child2", "Age": 4},
            {"ChildId": "child4", "Age": 1},
        ]
    )
    sliced_df = df_slicer(test_df)

    expected_df = pd.DataFrame(
        [{"ChildId": "child1", "Age": 6},
         {"ChildId": "child3", "Age": 10},
        ]
    )

    pd.testing.assert_frame_equal(sliced_df, expected_df, check_names=False)