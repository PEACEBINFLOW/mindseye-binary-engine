from typing import List, Dict
from .models import PatternSignature
import numpy as np


class BinaryPatternRecognizer:
    """
    Compares pattern signatures and clusters them.
    """

    def similarity(self, a: PatternSignature, b: PatternSignature) -> float:
        """
        Returns similarity score (0 - 1).
        """
        entropy_dist = abs(a.entropy - b.entropy)
        comp_dist = abs(a.compression_ratio - b.compression_ratio)

        motif_overlap = len(
            set(a.motifs.keys()) & set(b.motifs.keys())
        ) / max(len(a.motifs.keys()), 1)

        score = 1 / (1 + entropy_dist + comp_dist) * (0.5 + 0.5 * motif_overlap)
        return min(1.0, max(0.0, score))

    def cluster(self, patterns: List[PatternSignature], k=5):
        """
        Simple k-means clustering on entropy and compression ratio.
        """

        if len(patterns) < k:
            return {i: [p] for i, p in enumerate(patterns)}

        X = np.array([
            [p.entropy, p.compression_ratio] for p in patterns
        ])

        # Basic random-init k-means
        centroids = X[np.random.choice(len(X), k, replace=False)]
        for _ in range(10):
            labels = np.argmin(((X[:, None] - centroids[None, :]) ** 2).sum(-1), axis=1)
            for i in range(k):
                pts = X[labels == i]
                if len(pts):
                    centroids[i] = pts.mean(0)

        clusters = {i: [] for i in range(k)}
        for idx, p in enumerate(patterns):
            clusters[labels[idx]].append(p)

        return clusters
