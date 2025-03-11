import os
import time
from banner import display_banner
from file_manager import list_pcap_files, create_temp_folder
from chunker import detect_large_pcap, chunk_pcap, explain_chunking
from extractor import process_pcap
from sorter import merge_sorted_data
from output import save_output

def main_menu():
    """Displays the interactive menu for user selection."""
    while True:
        display_banner()
        print("[1] Select a PCAP file")
        print("[2] Select a folder of PCAPs")
        print("[3] View temporary files")
        print("[4] Clear temporary files")
        print("[5] Exit")

        choice = input("\n[?] Select an option: ").strip()

        if choice == "1":
            select_pcap_file()
        elif choice == "2":
            select_pcap_folder()
        elif choice == "3":
            view_temp_files()
        elif choice == "4":
            clear_temp_files()
        elif choice == "5":
            print("\n[+] Exiting PacketMiner. Goodbye!")
            break
        else:
            print("\n[!] Invalid option. Please try again.")
            time.sleep(1)

def select_pcap_file():
    """Handles selection of a single PCAP file."""
    pcap_files = list_pcap_files()
    if not pcap_files:
        input("\n[!] No PCAP files found. Press Enter to return to menu.")
        return
    
    print("\nAvailable PCAP files:")
    for idx, file in enumerate(pcap_files, start=1):
        print(f"[{idx}] {file}")

    choice = input("\n[?] Select a PCAP file (or 'b' to go back): ").strip()
    if choice.lower() == "b":
        return

    try:
        choice = int(choice) - 1
        if 0 <= choice < len(pcap_files):
            selected_file = pcap_files[choice]
            handle_large_pcap(selected_file)
        else:
            print("\n[!] Invalid selection.")
    except ValueError:
        print("\n[!] Please enter a valid number.")

def select_pcap_folder():
    """Handles selection of a folder containing PCAP files."""
    folder_path = input("\n[?] Enter the folder path containing PCAP files: ").strip()
    if not os.path.isdir(folder_path):
        print("\n[!] Invalid folder path.")
        return

    pcap_files = list_pcap_files(folder_path)
    if not pcap_files:
        print("\n[!] No PCAP files found in the folder.")
        return
    
    print(f"\n[+] Found {len(pcap_files)} PCAP files in {folder_path}.")
    process_pcap_folder(pcap_files)

def handle_large_pcap(file_path):
    """Detects if a PCAP is too large and prompts for chunking."""
    large_status = detect_large_pcap(file_path)

    if large_status == "suggest":
        explain_chunking()
        choice = input("[?] Would you like to chunk this file? (y/n): ").strip().lower()
        if choice == "y":
            chunk_pcap(file_path)

    elif large_status:
        explain_chunking()
        print("\n[!] This file **must** be chunked before processing.")
        input("Press Enter to continue...")
        chunk_pcap(file_path)

    process_pcap(file_path)

def process_pcap_folder(pcap_files):
    """Processes multiple PCAP files in a folder."""
    temp_folder = create_temp_folder()
    for file in pcap_files:
        handle_large_pcap(file)
    
    print("\n[+] Merging sorted data from all files...")
    merged_file = merge_sorted_data(temp_folder)
    save_output(merged_file)

def view_temp_files():
    """Displays contents of the temporary folder."""
    temp_folder = "temp"
    if not os.path.exists(temp_folder) or not os.listdir(temp_folder):
        print("\n[!] No temporary files found.")
    else:
        print("\n[+] Temporary files:")
        for file in os.listdir(temp_folder):
            print(f"  - {file}")
    input("\nPress Enter to return to menu.")

def clear_temp_files():
    """Deletes all temporary files."""
    temp_folder = "temp"
    if os.path.exists(temp_folder):
        for file in os.listdir(temp_folder):
            os.remove(os.path.join(temp_folder, file))
        print("\n[+] Temporary files cleared.")
    else:
        print("\n[!] No temporary files to clear.")
    time.sleep(1)

if __name__ == "__main__":
    main_menu()
