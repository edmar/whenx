from whenx.services.send_email import send_email


def test_send_email():
    r = send_email(
        "alerts@whenx.ai",
        "edmaroferreira@gmail.com",
        "This this time testing my own email as sender.",
        "A new email alert.",
    )
    assert r is not None
