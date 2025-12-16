from mocks.cart_service import CartService
from database.database import Database

def test_add_to_cart_stock_fail():
    """
    E-TIC-CART-02
    Stok Yetersizligi Durumunda Urunun Sepete Eklenememesi
    """
    db = Database()
    cart_service = CartService(db)

    user_id = 1  # Ali Veli, giris yapmis kullanici
    product_id = 2  # Bluetooth Hoparlor
    quantity = 10  # Stokta sadece 5 adet var

    result = cart_service.add_to_cart(user_id, product_id, quantity)
    
    assert result["success"] is False
    assert result["message"] == "Yetersiz stok"
    assert len(db.cart) == 0