import re
from database.database import Database

class RegisterService:
    def __init__(self, database: Database):
        # daha once kayitli email adreslerini tutan bir set
        self.db = database

    def is_valid_password(self, password: str) -> bool:
        """
        Sifre en az 8 karakter, harf, rakam ve ozel karakter icermelidir.
        """
        if len(password) < 8:
            return False
        if not re.search(r"[A-Za-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True
    
    def register_user(
        self,
        full_name: str,
        email: str,
        password: str,
        kvkk_accepted: bool
    ) -> dict:
        """
        Kullanici kayit islemini simule eder.
        """
        registered_emails = {user["email"] for user in self.db.get_all_users()}
        if not full_name:
            return {"success": False, "message": "Ad Soyad zorunludur"}
        if not email:
            return {"success": False, "message": "E-posta alani bos birakilamaz"}
        if email in registered_emails:
            return {"success": False, "message": "E-posta baska bir kullaniciya aittir"}
        if not self.is_valid_password(password):
            return {"success": False, "message": "Sifre gereksinimlerini karsilamiyor"}
        if not kvkk_accepted:
            return {"success": False, "message": "KVKK kabul edilmelidir"}
        
        # Kayit islemi basarili, email adresini kaydet
        self.db.users.append({
            "full_name": full_name,
            "email": email,
            "password": password
        })
        return {
            "success": True,
            "message": "Kayit islemi basarili",
            "redirect": "homepage",
            "logged_in": True,
        }