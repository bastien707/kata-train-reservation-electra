# import json
# import requests


# from flask import Flask, request

# def create_app():

#     app = Flask("train_data")
#     def check_available_seats(train_data):
#         available_seats = (s 
#             for s in train_data["seats"].values() 
#             if s["coach"] == "A" and not s["booking_reference"]) 
#         return available_seats

#     def reserve_seats(available_seats, seat_count):
#         to_reserve = []
#         for i in range(seat_count):
#             to_reserve.append(next(available_seats))
#         return to_reserve

#     def create_reservation(to_reserve, train_id, booking_reference):
#         seat_ids = [s["seat_number"] + s["coach"] for s in to_reserve]
#         return {
#             "train_id": train_id,
#             "booking_reference": booking_reference,
#             "seats": seat_ids
#         }
    

# # infra
#     def send_reservation(reservation):
#         reservation_payload = {
#             "train_id": reservation["train_id"],
#             "seats": reservation["seats"], 
#             "booking_reference": reservation["booking_reference"]
#         }
#         response = requests.post("http://localhost:8081/reserve", json=reservation_payload)
#         return response

#     @app.post("/reserve")
#     def reserve():
#         payload = request.json
#         seat_count = payload["count"]
#         train_id = payload["train_id"]  
#         booking_reference = requests.get("http://localhost:8082/booking_reference").text

#         train_data = requests.get(f"http://localhost:8081/data_for_train/{train_id}").json()
        
#         available_seats = check_available_seats(train_data)  
#         to_reserve = reserve_seats(available_seats, seat_count)
#         reservation = create_reservation(to_reserve, train_id, booking_reference)
        
#         response = send_reservation(reservation)
#         assert response.status_code == 200, response.text
    
#         return json.dumps(reservation)
    
#     return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True, port=8083)
