def test_meter_navigator_init():
    # Just ensure it initializes
    from src.mindseye_binary.meter_navigator import BinaryMeterNavigator
    nav = BinaryMeterNavigator(pattern_store=None)
    assert nav is not None
