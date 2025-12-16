class Database:
    def __init__(self):
        # kullanicilar tablosu
        self.users = [
            {
                "id": 1,
                "full_name": "Ali Veli",
                "email": "aliveli@gmail.com",
                "password": "AliVeli123!",
                "logged_in": True
            },
            {
                "id": 2,
                "full_name": "Ahmet Yilmaz",
                "email": "ahmet.yilmaz@gmail.com",
                "password": "Test!123456",
                "logged_in": False
            },
        ]

        # sifre sifirlama icin epostalar tablosu
        self.sent_emails = []

        # ürünler tablosu
        self.products = [
            {
                "id": 1,
                "name": "Kablosuz Kulaklik",
                "price": 500.00,
                "stock": 10
            },
            {
                "id": 2,
                "name": "Bluetooth Hoparlor",
                "price": 899.00,
                "stock": 5
            }
        ]

        # sepet tablosu
        self.cart = []

        # sepet tablosu
        self.coupons = {
            "INDIRIM10": 10,
            "INDIRIM20": 20
        }

    def get_all_users(self):
        return self.users
    
    def is_logged_in(self, user_id: int) -> bool:
        for user in self.users:
            if user["id"] == user_id and user["logged_in"]:
                return True
        return False

    def get_product_by_id(self, product_id: int):
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None
