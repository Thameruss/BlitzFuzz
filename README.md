Here is the updated **README.md** with the changes:

````markdown
# BlitzFuzz - High-speed Subdomain Fuzzer

BlitzFuzz is a fast and simple subdomain fuzzer built in Python. It allows you to perform high-speed fuzzing on target URLs to discover subdomains using a wordlist. The tool is designed to be lightweight with no unnecessary bloat.

### Features
- High-speed subdomain fuzzing
- Simple, easy-to-use command-line interface
- Customizable request rate and timeout
- Results saved to an output file (optional)
- User-agent customization
- Progress bar for tracking fuzzing status

### Installation
To use BlitzFuzz, you need Python installed. If you don’t have Python, you can download it from [python.org](https://www.python.org/downloads/).

### Usage

After downloading or cloning BlitzFuzz, navigate to the folder containing the script. Then, you can run the tool using the following command:

```bash
python BlitzFuzz.py -u "https://mozilla.org" -w "/path/to/your/wordlist.txt"
````

Replace `/path/to/your/wordlist.txt` with the actual path of your wordlist file. For example, on Windows, this might be:

```bash
python BlitzFuzz.py -u "https://mozilla.org" -w "C:/Users/(YOUR_USERNAME)/Desktop/subfind.txt"
```

On Linux or macOS, the command would look like:

```bash
python BlitzFuzz.py -u "https://mozilla.org" -w "/home/(YOUR_USERNAME)/Desktop/subfind.txt"
```

### Command-Line Arguments

* `-u` / `--url`: The target URL (you must use the base domain, e.g., `https://mozilla.org`).
* `-w` / `--wordlist`: The path to your wordlist file containing possible subdomains.
* `--rate`: The number of requests to make per second. Default is `10.0`.
* `--timeout`: The timeout per request in seconds. Default is `10`.
* `-o` / `--output`: (Optional) The file where results will be saved.
* `--ua` / `--user-agent`: (Optional) A custom User-Agent string for the requests. Default is `"Mozilla/5.0 (BlitzFuzz)"`.

### Example

To fuzz subdomains of `mozilla.org` using a wordlist stored at `/path/to/your/wordlist.txt`, use the following command:

```bash
python BlitzFuzz.py -u "https://mozilla.org" -w "/path/to/your/wordlist.txt"
```

For example, if you're on Windows and your wordlist is on your desktop, you can run:

```bash
python BlitzFuzz.py -u "https://mozilla.org" -w "C:/Users/(YOUR_USERNAME)/Desktop/subfind.txt"
```

On Linux/macOS:

```bash
python BlitzFuzz.py -u "https://mozilla.org" -w "/home/(YOUR_USERNAME)/Desktop/subfind.txt"
```

This will fuzz the subdomains, show progress in the terminal, and print any subdomains found that return a `200 OK` status. If the `-o` option is specified, the results will also be written to a file.

### Output

The output will look like this:

```
[Progress] |██████████████████████--------------------------| 75% Complete
[200] https://www.mozilla.org - Found
[200] https://support.mozilla.org - Found

Found Subdomains:
[200] https://www.mozilla.org - Found
[200] https://support.mozilla.org - Found

Finished fuzzing 5000 subdomains. Found 2 valid URLs.
```

If you use the `-o` option, the results will be saved to a file, e.g., `results.txt`, in the format:

```
[200] https://www.mozilla.org
[200] https://support.mozilla.org
```

### Requirements

* Python 3.x
* `requests` library

You can install the required libraries using `pip`:

```bash
pip install requests
```

