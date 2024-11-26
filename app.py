from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from predict_emissions_rate_with_cargo import predict_emissions_rate_with_cargo
from compute_route import compute_route
from get_distance import get_distance

app = Flask(__name__)

@app.route("/predict-emmisions", methods=['GET'])
def predict_emissions():
    vehicle_class = request.args.get('vehicle-class') 
    engine_size = int(request.args.get('engine-size'))
    fuel_type = request.args.get('fuel-type') 
    fuel_consumption = int(request.args.get('fuel-consumption'))
    weight = int(request.args.get('weight'))
    meters = int(request.args.get('meters'))

    predicted_emissions = predict_emissions_rate_with_cargo(vehicle_class, engine_size, fuel_type, fuel_consumption, weight)
    total_emissions = predicted_emissions * (meters / 1000)

    return jsonify({
        "predicted_emissions": predicted_emissions,
        "total_emissions": total_emissions
        })

@app.route("/find-route", methods=['POST'])
def find_route():
    json = request.json

    start = json.get('start')
    end = json.get('end')

    response = compute_route(start, end)
    return jsonify(response)

@app.route("/get-distance", methods=['POST'])
def get_dist():
    json = request.json
    
    start = json.get('start')
    end = json.get('end')
    
    distance = get_distance(start=start, end=end)
    return({"distance": distance})