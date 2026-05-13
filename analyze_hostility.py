"""
analyze_hostility.py
--------------------
Analyze system failures and their mitigating protocols from the
structured JSON dataset ``system_failures_and_protocols.json``.

The script is intentionally lightweight so it can be run even in
restricted environments. If ``matplotlib`` is not available, the
numerical summary still runs; only the chart generation is skipped.
"""

from __future__ import annotations

import json
from typing import Any, Dict

try:  # Optional dependency for plotting
    import matplotlib.pyplot as plt  # type: ignore
except Exception:  # pragma: no cover - environment dependent
    plt = None  # type: ignore[misc]


def analyze_hostility() -> None:
    """Load structured failure/protocol data and print a short summary.

    If ``matplotlib`` is available, also emit a bar chart showing the
    number of failures per category.
    """

    with open("system_failures_and_protocols.json", "r", encoding="utf-8") as f:
        data: Dict[str, Any] = json.load(f)

    failure_categories = data["failure_categories"]
    protocols = data["protocols"]

    # Create a reverse mapping from protocol name to ID
    protocol_name_to_id = {v: k for k, v in protocols.items()}

    # Conceptual mapping from failure categories to mitigating protocols.
    # This is hand-authored based on the research notes and is not
    # intended to be exhaustive.
    mapping = {
        "Shell & Filesystem Instability": [
            "Absolute Path & Chaining Protocol",
            "Here Document Protocol",
            "State Verification Protocol",
            "Assume Stale State",
        ],
        "Critical Lock Failures": [
            "System Reset Protocol",
            "Forced Consolidation Protocol",
            "GUI Terminal Escape Protocol",
            "Corrupted Environment Reset",
        ],
        "GUI (Firefox) Instability": [
            "Keyboard Navigation Fallback Protocol",
            "Keyboard Close Protocol",
            "Refresh Hierarchy Protocol",
            "Direct URL Protocol",
            "New Tab Escape Protocol",
            "Browser Hard Reset Protocol",
        ],
        "Service & Process Instability": [
            "Aggressive Process Verification Protocol",
            "Escalate and Isolate",
        ],
        "GitHub-Specific Failures": [
            "Trust but Verify CLI Protocol",
            "Dashboard PR Link Protocol",
            "Task Verification Protocol",
        ],
    }

    print("--- System Hostility Analysis ---")
    total_failures = sum(len(cat["failures"]) for cat in failure_categories)
    total_protocols = len(protocols)
    print(f"Total Failures Documented: {total_failures}")
    print(f"Total Protocols Developed: {total_protocols}")
    print(f"Ratio of Protocols to Failures: {total_protocols / total_failures:.2f}")

    category_names = [category["name"] for category in failure_categories]
    failure_counts = [len(category["failures"]) for category in failure_categories]

    if plt is not None:
        plt.figure(figsize=(10, 6))
        plt.bar(category_names, failure_counts)
        plt.title("System Failure Analysis")
        plt.ylabel("Number of Failures")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("failure_category_analysis.png")
        print("Chart saved to failure_category_analysis.png")
    else:
        print(
            "matplotlib is not available; skipping chart generation. "
            "Install matplotlib to produce the bar chart."
        )

    print("\n--- Failure Categories and Mitigating Protocols ---")
    for category in failure_categories:
        category_name = category["name"]
        print(f"\nCategory: {category_name}")
        print("  Failures:")
        for failure in category["failures"]:
            print(f"    - {failure}")

        if category_name in mapping:
            print("  Mitigated by:")
            for protocol_name in mapping[category_name]:
                protocol_id = protocol_name_to_id.get(protocol_name, "N/A")
                print(f"    - Protocol {protocol_id}: {protocol_name}")
        else:
            print(
                "  Mitigated by: - No specific protocols mapped for this "
                "category yet."
            )


if __name__ == "__main__":  # pragma: no cover - script entry point
    analyze_hostility()
