from mocks.search_service import SearchService
from database.database import Database

def test_search_success():
    """
    E-TIC-SEARCH-01
    Urun Arama Basarili Senaryosu
    """

    db = Database()
    service = SearchService(db)

    keyword = "Kablosuz Kulaklik"

    results = service.search_products(keyword)

    # En az bir urun bulunmali
    assert len(results) > 0

    # Bulunan urunlar keyword icermeli
    for product in results:
        assert keyword.lower() in product["name"].lower()
        assert product["stock"] > 0