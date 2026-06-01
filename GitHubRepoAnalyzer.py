import sys
from datetime import datetime
import requests

if len(sys.argv) < 2:
    print("Usage: python analyzer.py <GITHUB_REPO_URL>")
    sys.exit(1)

url = sys.argv[1]

path = url.replace("https://github.com/", "").strip("/")
parts = path.split("/")

if len(parts) < 2:
    print("[-] Invalid URL. Use: https://github.com/user/repo")
    sys.exit(1)

owner, repo = parts[0], parts[1]
api_url = f"https://api.github.com/repos/{owner}/{repo}"

print(f"[+] Checking {owner}/{repo}...")
res = requests.get(api_url)

if res.status_code == 404:
    print("[-] Repo not found.")
    sys.exit(1)
elif res.status_code != 200:
    print(f"[-] API Error: {res.status_code}")
    sys.exit(1)

data = res.json()

stars = data.get("stargazers_count", 0)
forks = data.get("forks_count", 0)
issues = data.get("open_issues_count", 0)
license_name = data.get("license", {}).get("name", "No License") if data.get("license") else "No License"
created = datetime.strptime(data["created_at"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d")

if issues == 0:
    score = "Excellent"
elif issues < 15:
    score = "Good"
else:
    score = "Needs Attention"

report_lines = [
    f"# Health Report: {owner}/{repo}",
    f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n",
    f"Description: {data.get('description', 'No description.')}",
    f"Created At: {created}",
    f"License: {license_name}",
    f"Health Score: {score}\n",
    f"Stars: {stars}",
    f"Forks: {forks}",
    f"Open Issues: {issues}\n",
    "Recommendations:"
]

if issues > 20:
    report_lines.append("- High number of open issues.")
if license_name == "No License":
    report_lines.append("- Consider adding an MIT or Apache 2.0 license.")
if stars < 10:
    report_lines.append("- Project is in early stage.")
    
if len(report_lines) == 10:
    report_lines.append("- Repository looks great!")

filename = f"{repo}_health_report.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))

print(f"[+] Saved to {filename}")
