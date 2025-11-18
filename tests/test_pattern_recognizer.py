from src.mindseye_binary.pattern_recognizer import BinaryPatternRecognizer
from src.mindseye_binary.models import PatternSignature
from datetime import datetime


def test_similarity():
    now = datetime.utcnow()
    a = PatternSignature("a", 80, 1.2, 0.5, {"aa": 1.0}, now)
    b = PatternSignature("b", 80, 1.2, 0.5, {"aa": 1.0}, now)

    rec = BinaryPatternRecognizer()
    score = rec.similarity(a, b)

    assert 0 <= score <= 1
