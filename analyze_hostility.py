<<<<<<< HEAD
"""
analyze_hostility.py
--------------------
Reads the JSON dataset describing system failures and prints the frequency of
each failure category. The script expects the JSON file to contain an array of
objects with a `failure_category` field, and uses pandas for the aggregation.
"""

from pathlib import Path
import sys

import pandas as pd


def main(json_filename: str = "system_failures_and_protocols.json") -> None:
    """Load the dataset and print simple frequency statistics."""
    json_path = Path(json_filename)

    # Validate that the expected JSON file exists before attempting to load it.
    if not json_path.exists():
        print(f"JSON file not found: {json_path.resolve()}", file=sys.stderr)
        sys.exit(1)

    try:
        # pandas handles JSON-to-DataFrame conversion, making aggregation easier.
        df = pd.read_json(json_path)
    except ValueError as exc:
        print(f"Failed to parse JSON: {exc}", file=sys.stderr)
        sys.exit(1)

    if "failure_category" not in df.columns:
        print("The dataset does not include a 'failure_category' column.", file=sys.stderr)
        sys.exit(1)

    # Count how often each failure category occurs, including missing categories.
    category_counts = df["failure_category"].value_counts(dropna=False).sort_values(ascending=False)

    print("Failure Category Frequency Analysis")
    print("-----------------------------------")
    for category, count in category_counts.items():
        label = "Unspecified" if pd.isna(category) else category
        print(f"{label}: {count}")


if __name__ == "__main__":
    main()
=======
import json

def analyze_hostility():
    with open('system_failures_and_protocols.json', 'r') as f:
        data = json.load(f)

    failure_categories = data['failure_categories']
    protocols = data['protocols']

    # Create a reverse mapping from protocol name to ID
    protocol_name_to_id = {v: k for k, v in protocols.items()}

    # This is a conceptual mapping and will be expanded with more sophisticated analysis
    # For now, we'll manually define some relationships
    mapping = {
        "Shell & Filesystem Instability": ["Absolute Path & Chaining Protocol", "Here Document Protocol", "State Verification Protocol"],
        "Critical Lock Failures": ["System Reset Protocol", "Forced Consolidation Protocol", "GUI Terminal Escape Protocol"],
        "GUI (Firefox) Instability": ["Keyboard Navigation Fallback Protocol", "Keyboard Close Protocol", "Refresh Hierarchy Protocol", "Direct URL Protocol", "New Tab Escape Protocol", "Browser Hard Reset Protocol"],
        "Service & Process Instability": ["Aggressive Process Verification Protocol"],
        "GitHub-Specific Failures": ["Trust but Verify CLI Protocol", "Dashboard PR Link Protocol"]
    }

    print("--- System Hostility Analysis ---")
    total_failures = sum(len(cat['failures']) for cat in failure_categories)
    total_protocols = len(protocols)
    print(f"Total Failures Documented: {total_failures}")
    print(f"Total Protocols Developed: {total_protocols}")
    print(f"Ratio of Protocols to Failures: {total_protocols / total_failures:.2f}")


    print("\n--- Failure Categories and Mitigating Protocols ---")
    for category in failure_categories:
        category_name = category['name']
        print(f"\nCategory: {category_name}")
        print(f"  Failures:")
        for failure in category['failures']:
            print(f"    - {failure}")

        if category_name in mapping:
            print("  Mitigated by:")
            for protocol_name in mapping[category_name]:
                protocol_id = protocol_name_to_id.get(protocol_name, "N/A")
                print(f"    - Protocol {protocol_id}: {protocol_name}")
        else:
            print("  Mitigated by: - No specific protocols mapped for this category yet.")


if __name__ == "__main__":
    analyze_hostility()
>>>>>>> 2b62254a4a2b0c5e95e7554ec9740b55d678c34a
