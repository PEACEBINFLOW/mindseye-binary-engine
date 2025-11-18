from src.mindseye_binary.time_labeler import BinaryTimeLabeler
from src.mindseye_binary.models import BinarySample


def test_time_labeler():
    tl = BinaryTimeLabeler(pattern_store=None)
    sample = BinarySample(
        id=None,
        data=b"hello world",
        source_system="test"
    )
    sig, tlbl = tl.label(sample)

    assert sig.hash is not None
    assert tlbl.origin_time is not None
