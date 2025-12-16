from database.database import Database

class PasswordResetService:
    def __init__(self, database: Database):
        self.db = database
        # Sistemde kayitli e-postalar
        self.registered_emails = [user["email"] for user in self.db.get_all_users()]

        # Gonderilen mailleri simule etmek icin
        self.sent_emails = []

    def send_reset_link(self, email: str) -> dict:
        """
        Sifremi unttum fonksiyonu simule eder
        """
        if not email:
            return {
                "success": False,
                "message": "E-posta alani zorunludur."
            }
        
        if email not in self.registered_emails:
            return {
                "success": False,
                "message": "Bu e-posta adresi ile kayitli kullanici bulunamadi"
            }
        
        # Mail gonderme islemi simule etme
        reset_link = f"https://ecommerce.test/reset-password?email={email}"
        self.db.sent_emails.append({
            "to": email,
            "link": reset_link    
        })

        return {
            "success": True,
            "message": "Parola sifirlama bağlantiniz e-posta adresinize gönderildi"
        }