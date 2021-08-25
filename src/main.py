import requests

def get_plate_details(plate):
    params = {
        "vrm": plate,
        "country": "UK",
        "lookupType": "PayCc",
        "jsonQmlOptions": "{}",
    }

    http_response = requests.get("https://tfl.gov.uk/Ruc/VehicleLookup/FindVehicleAjax", params = params, headers = {
        "X-Requested-With": "XMLHttpRequest",
    })

    if http_response.status_code == 200:
        vehicle_response_json = http_response.json()
        vehicle_description = vehicle_response_json.get("foundBasicVehicleTile").get("details")

        return vehicle_description

if __name__ == "__main__":
    while 1:
        vehicle_description = get_plate_details(input("Plate: "))
        print(vehicle_description)