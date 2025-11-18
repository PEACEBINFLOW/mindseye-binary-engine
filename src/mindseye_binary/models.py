from dataclasses import dataclass
from typing import Optional, Dict, List
from datetime import datetime


@dataclass
class BinarySample:
    """Raw binary + metadata for one captured segment."""
    id: Optional[str]
    data: bytes
    source_system: str
    source_path: Optional[str] = None
    captured_at: Optional[datetime] = None
    context: Optional[Dict] = None


@dataclass
class PatternSignature:
    """Compressed description of binary's shape + behavior."""
    hash: str
    length_bits: int
    entropy: float
    compression_ratio: float
    motifs: Dict[str, float]
    created_at: datetime


@dataclass
class TimeLabel:
    """Time labeling for internalized-time navigation."""
    origin_time: datetime
    last_seen_time: datetime
    transformations: int


@dataclass
class ProvenanceRecord:
    """Tracks 'who touched this binary pattern and how'."""
    pattern_hash: str
    events: List[Dict]


@dataclass
class Meter:
    """Defines a navigable range over time-labeled patterns."""
    label: str
    start_time: datetime
    end_time: datetime
    step_mode: str
    params: Dict
