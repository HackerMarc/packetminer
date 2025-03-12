# PacketMiner 

### Extract, Sort, and Analyze IP-MAC Mappings from PCAP Files

**PacketMiner** is a powerful Python tool designed for processing large PCAP files, extracting IP-MAC mappings, sorting them by IP address, and generating structured outputs in TXT and CSV formats. It was designed to cut down on time when analyzing large PCAP files taken during asset discovery engagements.

---

## Features
✅ Extracts **IP-MAC pairs** from PCAP files  
✅ Handles **large PCAPs (90GB+)** by **chunking** when needed  
✅ Sorts IP addresses in **octet order**  
✅ Outputs results as **TXT and CSV** with **OUI information**  
✅ **Interactive CLI** for easy usage  

---

## Installation
### 1️⃣ Clone the Repository

```bash
git clone https://github.com/HackerMarc/packetminer.git
cd packetminer
```

### 2️⃣ Run the Installation Script

```bash
chmod +x install.sh
./install.sh
source ./venv/bin/activate
```

This will:
- Install **Wireshark CLI tools** (if needed)  
- Set up a **Python virtual environment**  
- Install required **Python dependencies** 
- Activate the virtual environment 

---

## Usage
### Run PacketMiner

```bash
packetminer
```
or
```bash
python packetminer/cli.py
```
You'll see an interactive menu:

```
 ██▓███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████▄▄▄█████▓ ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀▓  ██▒ ▓▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███  ▒ ▓██░ ▒░▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄░ ▓██▓ ░ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒ ▒██▒ ░ ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░   ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░   ░    ░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░         ░   ▒   ░        ░ ░░ ░    ░    ░      ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
               ░  ░░ ░      ░  ░      ░  ░               ░    ░           ░    ░  ░   ░     
                   ░                                              - Developed by @HackerMarc   

[1] Select a PCAP file  
[2] Select a folder of PCAPs  
[3] View temporary files  
[4] Clear temporary files  
[5] Exit  

[?] Select an option: 
```

### Extract IP-MAC Mappings from a PCAP File
1. Select **Option 1** (`Select a PCAP file`)  
2. Choose a **PCAP file** from the list  
3. If the file is **over 5GB**, you’ll be prompted for **chunking**  
4. The tool extracts **IP-MAC mappings**, sorts them, and saves results  

---

## Advanced Features
### Processing Large PCAPs
- If a file is **over 5GB**, chunking is **suggested**  
- If a file is **over 10GB**, chunking is **required**  
- Uses `editcap` to split large PCAPs into manageable chunks  

### Sorting & Merging
- **IP addresses are sorted** by octet order  
- **Duplicate IP-MAC pairs** are removed  
- **Multiple PCAP files can be merged** into a single output  

---

## Development
### Run PacketMiner in Development Mode

```bash
python -m packetminer.cli
```

### Uninstall PacketMiner

```bash
pip uninstall packetminer
```

---

## To-Do & Future Updates
- [ ] **OUI Vendor Lookup** (via API or local database)  
- [ ] **More Export Formats** (JSON, Excel)  
- [ ] **Multi-threading for Faster Processing**  

---

## License
📜 MIT License
