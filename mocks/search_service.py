from database.database import Database

class SearchService:
    def __init__(self, database: Database):
        # Urun veritabanini simule etmek 
        self.db = database
        self.products = self.db.products

    def search_products(self, keyword: str) -> list:
        """
        Urun arama fonksiyonunu simule eder
        """
        if not keyword:
            return []
        
        keyword = keyword.lower()

        return [
            product for product in self.products
            if keyword in product["name"].lower()
        ]