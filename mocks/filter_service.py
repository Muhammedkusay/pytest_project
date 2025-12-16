from database.database import Database

class FilterService:
    def __init__(self, database: Database):
        self.db = database
        self.products = self.db.products

    def filter_by_price(self, min_price: int, max_price: int):
        """
        Fiyat filtresini simüle eder
        (HATALI IMPLEMENTASYON – üst siniri yanliş kontrol ediyor)
        """

        filtered_products = []

        for product in self.products:
            # Bilinçli olarak hata yapılıyor: max_price kontrol edilmiyor
            if product["price"] >= min_price and product["price"] <= max_price: 
                filtered_products.append(product)

        return filtered_products