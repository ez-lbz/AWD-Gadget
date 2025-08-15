import os
import re
import time
import logging
import hashlib
import shellcode
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def normalize_url(line):
    line = line.strip()
    if not line:
        return None

    parts = re.split(r'\s+', line)
    if len(parts) == 2:
        line = f"{parts[0]}:{parts[1]}"

    if not re.match(r'^[a-zA-Z]+://', line):
        line = "http://" + line

    parsed = urlparse(line)
    if not parsed.hostname:
        return None
    return line

flag_pattern = re.compile(r'flag\{.*?\}', re.IGNORECASE)

def process_url(url):
    try:
        resp = shellcode.shellcode(url)
        flags = flag_pattern.findall(resp)
        if flags:
            logging.info(f"[+] {url} -> Found: {flags}")
        else:
            logging.info(f"[-] {url} -> No flag found")
        return flags
    except Exception as e:
        logging.error(f"Error processing {url}: {e}")
        return []

def deduplicate_flags(flags_list):
    seen_hashes = set()
    unique_flags = []
    for flag in flags_list:
        h = hashlib.sha256(flag.encode('utf-8')).hexdigest()
        if h not in seen_hashes:
            seen_hashes.add(h)
            unique_flags.append(flag)
    return unique_flags

def main():
    if not os.path.exists("../target.txt"):
        logging.error("target.txt file not found")
        return

    with open("../target.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    urls = []
    for line in lines:
        norm = normalize_url(line)
        if norm:
            urls.append(norm)

    urls = list(set(urls))
    logging.info(f"Loaded {len(urls)} targets")

    all_flags = []
    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = {executor.submit(process_url, url): url for url in urls}
        for future in as_completed(futures):
            all_flags.extend(future.result())

    unique_flags = deduplicate_flags(all_flags)

    if unique_flags:
        os.makedirs("../Flag", exist_ok=True)
        filename = f"../Flag/{int(time.time())}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            for flag in sorted(unique_flags):
                f.write(flag + "\n")
        logging.info(f"Found {len(unique_flags)} unique flags, saved to {filename}")
    else:
        logging.info("No flags found")

if __name__ == "__main__":
    main()