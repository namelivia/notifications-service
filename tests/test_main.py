from .test_base import client


class TestApp:
    def test_send_notification(self, client):
        response = client.post(
            "/notification",
            json={
                "message": "Test message",
            },
        )
        assert response.status_code == 200
