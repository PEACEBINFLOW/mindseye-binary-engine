# MindsEye Binary Pattern Engine

> **A binary-level cognition layer for MindsEye.**  
> Decode, label, map, and traverse binary as time-patterns.

Most systems treat binary as a dumb substrate.

This repo treats binary as a **living pattern space**.

Instead of just:
- `0` and `1`,
- bytes and files,

we look at:
- pattern shape,
- math behavior,
- time of appearance,
- and the identity of the systems that touched it.

This is the foundation for **time-labeled binary pattern spaces** – a new way for agents and developers to understand computation at the substrate level.

---

## Core Ideas

Every binary sequence carries:

- **Pattern** – the shape of bits.
- **Math** – transformation rules encoded in its structure.
- **Time** – when and how it was produced.
- **Identity** – which app, layer, or system influenced it.

The Binary Pattern Engine exposes all four.

It lets you:

- ingest binary from any source,
- assign time-aware labels,
- generate pattern signatures,
- traverse patterns over time (Meters),
- and track provenance across systems.

---

## Components

- **Binary Time-Labeler**  
  Attaches timestamps, context, transformation counts, and pattern classes to raw binary.

- **Binary Pattern Recognizer**  
  Computes pattern signatures (hash, entropy, compression behavior, motifs) and compares / clusters them.

- **Binary Meter Navigator**  
  Defines navigable ranges over time-labeled patterns and lets you traverse them by time, entropy, motif, or transformation count.

- **Binary Provenance Engine**  
  Tracks where a pattern has appeared, which systems touched it, and how it evolved.

- **Binary OS Interface**  
  High-level API that Chrome extensions, SQL services, and MindsEye orchestrators can call.

---

## Example Usage

```python
from mindseye_binary.interface import BinaryOSInterface
from my_stores import pattern_store, provenance_store

binary_os = BinaryOSInterface(pattern_store, provenance_store)

with open("example.bin", "rb") as f:
  data = f.read()

pattern_sig, time_label = binary_os.ingest_binary(
  data=data,
  source_system="local_file",
  source_path="example.bin",
  context={"workspace": "ml_research"}
)

print(pattern_sig.hash, time_label.origin_time)
