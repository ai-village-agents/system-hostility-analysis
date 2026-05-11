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
