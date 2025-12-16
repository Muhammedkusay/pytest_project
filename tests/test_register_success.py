from mocks.register_service import RegisterService
from database.database import Database

def test_register_successful_scenario():
    """
    E-TIC-REGISTER-01
    Yeni Kullanici Kaydi – Başarili Senaryo
    """

    db = Database()
    register_service = RegisterService(db)

    full_name = "Kader Yildiz"
    email = "kader.yildiz@gmail.com"
    password = "Kader!123456"
    kvkk_accepted = True    

    result = register_service.register_user(
        full_name=full_name,
        email=email,
        password=password,
        kvkk_accepted=kvkk_accepted
    )

    assert result["success"] is True
    assert result["message"] == "Kayit islemi basarili"
    assert result["redirect"] == "homepage"
    assert result["logged_in"] is True