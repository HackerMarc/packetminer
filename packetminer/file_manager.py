import os
import shutil

TEMP_FOLDER = "temp"

def list_pcap_files(directory="."):
    """Lists all PCAP files in the given directory."""
    pcap_files = [f for f in os.listdir(directory) if f.endswith((".pcap", ".pcapng"))]
    return sorted(pcap_files)

def create_temp_folder():
    """Creates a temporary folder for extracted data, clearing it if it exists."""
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)  # Remove old temp files
    os.makedirs(TEMP_FOLDER)
    return TEMP_FOLDER

def clear_temp_folder():
    """Deletes all temporary files."""
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)
        print("[+] Temporary folder cleared.")
    else:
        print("[!] No temporary files to clear.")

if __name__ == "__main__":
    print("\n[+] Testing file manager module...")
    print("[+] PCAP files in current directory:", list_pcap_files())
    create_temp_folder()
    print("[+] Temp folder created at:", TEMP_FOLDER)