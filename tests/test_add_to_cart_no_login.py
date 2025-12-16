from mocks.cart_service import CartService
from database.database import Database  

def test_add_to_cart_no_login():
    """
    E-TIC-CART-03
    Kullanici giriş yapmadan sepete ürün eklemesi
    """
    db = Database()
    cart_service = CartService(db)

    user_id = 2  # Ahmet Yilmaz, giris yapmamis kullanici
    product_id = 1  # Kablosuz Kulaklik
    quantity = 1

    result = cart_service.add_to_cart(user_id, product_id, quantity)
    
    # print(f"Result: {result}")

    assert result["success"] is False
    assert result["message"] == "Kullanici girisi gerekli"
    assert len(db.cart) == 0