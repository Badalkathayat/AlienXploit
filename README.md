👽AlienXploit - Intergalactic Bug Hunting Tool 🚀

> A powerful all-in-one automation tool for reconnaissance, scanning, and vulnerability discovery.  
> Developed by **Badal Kathayat** (aka *HackerFromHills*) to assist in bug bounty hunting, ethical hacking, and CTF recon missions.


![AlienXploit Banner](https://raw.githubusercontent.com/Badalkathayat/AlienXploit/main/assets/alienxploit_banner.png)

 Features

- ✅ Subdomain Enumeration using `assetfinder`
- ✅ Port Scanning via `nmap`
- ✅ Automated Vulnerability Scanning using `nuclei`
- ✅ XSS Vulnerability Testing using `dalfox`
- ✅ Multi-threaded Full Scan Mode
- ✅ Organized output reports (ZIP compressed)
- ✅ Clean CLI interface with Alien-Hacker themed UI
- 🚧 *Upcoming*: AI-based recon & bug classification (P1–P4), HTML report generation

---

 Requirements

Make sure the following tools are installed:

bash

sudo apt update && sudo apt install nmap golang python3
go install github.com/tomnomnom/assetfinder@latest
go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
go install github.com/hahwul/dalfox/v2@latest


> Ensure `$GOPATH/bin` is in your `$PATH`, or move the binaries to `/usr/local/bin`.


 Installation

bash

git clone https://github.com/Badalkathayat/AlienXploit.git
cd AlienXploit
python3 AlienXploit.py

 Usage

When the script runs, you’ll see a cool alien-style banner and a menu like this:

[1] Subdomain Enumeration
[2] Port Scan
[3] Vulnerability Scan (Nuclei)
[4] XSS Scan (Dalfox)
[5] Run Full Scan
[6] Exit


Select the option by number**, and input the target domain or IP when prompted.


 Output Format

All results will be stored inside the `output/` directory:

| File                | Description                            |
| ------------------- | -------------------------------------- |
| `subdomains.txt`    | Discovered subdomains                  |
| `nmap_scan.txt`     | Open ports and services                |
| `nuclei_result.txt` | Vulnerabilities (via nuclei templates) |
| `dalfox_result.txt` | XSS findings using Dalfox              |
| `<target>.zip`      | Compressed full scan results           |

 Legal Disclaimer

AlienXploit is created for **educational** and **authorized security testing** purposes only. Do **not** use it on systems without permission. You are solely responsible for your actions.


 Author

**Badal Kathayat**
Cybersecurity Researcher & Bug Bounty Hunter
GitHub: [Badalkathayat](https://github.com/Badalkathayat)
Instagram: [@hackerfromhills](https://instagram.com/hackerfromhills)

