from mocks.popup_state import PopupState

def test_onboarding_popup_first_visit():
    """
    E-TIC-ONBOARD-01
    İlk ziyarette tanıtım popup gösterilmeli
    """
    popup_state = PopupState()

    # Siteye ilk ziyaret
    popup_visible = popup_state.load_homepage()

    # Bekelen sonuç: Popup görünür olmalı
    assert popup_visible is True

def test_onboarding_popup_not_shown_after_close_and_refresh():
    """
    E-TIC-ONBOARD-01
    Popup kapatıldıktan sonra aynı oturumda tekrar gösterilmemeli
    """

    popup_state = PopupState()

    # ilk girişte popup gösterilir
    popup_state.load_homepage()

    # kullanıcı popup'ı kapatır
    popup_state.close_popup()

    # Sayfa yenilenir
    popup_refresh = popup_state.load_homepage()

    # Beklenen sonuç: Popup tekrar görünür olmamalı
    assert popup_refresh is False
