from mocks.login_service import LoginService
from database.database import Database

def test_login_with_valid_credentials():
    """
    E-TIC-LOGIN-01
    Başarili Kullanici Girişi (Login)
    """

    db = Database()
    login_service = LoginService(db)
    
    # Geçerli kullanıcı bilgileri
    email = "ahmet.yilmaz@gmail.com"
    password = "Test!123456"

    result = login_service.login(email=email, password=password)

    assert result["success"] is True
    assert result["message"] == "Giriş başarili"
    assert result["redirect"] == "homepage"
    assert result["logged_in"] is True