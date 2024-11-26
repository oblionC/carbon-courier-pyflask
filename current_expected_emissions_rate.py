def current_expected_emmissions_rate(speed, predicted_emissions):
    if speed < 3: 
        return predicted_emissions
    
    optimalSpeed = 70
    a = 1200 # low speed inefficiency factor
    b = 0.0015 # air resistance factor
    c = 100 # base emissions
    
    optimalEmissions = (a/optimalSpeed) + (b * optimalSpeed * optimalSpeed) + c
    emissions = (a/speed) + (b * speed * speed) + c
    emission_multiplication_factor = emissions / optimalEmissions

    return predicted_emissions * emission_multiplication_factor
