class PopupState:
    def __init__(self):
        # tarayıcı oturumunda popup gösterilip gösterilmediğini 
        self.popuop_shown = False

    def load_homepage(self):
        # Ana sayfa yüklendiğinde popup gösterilir
        if not self.popuop_shown:
            return True
        return False
    
    def close_popup(self):
        # kullanıcı popup kapattığında durumu günceller
        self.popuop_shown = True