from mocks.login_service import LoginService
from database.database import Database

def test_login_with_wrong_password():
    """
    E-TIC-LOGIN-02
    Hatali Şifre ile Giriş Denemesi
    """

    db = Database()
    login_service = LoginService(db)
    
    # Yanlis sifre ile giris yapmaya calis
    result = login_service.login(
        email="ahmet.yilmaz@gmail.com",
        password="WrongPassword!123"
    )

    # Girişin başarısız olduğunu doğrula
    assert result["success"] is False
    assert result["message"] == "Hatali sifre."