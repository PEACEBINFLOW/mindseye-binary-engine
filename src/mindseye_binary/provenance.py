from datetime import datetime
from .models import ProvenanceRecord


class BinaryProvenanceEngine:
    """
    Tracks events in the life of a binary pattern.
    """

    def __init__(self, provenance_store):
        self.store = provenance_store

    def record_event(self, pattern_hash, system, action, location="", meta=None):
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "system": system,
            "action": action,
            "location": location,
            "meta": meta or {}
        }
        self.store.append_event(pattern_hash, event)

    def get_provenance(self, pattern_hash):
        events = self.store.get_events(pattern_hash)
        return ProvenanceRecord(pattern_hash=pattern_hash, events=events)
