#github-repo-analyzer

Python utility for auditing GitHub repository metrics and exporting LLM-ready health insights.

---

## Overview

**GitHubRepoAnalyzer** is a lightweight, zero-dependency Command Line Interface (CLI) utility designed for developers and open-source maintainers. It automates the process of fetching repository metadata, analyzing community engagement, and evaluating project maintenance status using the official GitHub REST API.

The tool generates structured reports optimized for Large Language Models (LLMs), allowing developers to quickly feed repository health metrics into AI workflows for comprehensive auditing.

## 🚀 How to Use (v2.0.0)

**For Windows Users:**
The easiest way to run the analyzer with full color support:
1. Clone the repository to your PC.
2. Double-click the `start.bat` file.
3. Paste the GitHub repository URL when prompted!

### Key Features

| Feature | Description | Technical Implementation |
| :--- | :--- | :--- |
| **Automated Metric Auditing** | Tracks live counts of stars, forks, and open issues | GitHub REST API integration |
| **Health Scoring** | Evaluates project status based on open issues and pull requests | Static analysis heuristics |
| **Structured Export** | Generates standalone, clean Markdown health reports | Native file I/O formatting |
| **Zero External Setup** | Operates dynamically using Python standard libraries | Lightweight deployment |

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- `requests` library

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Shariiik/github-repo-analyzer.git
cd github-repo-analyzer
```

Install the required configuration:

```bash
pip install -r requirements.txt
```

### Usage

Execute the automated Windows batch script or run the Python script directly from your terminal by passing any valid public GitHub repository URL:

```bash
python GitHubRepoAnalyzer.py [https://github.com/psf/requests](https://github.com/psf/requests)
```

---

## Report Structure Example

The tool automatically formats the extracted metadata into a standardized Markdown report (`{repository_name}_health_report.md`):

```markdown
# Health Report: owner/repository
Generated: YYYY-MM-DD HH:MM

Description: Public repository description text.
Created At: YYYY-MM-DD
License: License Name
Health Score: [Excellent / Good / Needs Attention]

Stars: 0
Forks: 0
Open Issues: 0

Recommendations:
- Actionable optimization advice based on repository state.
```

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.
