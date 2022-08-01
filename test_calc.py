# -*- coding: utf-8 -*-
""" 

Created on Fri Jul 29 18:57 2022

@author: Lenka Wolfova
"""


def test_zeros():
    # Arrange
    initial_investment = 0
    interest_rate = 0
    monthly_deposit = 0
    years = 0
    expected_output = 0

    # Act
    actual_output = monthly_compounding()

    #Assert
    assert actual_output == expected_output

def test_one_year_zero_interest ():
    pass