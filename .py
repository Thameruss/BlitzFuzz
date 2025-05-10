import argparse
import time
import requests
from urllib.parse import urlparse

# BlitzFuzz - High-speed URL fuzzer in Python

# Banner function
def print_banner():
    banner = r'''
 _______  ___      ___   _______  _______ 
|  _    ||   |    |   | |       ||       |
| |_|   ||   |    |   | |_     _||____   |
|       ||   |    |   |   |   |   ____|  |
|  _   | |   |___ |   |   |   |  | ______|
| |_|   ||       ||   |   |   |  | |_____ 
|_______||_______||___|   |___|  |_______|
 _______  __   __  _______  _______       
|       ||  | |  ||       ||       |      
|    ___||  | |  ||____   ||____   |      
|   |___ |  |_|  | ____|  | ____|  |      
|    ___||       || ______|| ______|      
|   |    |       || |_____ | |_____       
|___|    |_______||_______||_______|       

             BlitzFuzz - High-Speed Subdomain Fuzzer
   Fast, simple, and to the point — no bloat, just results.
   Created by Thamer Almutairi
   Instagram: @0x54414d | X: @sliusx

'''
    print(banner)

# Helper: Build the target URL based on the mode and word
def build_url(base, word, mode):
    parsed = urlparse(base)
    if mode == "subdomain":
        return f"{parsed.scheme}://{word}.{parsed.netloc}{parsed.path}"
    elif mode == "path":
        if base.endswith("/"):
            return f"{base}{word}"
        return f"{base}/{word}"
    elif mode == "replace":
        return base.replace("FUZZ", word)
    return base

def fetch(url, timeout):
    try:
        response = requests.get(url, timeout=timeout)
        return url, response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return url, None, str(e)

def print_progress_bar(iteration, total, length=50):
    if total > 0:
        percent = ("{0:.1f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = '█' * filled_length + '-' * (length - filled_length)
        print(f'\r[Progress] |{bar}| {percent}% Complete', end="")

def run(wordlist, base_url, mode, rate, timeout, output_file, user_agent):
    headers = {"User-Agent": user_agent}
    delay = 1.0 / rate

    total_subdomains = len(wordlist)
    successful_subdomains = 0

    if total_subdomains == 0:
        print("Error: The wordlist is empty or not provided properly.")
        return

    results = []
    seen = set()  # Set to store found subdomains to avoid duplicates

    # Initialize the progress bar
    print_progress_bar(0, total_subdomains)

    found_subdomains = []  # List to keep track of found subdomains

    for i, word in enumerate(wordlist):
        word = word.strip()
        fuzzed_url = build_url(base_url, word, mode)

        if fuzzed_url in seen:
            continue  # Skip duplicates

        seen.add(fuzzed_url)

        # Fetch the URL and check response
        url, status, _ = fetch(fuzzed_url, timeout)
        if status == 200:
            results.append(url)
            # Print the found subdomains beneath the progress bar
            found_subdomains.append(f"[200] {url} - Found")

        # Print progress bar for every 10 subdomains
        if i % 10 == 0 or i == total_subdomains - 1:
            print_progress_bar(i + 1, total_subdomains)  # We add +1 to handle the last update

        time.sleep(delay)  # Adjust the rate of requests

    # After the loop, print the found subdomains below the progress bar
    print("\nFound Subdomains:")
    for subdomain in found_subdomains:
        print(subdomain)

    print(f"\nFinished fuzzing {total_subdomains} subdomains. Found {len(results)} valid URLs.")

    if output_file:
        with open(output_file, 'w') as f:
            for result in results:
                f.write(f"[200] {result}\n")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="BlitzFuzz - High-speed URL fuzzer")
    parser.add_argument("-u", "--url", required=True, help="Target URL (use FUZZ for replace mode)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
    parser.add_argument("-m", "--mode", choices=["subdomain", "path", "replace"], default="replace", help="Fuzzing mode")
    parser.add_argument("--rate", type=float, default=10.0, help="Requests per second (float allowed)")
    parser.add_argument("--timeout", type=int, default=10, help="Timeout per request (seconds)")
    parser.add_argument("-o", "--output", help="Output file to write results")
    parser.add_argument("--ua", "--user-agent", dest="user_agent", default="Mozilla/5.0 (BlitzFuzz)", help="Custom User-Agent")

    args = parser.parse_args()

    with open(args.wordlist, 'r') as f:
        wordlist = f.readlines()

    run(wordlist, args.url, args.mode, args.rate, args.timeout, args.output, args.user_agent)

if __name__ == "__main__":
    main()
