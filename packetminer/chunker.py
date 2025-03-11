import os
import subprocess
import math

CHUNK_SIZE_MB = 5000  # 5GB suggestion, 10GB forced chunking (set in cli.py)
FORCE_CHUNK_MB = 10000  # 10GB threshold for automatic chunking
CHUNK_OUTPUT_FOLDER = "temp/chunks"

def detect_large_pcap(file_path):
    """Detects if a PCAP file exceeds the chunking thresholds."""
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)  # Convert bytes to MB

    if file_size_mb > FORCE_CHUNK_MB:
        print(f"\n[!] Large PCAP detected ({round(file_size_mb, 2)} MB). Chunking is **required** at 10GB+.")
        return True
    elif file_size_mb > CHUNK_SIZE_MB:
        print(f"\n[!] Large PCAP detected ({round(file_size_mb, 2)} MB). Chunking is **recommended** at 5GB+.")
        return "suggest"
    return False

def chunk_pcap(file_path, chunk_size=1000000):
    """
    Splits a large PCAP file into smaller chunks using `editcap`.
    
    - `chunk_size` defines the number of packets per chunk.
    - Output is stored in `temp/chunks/`.
    """
    os.makedirs(CHUNK_OUTPUT_FOLDER, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    chunk_pattern = os.path.join(CHUNK_OUTPUT_FOLDER, f"{base_name}_chunk_%05d.pcapng")

    print(f"\n[+] Chunking {file_path} into {chunk_size}-packet segments...")
    
    try:
        subprocess.run(["editcap", "-c", str(chunk_size), file_path, chunk_pattern], check=True)
        print("[+] Chunking complete. Chunks saved in 'temp/chunks/'.")
    except FileNotFoundError:
        print("\n[!] Error: `editcap` not found. Install Wireshark CLI tools and try again.")
    except subprocess.CalledProcessError:
        print("\n[!] Error: Chunking failed. Check if the PCAP file is valid.")

def explain_chunking():
    """Provides an explanation of the chunking process to the user."""
    print("\n[+] Chunking Information:")
    print("- Large PCAP files can cause performance issues or fail to load.")
    print("- Splitting the file into smaller parts improves processing speed.")
    print("- `editcap` is used to break the file into 1M-packet chunks by default.")
    print("- Chunks are processed individually and merged later.")

if __name__ == "__main__":
    test_pcap = "test_large.pcapng"
    print("\n[+] Testing chunker module...")
    large_detected = detect_large_pcap(test_pcap)
    if large_detected:
        explain_chunking()