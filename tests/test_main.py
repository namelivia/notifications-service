from .test_base import client
from mock import patch


class TestApp:
    @patch("app.services.telegram.Telegram.send")
    def test_send_notification(self, m_send, client):
        response = client.post(
            "/notification",
            json={
                "message": "Test message",
            },
        )
        assert response.status_code == 200
        m_send.assert_called_with("Test message")
