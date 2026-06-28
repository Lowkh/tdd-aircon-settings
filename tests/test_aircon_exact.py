from src.aircon import aircon_settings


def test_aircon_returns_default_configuration():
    assert aircon_settings() == "Mode: COOL, Temp: 24°C, Fan: AUTO"

def test_aircon_settings_type_is_str():
    result = aircon_settings()
    assert isinstance(result, str)