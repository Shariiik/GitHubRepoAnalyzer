import urllib.request
import json
import sys
import time
import os
from datetime import datetime

class Colors:
    RED = '\033[91m'
    DARK_RED = '\033[31m'
    GREY = '\033[90m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    print(f"{Colors.RED}{Colors.BOLD}")
    print(r"""
  _____ _ _   _   _       _       _____                  
 / ____(_) | | | | |     | |     |  __ \                 
| |  __ _| |_| |_| |_   _| |__   | |__) |___ _ __   ___  
| | |_ | | __|  _  | | | | '_ \  |  _  // _ \ '_ \ / _ \ 
| |__| | | |_| | | | |_| | |_) | | | \ \  __/ |_) | (_) |
 \_____|_|\__|_| |_|\__,_|_.__/  |_|  \_\___| .__/ \___/ 
                                            | |          
                                            |_|          
         /\                | |                     
        /  \   _ __   __ _| |_   _ _______ _ __  
       / /\ \ | '_ \ / _` | | | | |_  / _ \ '__| 
      / ____ \| | | | (_| | | |_| |/ /  __/ |    
     /_/    \_\_| |_|\__,_|_|\__, /___\___|_|    
                              __/ |              
                             |___/               
    """)
    print(f"{Colors.DARK_RED}           [ v2.0.0 | LLM-Ready JSON Engine ]{Colors.ENDC}")
    print(f"{Colors.GREY}{'=' * 65}{Colors.ENDC}\n")

def animate_loading(target):
    sys.stdout.write(f"{Colors.CYAN} ❯ Connecting to {target}{Colors.ENDC}\n")
    sys.stdout.write(f"   {Colors.DARK_RED}[{Colors.ENDC}")
    toolbar_width = 50
    
    for i in range(toolbar_width):
        time.sleep(0.03)
        sys.stdout.write(f"{Colors.RED}▓{Colors.ENDC}")
        sys.stdout.flush()
    sys.stdout.write(f"{Colors.DARK_RED}]{Colors.ENDC} {Colors.GREEN}DONE{Colors.ENDC}\n\n")

def fetch_repo_data(url):
    parts = url.rstrip('/').split('/')
    if len(parts) < 2:
        print(f"{Colors.RED}❌ Error: Invalid GitHub URL.{Colors.ENDC}")
        return None
    owner, repo = parts[-2], parts[-1]
    
    target = f"{owner}/{repo}"
    animate_loading(target)
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    try:
        req = urllib.request.Request(api_url, headers={'User-Agent': 'GitHubRepoAnalyzer-App'})
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"{Colors.RED}❌ API Request Failed: {e}{Colors.ENDC}")
        return None

def main():
    os.system('')
    print_banner()
    
    if len(sys.argv) < 2:
        print(f"{Colors.RED}⚠️ Usage: python GitHubRepoAnalyzer.py <repository_url>{Colors.ENDC}")
        sys.exit(1)
        
    data = fetch_repo_data(sys.argv[1])
    
    if data:
        name = data.get('full_name', 'Unknown')
        stars = data.get('stargazers_count', 0)
        forks = data.get('forks_count', 0)
        issues = data.get('open_issues_count', 0)
        health = "Excellent" if issues < 20 else "Needs Attention"
        
        print(f"{Colors.GREEN} ✅ Scan Complete!{Colors.ENDC}")
        print(f"    ⭐ Stars:  {Colors.BOLD}{stars}{Colors.ENDC}")
        print(f"    🍴 Forks:  {Colors.BOLD}{forks}{Colors.ENDC}")
        print(f"    🐛 Issues: {Colors.BOLD}{issues}{Colors.ENDC}\n")
        
        export_data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "tool_version": "2.0.0"
            },
            "repository": {
                "name": name,
                "url": data.get('html_url', ''),
                "description": data.get('description', '')
            },
            "metrics": {
                "stars": stars,
                "forks": forks,
                "open_issues": issues
            },
            "health_status": health
        }
        
        filename = f"{name.replace('/', '_')}_metrics.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=4)
            
        print(f"{Colors.CYAN} 💾 LLM-Ready JSON exported to: {Colors.BOLD}{filename}{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
