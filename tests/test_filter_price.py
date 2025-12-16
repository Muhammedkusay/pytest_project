from mocks.filter_service import FilterService
from database.database import Database

def test_filter_by_price():
    """
    E-TIC-FILTER-01
    Fiyat Filtresi ile Ürün Listeleme
    """

    db = Database()
    filter_service = FilterService(db)

    min_price = 300
    max_price = 500

    results = filter_service.filter_by_price(min_price, max_price)

    # en az bir ürün döndüğünü doğrula
    assert len(results) > 0

    # Tüm ürünler 300–500 aralığında olmalı
    for product in results:
        assert min_price <= product["price"] and product["price"] <= max_price