def test_health_check_api(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
