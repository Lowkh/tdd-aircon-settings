from src.aircon import aircon_settings


def test_default_temp_is_in_comfort_range():
    s = aircon_settings()
    temp_part = s.split("Temp:").split(",").strip()[5]
    temp_value = int(temp_part.replace("°C", ""))
    assert 22 <= temp_value <= 26