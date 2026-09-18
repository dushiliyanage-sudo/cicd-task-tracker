from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Wanderly" in response.data
    assert b"Go somewhere" in response.data


def test_destinations_page():
    client = app.test_client()
    response = client.get("/destinations")
    assert response.status_code == 200
    assert b"Santorini" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_add_trip():
    client = app.test_client()
    response = client.post(
        "/plan",
        data={
            "destination": "Kandy, Sri Lanka",
            "date": "November 10, 2026",
            "note": "Temple and lake day",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Kandy, Sri Lanka" in response.data


def test_delete_trip():
    client = app.test_client()
    response = client.post("/plan/delete/1", follow_redirects=True)
    assert response.status_code == 200
    assert b"Trip removed from your travel board." in response.data
