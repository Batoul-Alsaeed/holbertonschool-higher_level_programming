#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys

status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
file_size_total = 0
line_count = 0

def print_stats():
    print(f"File size: {file_size_total}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()

        try:
            status_code = parts[-2]
            file_size = int(parts[-1])
            file_size_total += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (IndexError, ValueError):
            pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
