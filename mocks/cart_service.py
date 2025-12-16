from database.database import Database

class CartService:
    def __init__(self, database: Database):
        self.db = database

    def add_to_cart(self, user_id: int, product_id: int, quantity: int) -> dict:
        """
        Sepete ürün ekleme işlemini simüle eder
        """
        if not self.db.is_logged_in(user_id):
            return {
                "success": False, 
                "message": "Kullanici girisi gerekli"
            }
        
        if quantity <= 0:
            return {
                "success": False, 
                "message": "Geçersiz miktar"
            }
        
        product = self.db.get_product_by_id(product_id)

        if not product:
            return {
                "success": False, 
                "message": "Ürün bulunamadi"
            }
        
        if product["stock"] < quantity:
            return {
                "success": False, 
                "message": "Yetersiz stok"
            }
        
        cart_item = {
            "product_id": product_id,
            "name": product["name"],
            "quantity": quantity,
            "price": product["price"]
        }

        self.db.cart.append(cart_item)

        return {
            "success": True, 
            "message": "Ürün sepete eklendi", 
            "cart_item": self.db.cart
        }