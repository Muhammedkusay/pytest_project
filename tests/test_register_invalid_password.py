from mocks.register_service import RegisterService
from database.database import Database

def test_register_invalid_password():
    """
    E-TIC-REGISTER-03
    Zayif Şifre ile Kayit Olma Denemesi
    """

    db = Database()
    register_service = RegisterService(db)

    full_name = "Kader Yildiz"
    email = "kader@gmail.com"
    password = "12345"  # Zayif sifre
    kvkk_accepted = True

    result = register_service.register_user(
        full_name=full_name,    
        email=email,
        password=password,
        kvkk_accepted=kvkk_accepted
    )  

    # print(result)

    assert result["success"] is False
    assert result["message"] == "Sifre gereksinimlerini karsilamiyor"
