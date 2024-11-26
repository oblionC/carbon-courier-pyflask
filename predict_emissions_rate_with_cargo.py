import joblib
import pandas as pd
# from current_expected_emissions_rate import current_expected_emmissions_rate

from constants import *

def predict_emissions_rate_with_cargo(vehicle_class, engine_size, fuel_type, fuel_consumption, weight):
    """Predicts CO2 emissions for cargo vehicles with adjustable weight impact.
    """

    model = joblib.load(MODEL_PKL_NAME)

    # Validate inputs
    if vehicle_class not in ['Cargo Van', 'Pickup Truck', 'SUV - STANDARD']:
        raise ValueError("Invalid vehicle class. Only 'Cargo Van', 'Pickup Truck', and 'SUV - STANDARD' are supported for this function.")
    if not isinstance(weight, (int, float)) or weight <= 0 :
        raise ValueError("Invalid weight. Weight should be a positive number.")


    # Create a DataFrame for prediction
    input_data = pd.DataFrame({
        'Vehicle Class': [vehicle_class],
        'Engine Size(L)': [engine_size],
        'Fuel Type': [fuel_type],
        'Fuel Consumption Comb (L/100 km)': [fuel_consumption]
    })

    # Predict emissions
    emissions = model.predict(input_data)[0]

    # Adjust emissions based on weight
    emissions += weight * EMISSION_KG_PER_KM_PER_KG_WEIGHT 

    return emissions


# vehicle_class = 'Cargo Van'
# engine_size = 4
# fuel_type = 'Z' #fuel type
# fuel_consumption = 12
# weight = 2000

# predicted_emissions = predict_emissions_rate_with_cargo(vehicle_class, engine_size, fuel_type, fuel_consumption, weight)
# print(predicted_emissions, current_expected_emmissions_rate(0, predicted_emissions))
