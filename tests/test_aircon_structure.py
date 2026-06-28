from src.aircon import aircon_settings


def test_aircon_settings_is_stable_across_calls():
    assert aircon_settings() == aircon_settings()


def test_aircon_settings_contains_mode_temp_fan_labels():
    s = aircon_settings()
    assert "Mode:" in s
    assert "Temp:" in s
    assert "Fan:" in s