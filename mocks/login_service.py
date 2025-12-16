from database.database import Database

class LoginService:
    def __init__(self, database: Database):
        self.db = database

    def login(self, email, password):
        """
        Kullanici giris islemini simule eder.
        """
        emails = {user["email"]: user for user in self.db.get_all_users()}
        if email not in emails:
            return {
                "success": False,
                "message": "Kullanici bulunamadi."
            }
        user = emails[email]
        if user["password"] != password:
            return {
                "success": False,
                "message": "Hatali sifre."
            }
        
        return {
            "success": True,
            "message": "Giriş başarili",
            "redirect": "homepage",
            "logged_in": True,
        }