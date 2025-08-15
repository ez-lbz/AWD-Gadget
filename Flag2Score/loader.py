import os
import time
import logging
import shellcode

NUM_FILES = 1
MAX_RETRIES = 5
RETRY_DELAY = 2

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def get_recent_files():
    flag_dir = "../Flag"
    if not os.path.exists(flag_dir):
        logging.error("Flag directory not found")
        return []
    files = [os.path.join(flag_dir, f) for f in os.listdir(flag_dir) if f.endswith(".txt")]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files[:NUM_FILES]

def read_flags(files):
    flags = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                flag = line.strip()
                if flag:
                    flags.append(flag)
    return flags

def submit_flag(flag):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            status = shellcode.shellcode(flag)
            if status:
                logging.info(f"[+] Submitted {flag} successfully on attempt {attempt}")
                return True
            else:
                logging.warning(f"[-] Failed to submit {flag} on attempt {attempt}")
        except Exception as e:
            logging.error(f"Error submitting {flag} on attempt {attempt}: {e}")
        time.sleep(RETRY_DELAY)
    return False

def main():
    files = get_recent_files()
    if not files:
        logging.error("No flag files found")
        return
    flags = read_flags(files)
    failed_flags = []
    for flag in flags:
        success = submit_flag(flag)
        if not success:
            failed_flags.append(flag)
        time.sleep(RETRY_DELAY)
    if failed_flags:
        logging.info("Failed flags:")
        for f in failed_flags:
            logging.info(f)

if __name__ == "__main__":
    main()