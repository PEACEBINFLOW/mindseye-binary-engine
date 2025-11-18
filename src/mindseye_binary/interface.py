from .models import BinarySample
from .time_labeler import BinaryTimeLabeler
from .pattern_recognizer import BinaryPatternRecognizer
from .meter_navigator import BinaryMeterNavigator
from .provenance import BinaryProvenanceEngine


class BinaryOSInterface:
    """
    High-level entrypoint for Chrome, SQL, MindsEye cloud, and Kaggle tools.
    """

    def __init__(self, pattern_store, provenance_store):
        self.pattern_store = pattern_store
        self.provenance_store = provenance_store

        self.time_labeler = BinaryTimeLabeler(pattern_store)
        self.recognizer = BinaryPatternRecognizer()
        self.navigator = BinaryMeterNavigator(pattern_store)
        self.provenance = BinaryProvenanceEngine(provenance_store)

    def ingest_binary(self, data: bytes, source_system: str, source_path=None, context=None):
        sample = BinarySample(
            id=None,
            data=data,
            source_system=source_system,
            source_path=source_path,
            context=context
        )

        pattern_sig, time_label = self.time_labeler.label(sample)

        self.provenance.record_event(
            pattern_hash=pattern_sig.hash,
            system=source_system,
            action="ingest",
            location=source_path or "",
            meta=context
        )

        return pattern_sig, time_label
