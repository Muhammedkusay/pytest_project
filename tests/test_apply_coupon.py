from database.database import Database
from mocks.coupon_service import CouponService
from mocks.cart_service import CartService

def test_apply_valid_coupon():
    """
    E-TIC-COUPON-01
    Gecerli Kupon Kodu ile Sepette Indirim Uygulanmasi
    """
    db = Database()
    cart_service = CartService(db)
    coupon_service = CouponService(db)

    user_id = 1     # Ali Veli
    product_id = 1  # Kablosuz Kulaklik

    cart_service.add_to_cart(user_id, product_id, 2)  # 2 adet ekle

    result = coupon_service.apply_coupon(user_id, "INDIRIM10")

    assert result["success"] is True
    assert result["message"] == "Kupon basariyla uygulandi"
    assert result["discount_amount"] == 100.0
    assert result["final_price"] == 900.0