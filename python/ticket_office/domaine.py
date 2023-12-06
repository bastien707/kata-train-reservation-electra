def check_available_seats(train_data):
    available_seats = (s 
        for s in train_data["seats"].values() 
        if s["coach"] == "A" and not s["booking_reference"]) 
    return available_seats

def reserve_seats(available_seats, seat_count):
    to_reserve = []
    for i in range(seat_count):
        to_reserve.append(next(available_seats))
    return to_reserve

def create_reservation(to_reserve, train_id, booking_reference):
    seat_ids = [s["seat_number"] + s["coach"] for s in to_reserve]
    return {
        "train_id": train_id,
        "booking_reference": booking_reference,
        "seats": seat_ids
    }


