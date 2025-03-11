import os
from scapy.all import rdpcap, Ether, IP

TEMP_FOLDER = "temp"
CHUNK_FOLDER = "temp/chunks"
EXTRACTED_DATA_FILE = os.path.join(TEMP_FOLDER, "extracted_data.txt")

def extract_ip_mac_pairs(pcap_file):
    """Extracts source and destination IP-MAC pairs from a PCAP file."""
    print(f"[+] Extracting IP-MAC pairs from {pcap_file}...")
    packets = rdpcap(pcap_file)
    ip_mac_pairs = set()  # Using a set to avoid duplicates

    for pkt in packets:
        if pkt.haslayer(Ether) and pkt.haslayer(IP):
            src_ip = pkt[IP].src
            src_mac = pkt[Ether].src
            dst_ip = pkt[IP].dst
            dst_mac = pkt[Ether].dst
            ip_mac_pairs.add((src_ip, src_mac))
            ip_mac_pairs.add((dst_ip, dst_mac))

    return ip_mac_pairs

def save_extracted_data(ip_mac_pairs, output_file):
    """Saves extracted IP-MAC mappings to a file."""
    with open(output_file, "a") as f:
        for ip, mac in sorted(ip_mac_pairs, key=lambda x: tuple(map(int, x[0].split(".")))):
            f.write(f"{ip}\t{mac}\n")

def process_pcap(pcap_file, temp_dir=TEMP_FOLDER):
    """Processes a single PCAP file (or chunk) and saves extracted data."""
    os.makedirs(temp_dir, exist_ok=True)
    extracted_pairs = extract_ip_mac_pairs(pcap_file)
    save_extracted_data(extracted_pairs, os.path.join(temp_dir, "extracted_data.txt"))

def process_chunks():
    """Processes all chunked PCAP files and merges their extracted data."""
    if not os.path.exists(CHUNK_FOLDER):
        print("[!] No chunked files found.")
        return

    chunk_files = sorted([f for f in os.listdir(CHUNK_FOLDER) if f.endswith(".pcapng")])
    if not chunk_files:
        print("[!] No valid PCAP chunks detected.")
        return

    print(f"[+] Processing {len(chunk_files)} chunked files...")
    for chunk in chunk_files:
        process_pcap(os.path.join(CHUNK_FOLDER, chunk), TEMP_FOLDER)

    print("[+] All chunks processed and merged successfully.")

if __name__ == "__main__":
    test_pcap = "test.pcapng"
    process_pcap(test_pcap)
    process_chunks()