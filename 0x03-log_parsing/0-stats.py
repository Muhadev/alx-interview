#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """ Print the current statistics. """
    global total_file_size, status_counts
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def signal_handler(sig, frame):
    """ Handle the SIGINT signal (CTRL + C) to print statistics. """
    print_stats()
    sys.exit(0)

# Set up the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue
        
        ip, _, _, date, _, request, status, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        
        # Verify the format of the log line
        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        # Convert and sum file size
        try:
            file_size = int(file_size)
            total_file_size += file_size
        except ValueError:
            continue

        # Count status codes
        try:
            status = int(status)
            if status in status_counts:
                status_counts[status] += 1
        except ValueError:
            continue

        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats()

    except Exception:
        continue

# Print final statistics if the script ends without an interruption
print_stats()
