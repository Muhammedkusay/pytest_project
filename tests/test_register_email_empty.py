from mocks.register_service import RegisterService
from database.database import Database

def test_register_with_empty_email():
    """
    E-TIC-REGISTER-02
    E-posta Alani Boşken Kayit Olma Denemesi
    """

    db = Database()
    register_service = RegisterService(db)

    full_name = "Mehmet Demir"
    email = ""
    password = "Test!123456"
    kvkk_accepted = True

    result = register_service.register_user(
        full_name=full_name,
        email=email,
        password=password,
        kvkk_accepted=kvkk_accepted
    )

    assert result["success"] is False
    assert result["message"] == "E-posta alani bos birakilamaz"
