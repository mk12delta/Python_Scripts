#!/usr/bin/env python3
#program to analyze apache web logs

import sys, re, socket

# get_hostname takes an ip address as a string and returns a string
# that is either the hostname associated with that ip address or the
# ip address itself because there isn't a reverse lookup.
def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return ip_address

LOG_RE = re.compile(
    r'^(\S+) \S+ \S+ \[([^:]+):(\d\d):\d\d:\d\d [^\]]*\] '
    r'"(\S+) (\S+) (\S+)" (\d{3}) (\S+) "([^"]*)" "([^"]*)"'
)

def progress_bar(current, total, width=50):
    filled = int(width * current / total)
    bar = '=' * filled + '-' * (width - filled)
    percent = current / total * 100
    print(f"\r[{bar}] {percent:6.2f}% ({current}/{total})", end="", flush=True)

def read_file(filenames):
    lines = []
    for filename in filenames:
        with open(filename) as f:
            lines.extend(f.readlines())
    return lines

def parse_line(line, counts):
    match = LOG_RE.match(line)
    if match is None:
        return
    ip, date, hour, method, url, version, status, nbytes, referer, agent = match.groups()
    hostname = get_hostname(ip)
    for report, key in (('hostname', hostname),
                        ('date', date),
                        ('hour', hour),
                        ('method', method),
                        ('url', url),
                        ('version', version),
                        ('status', status)):
        counts.setdefault(report, {})
        counts[report][key] = counts[report].get(key, 0) + 1

def write_report(out, title, data, sort_key=None):
    total = sum(data.values())
    out.write("=" * 78 + "\n")
    out.write(f"{title}\n")
    out.write("=" * 78 + "\n\n")
    out.write("Count  Percent  Resource\n")
    out.write("-----  -------  --------\n")
    for key in sorted(data, key=sort_key):
        hits=data[key]
        percent = hits / total * 100
        out.write(f"{hits:>5}  {percent:6.2f}%  {key}\n")
    out.write("\n")

def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} logfile [logfile ...]')
        sys.exit(1)
    lines = read_file(sys.argv[1:])
    total = len(lines)
    counts = {}
    for i, line in enumerate(lines, start=1):
        parse_line(line, counts)
        progress_bar(i, total)
    print()
    reports = (
        ('Hostname Report', 'hostname', None),
        ('Date Report',     'date',     None),
        ('Hours Report',    'hour',     None),
        ('Status Report',   'status',   int),
        ('Method Report',   'method',   None),
        ('Version Report',  'version',  None),
        ('URL Report',      'url',      None),
    )
    with open("Carmine_Adam.summary", "w") as out:
        for title, report, sort_key in reports:
            write_report(out, title, counts.get(report, {}), sort_key)

    print("DONE!")

if __name__ == "__main__":
    main()