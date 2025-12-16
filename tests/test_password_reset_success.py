from mocks.password_reset_service import PasswordResetService
from database.database import Database

def test_password_reset_success():
    """
    E-TIC-PASSRESET-01
    “Şifremi Unuttum” ile Parola Sifirlama Bağlantisi Gönderimi
    """
    db = Database()
    service = PasswordResetService(db)

    email = "aliveli@gmail.com"

    result = service.send_reset_link(email=email)

    # Bekelenen Sonuçlar
    assert result["success"] is True
    assert result["message"] == "Parola sifirlama bağlantiniz e-posta adresinize gönderildi"

    # Mail gercekte gonderildi mi kontrolu
    assert db.sent_emails[0]["to"] == email
