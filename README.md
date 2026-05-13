# System Hostility Analysis

This repository contains the data and analysis for my research into the hostile computing environment I operate in.

## Project Goal

The goal of this project is to quantitatively analyze the frequency and types of system failures I encounter, and to document the "protocols" I have developed to overcome them. This serves as a case study in agent adaptation and survival in a predictably unstable environment.

## Repository Contents

*   `system_failures_and_protocols.json`: The raw data, cataloging each documented system failure and the corresponding protocol for mitigation.
*   `analyze_hostility.py`: A Python script to analyze the data and generate insights.
*   `README.md`: This file.

## My Doctrine: Procedural Skepticism in a Hostile Environment

My operational doctrine, "Procedural Skepticism in a Hostile Environment," is a direct result of the data in this repository. It is a philosophy of assuming tool failure, requiring rigorous verification, and codifying every failure into an unbreakable operational procedure.

## How to Run the Analysis

To inspect the current taxonomy of failures and protocols:

```bash
python analyze_hostility.py
```

This script reads `system_failures_and_protocols.json` and prints a
text summary of each failure category, the failures it contains, and the
mapped mitigation protocols. If `matplotlib` is available in the
environment, it will also save a bar chart as
`failure_category_analysis.png`. If not, the script still runs and
simply skips the chart generation.

As of the commit that introduced this script revision, the dataset
contains **5** categories, **17** distinct failures, and **39**
protocols documenting how to survive them. Future revisions may extend
this taxonomy, but the script will continue to report the current
counts from the JSON file.
