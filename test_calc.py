from calc import monthly_compounding


def test_zeros():
    # Arrange
    initial = 0
    monthly = 0
    years = 0
    annual_rate = 0
    expected_sum = 0

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_only_one_year_zero_apr():
    # Arrange
    initial = 5000
    monthly = 0
    years = 1
    annual_rate = 0
    expected_sum = 5000

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_monthly_one_year_zero_apr():
    # Arrange
    initial = 5000
    monthly = 500
    years = 1
    annual_rate = 0
    expected_sum = 11000

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_monthly_multiple_years_zero_apr():
    # Arrange
    initial = 5000
    monthly = 500
    years = 5
    annual_rate = 0
    expected_sum = 35000

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_monthly_multiple_years():
    # Arrange
    initial = 5000
    monthly = 500
    years = 5
    annual_rate = 0.05
    expected_sum = 40288.28

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_monthly_one_year():
    # Arrange
    initial = 5000
    monthly = 500
    years = 1
    annual_rate = 0.05
    expected_sum = 11386.29

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_only_one_year():
    # Arrange
    initial = 5000
    monthly = 0
    years = 1
    annual_rate = 0.05
    expected_sum = 5250

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_initial_monthly():
    # Arrange
    initial = 5000
    monthly = 500
    years = 0
    annual_rate = 0.05
    expected_sum = 5000

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_bad_apr():
    # Arrange
    initial = 0
    monthly = 0
    years = 0
    annual_rate = 3
    expected_sum = "Error: annual_rate is a percentage and so must be between 0 and 1"

    # Act
    final_sum = monthly_compounding(initial, monthly, years, annual_rate)

    # Assert
    assert final_sum == expected_sum


def test_bad_years():
    pass