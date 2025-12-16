from mocks.coupon_service import CouponService
from mocks.cart_service import CartService  
from database.database import Database

def test_apply_invalid_coupon():
    """
    E-TIC-COUPON-02
    Gecersiz Kupon Kodu Uygulama Denemesi
    """

    db = Database()
    cart_service = CartService(db)
    coupon_service = CouponService(db)

    cart_service.add_to_cart(user_id=1, product_id=1, quantity=1)  # Sepete ürün ekle

    user_id = 1  # Giriş yapmış kullanıcı
    coupon_code = "INDIRIM50"  # Geçersiz kupon kodu

    result = coupon_service.apply_coupon(
        user_id=user_id,
        coupon_code=coupon_code
    )

    # print(result)

    assert result["success"] is False
    assert result["message"] == "Kupon kodu gecersiz"