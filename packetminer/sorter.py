import os

TEMP_FOLDER = "temp"
EXTRACTED_DATA_FILE = os.path.join(TEMP_FOLDER, "extracted_data.txt")
SORTED_OUTPUT_FILE = os.path.join(TEMP_FOLDER, "sorted_ip_mac.txt")

def load_extracted_data():
    """Loads extracted IP-MAC mappings from a file."""
    if not os.path.exists(EXTRACTED_DATA_FILE):
        print("[!] No extracted data found.")
        return []

    with open(EXTRACTED_DATA_FILE, "r") as f:
        data = {line.strip() for line in f.readlines()}  # Remove duplicates
    return list(data)

def get_oui(mac_address):
    """Extracts the first 3 octets of a MAC address (OUI)."""
    return ":".join(mac_address.split(":")[:3])

def process_data(data):
    """Processes IP-MAC mappings and extracts OUI."""
    processed_data = []
    for entry in data:
        ip, mac = entry.split("\t")
        oui = get_oui(mac)
        processed_data.append(f"{ip}\t{mac}\t{oui}")
    return processed_data

def sort_ip_mac_data(data):
    """Sorts IP-MAC mappings based on IP octets."""
    def ip_sort_key(entry):
        ip = entry.split("\t")[0]
        return tuple(map(int, ip.split(".")))  # Convert IP to tuple for sorting
    
    return sorted(data, key=ip_sort_key)

def save_sorted_data(sorted_data):
    """Saves sorted IP-MAC mappings with OUI."""
    with open(SORTED_OUTPUT_FILE, "w") as f:
        for entry in sorted_data:
            f.write(entry + "\n")
    print(f"[+] Sorted data with OUI saved to {SORTED_OUTPUT_FILE}")

def merge_and_sort():
    """Loads, processes, sorts, and saves the final IP-MAC mappings with OUI."""
    print("[+] Merging and sorting extracted data with OUI...")
    data = load_extracted_data()
    if data:
        processed_data = process_data(data)
        sorted_data = sort_ip_mac_data(processed_data)
        save_sorted_data(sorted_data)
    else:
        print("[!] No data available to sort.")

if __name__ == "__main__":
    merge_and_sort()
