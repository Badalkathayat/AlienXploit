# AlienXploit
AlienXploit - An intergalactic AI-powered bug bounty tool 🚀👽

 👽 AlienXploit v1.2

**AlienXploit** is an advanced, alien-themed bug bounty automation tool developed by **Badal Kathayat (aka HackerFromHills)**.  
It automates the full reconnaissance + scanning process for web applications using some of the most powerful tools in cybersecurity.

>  "Hacking the galaxy, one domain at a time..." – AlienXploit


 Features

- 🌐 **Subdomain Enumeration** — using `assetfinder`
- 🛡️ **Port Scanning** — using `nmap`
- 🚨 **Vulnerability Scanning** — using `nuclei` with default templates
- 💉 **XSS Scanning** — using `dalfox`
- 📦 **Full Scan Mode** — runs all the above in parallel and creates ZIP reports
- 📄 **Log File** — Everything gets saved in `AlienXploit.log`
- 🎨 Cool alien-themed terminal banner on start

 Project Structure


AlienXploit/
├── AlienXploit.py      # Main Python script
├── README.md           # You're reading this
├── output/             # All scan results saved here
├── LICENSE             # (Optional)
└── assets/             # (Optional: for logo/banner image)

 Requirements

You must have the following tools installed and accessible from your terminal:

- `assetfinder`
- `nmap`
- `nuclei`
- `dalfox`
- `Python 3.x`
- Python module: `termcolor` (install using `pip install termcolor`)

 Usage

bash
# Run the tool
python3 AlienXploit.py


Once it starts, you'll see a menu like:

[1] Subdomain Enumeration
[2] Port Scan
[3] Vulnerability Scan (Nuclei)
[4] XSS Scan (Dalfox)
[5] Run Full Scan
[6] Exit
```

Example:

```bash
Enter your choice: 5
Enter target domain: example.com
```

All scan outputs will be saved inside the `/output/` folder and zipped.


Disclaimer

> This tool is for **educational and authorized security testing only**.
> Unauthorized scanning of systems is **illegal** and **strictly discouraged**.



👤 Author

* **Name:** Badal Kathayat
* **Alias:** HackerFromHills
* **GitHub:** [Badalkathayat](https://github.com/Badalkathayat)
* **LinkedIn:** [badal-kathayat-hackerfromhills](https://www.linkedin.com/in/badal-kathayat-hackerfromhills/)


 📌 Upcoming Features

* 🤖 AI-based Recon (OpenAI/GPT integration)
* 📊 Better HTML report generation
* 🧠 Automated Bug Prioritization (P1–P4)
* ⚙️ Custom Nuclei & Dalfox rulesets
* 🖼️ Alien-hacker logo/banner integration


 ⭐ Show your Support!

If you like the project, give it a ⭐ star on GitHub!


