from datetime import datetime
from .models import BinarySample, PatternSignature, TimeLabel
from . import utils


class BinaryTimeLabeler:
    """
    Assigns time + identity to binary samples and produces PatternSignatures.
    """

    def __init__(self, pattern_store=None):
        self.pattern_store = pattern_store

    def label(self, sample: BinarySample):
        now = datetime.utcnow()

        # 1. Compute base hash
        pattern_hash = utils.compute_hash(sample.data)

        # 2. Pattern stats
        entropy = utils.estimate_entropy(sample.data)
        compression_ratio = utils.estimate_compression_ratio(sample.data)
        motifs = utils.extract_motifs(sample.data)

        existing = None
        if self.pattern_store:
            existing = self.pattern_store.get_by_hash(pattern_hash)

        if existing:
            # Seen before → update time info
            origin = existing["time_label"].origin_time
            transformations = existing["time_label"].transformations + 1
        else:
            # First sighting
            origin = now
            transformations = 0

        time_label = TimeLabel(
            origin_time=origin,
            last_seen_time=now,
            transformations=transformations
        )

        pattern_sig = PatternSignature(
            hash=pattern_hash,
            length_bits=len(sample.data) * 8,
            entropy=entropy,
            compression_ratio=compression_ratio,
            motifs=motifs,
            created_at=now
        )

        if self.pattern_store:
            self.pattern_store.save_pattern(pattern_sig, time_label, sample)

        return pattern_sig, time_label
