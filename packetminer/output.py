import os
import csv

TEMP_FOLDER = "temp"
SORTED_OUTPUT_FILE = os.path.join(TEMP_FOLDER, "sorted_ip_mac.txt")
FINAL_TXT_FILE = "final_output.txt"
FINAL_CSV_FILE = "final_output.csv"

def load_sorted_data():
    """Loads sorted IP-MAC-OUI data from the temp file."""
    if not os.path.exists(SORTED_OUTPUT_FILE):
        print("[!] No sorted data found.")
        return []

    with open(SORTED_OUTPUT_FILE, "r") as f:
        return [line.strip().split("\t") for line in f.readlines()]

def save_to_txt(data):
    """Saves data to a final text file."""
    with open(FINAL_TXT_FILE, "w") as f:
        for row in data:
            f.write("\t".join(row) + "\n")
    print(f"[+] Final TXT output saved as {FINAL_TXT_FILE}")

def save_to_csv(data):
    """Saves data to a final CSV file with a header row."""
    with open(FINAL_CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["IP Address", "MAC Address", "OUI"])  # Header row
        writer.writerows(data)
    print(f"[+] Final CSV output saved as {FINAL_CSV_FILE}")

def generate_output():
    """Loads sorted data and saves it in TXT & CSV formats."""
    print("[+] Generating final output files...")
    data = load_sorted_data()
    if data:
        save_to_txt(data)
        save_to_csv(data)
    else:
        print("[!] No data available for output.")

if __name__ == "__main__":
    generate_output()