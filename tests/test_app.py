from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"DevOps Task Tracker" in response.data


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/add",
        data={"title": "Test CI/CD"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test CI/CD" in response.data