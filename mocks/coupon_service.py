from database.database import Database

class CouponService:
    def __init__(self, db: Database):
        self.db = db

    def apply_coupon(self, user_id: int, coupon_code: str) -> float:
        """
        Kuponu sepete uygular
        """
        if not self.db.is_logged_in(user_id):
            return {
                "success": False,
                "message": "Kullanici girisi gerekli"
            }
        
        if not self.db.cart:
            return {
                "success": False,
                "message": "Sepet bos"
            }

        if coupon_code not in self.db.coupons:
            return {
                "success": False,
                "message": "Kupon kodu gecersiz"
            }
        
        discount = self.db.coupons[coupon_code]
        
        total_price = sum(
            item["price"] * item["quantity"] for item in self.db.cart
        )

        discount_amount = total_price * discount / 100
        final_price = total_price - discount_amount

        return {
            "success": True,
            "message": "Kupon basariyla uygulandi",
            "discount_amount": discount_amount,
            "final_price": final_price
        }