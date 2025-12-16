from mocks.search_service import SearchService
from database.database import Database

def test_search_no_result():
    """
    E-TIC-SEARCH-02
    Arama Sonucu Bulunmayan Kelime ile Ürün Arama
    """
    db = Database()
    search_service = SearchService(db)

    keyword = "Laptop"  # Veritabanında olmayan bir kelime

    result = search_service.search_products(keyword)

    assert result == [] 