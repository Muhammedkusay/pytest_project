from database.database import Database
from mocks.cart_service import CartService

def test_add_to_cart_success():
    """
    E-TIC-CART-01
    Urunun Sepete Basarili Sekilde Eklenmesi
    """
    db = Database()
    cart_service = CartService(db)

    product_id = 1  # Kablosuz Kulaklik
    quantity = 1

    result = cart_service.add_to_cart(
        user_id=1,
        product_id=product_id, 
        quantity=quantity
    )


    assert result["success"] is True
    assert result["message"] == "Ürün sepete eklendi"

    cart_item = result["cart_item"][0]

    assert cart_item["product_id"] == product_id
    assert cart_item["quantity"] == quantity
    assert cart_item["price"] > 0