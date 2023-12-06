import json
import requests

from domaine import check_available_seats


def test_reserve_seats_from_empty_train():
    train_id = "express_2000"


    response = requests.post(f"http://127.0.0.1:8081/reset/{train_id}")
    response.raise_for_status()

    response = requests.post(
        "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
    )

    assert response.status_code == 200, response.text
    reservation = response.json()
    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["1A", "2A", "3A", "4A"]


def test_reserve_four_additional_seats():
    train_id = "express_2000"

    response = requests.post(f"http://127.0.0.1:8081/reset/{train_id}")
    response.raise_for_status()

    response = requests.post(
        "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
    )
    assert response.status_code == 200, response.text
    
    response = requests.post(
        "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 4}
    )
    assert response.status_code == 200, response.text
    reservation = response.json()
    assert reservation["train_id"] == "express_2000"
    assert len(reservation["seats"]) == 4
    assert reservation["seats"] == ["5A", "6A", "7A", "8A"]


# def test_reserve_check_70():
#     train_id = "express_2000"

#     response = requests.post(f"http://127.0.0.1:8081/reset/{train_id}")
#     response.raise_for_status()

#     response = requests.post(
#         "http://127.0.0.1:8083/reserve", json={"train_id": train_id, "count": 10} ## We add 10 persons (62.5%)
#     )
#     assert response.status_code == 200, response.text
#     reservation = response.json()

#     len(reservation["seats"])
    
    
# def test_check_available_seats_2():
#     train_data = {
#         "seats": {
#             "1A": {"coach": "A", "booking_reference": "REF1234"},
#             "2A": {"coach": "A", "booking_reference": None}, 
#             "3A": {"coach": "A", "booking_reference": None}  
#         }
#     }
#     expected = ["2A", "3A"]
    
#     actual = list(check_available_seats(train_data))
    
#     # Assertions
#     assert all(seat in actual for seat in expected)
#     assert len(expected) == len(actual)

    
def test_check_available_seats_3():

    train_data = {
        "seats": {
            "1A": {"coach": "A", "booking_reference": "REF1234"},
            "2A": {"coach": "A", "booking_reference": None}, 
            "3A": {"coach": "A", "booking_reference": None}  
        }
    }

    expected = ["2A", "3A"]

    available_seats = check_available_seats(train_data)
    
    actual = [seat for seat in available_seats]

    assert all(seat in actual for seat in expected) 
    assert len(expected) == len(actual)
    
def test_check_available_seats_4():
    train_data = {
        "seats": {
            "1A": {"coach": "A", "booking_reference": "REF1234"},
            "2A": {"coach": "A", "booking_reference": None}, 
            "3A": {"coach": "A", "booking_reference": None}  
        }
    }
    
    expected = (["coach": "A", "booking_reference": None], ["coach": "A", "booking_reference": None])

    actual = check_available_seats(train_data)
    
    assert expected == actual