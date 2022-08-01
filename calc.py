def monthly_compounding(initial, monthly, years, annual_rate):
    if abs(annual_rate) > 1:
        return "Error: annual_rate is a percentage and so must be between 0 and 1"
    
    final_sum = initial
    monthly_rate = pow(1 + annual_rate, 1/12) - 1
    for _ in range(0, years*12):
        final_sum = final_sum*(1 + monthly_rate) + monthly

    return round(final_sum, 2)