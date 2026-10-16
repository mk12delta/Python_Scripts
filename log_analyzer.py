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
FIND_IP_RE = re.compile(r'^\d+\.\d+\.\d+\.\d+$')

def get_domain(hostname):
    if FIND_IP_RE.match(hostname) or '.' not in hostname:
        return 'DOTTED QUAD OR OTHER'
    return '.'.join(hostname.split('.')[-2:])

def get_family(agent):
    if 'Opera' in agent:
        return 'Opera'
    if 'MSIE' in agent or 'Trident' in agent:
        return 'Microsoft'
    if 'Chrome' in agent:
        return 'Chrome'
    if 'Firefox' in agent:
        return 'Firefox'
    if 'Safari' in agent:
        return 'Safari'
    return 'Unknown'

def get_os(agent):
    if 'Windows' in agent:
        return 'Windows'
    if 'Linux' in agent:
        return 'Linux'
    if 'Macintosh' in agent:
        return 'Macintosh'
    return 'Other'

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
    if agent == '-':
        agent_key = 'NO BROWSER ID'
    else:
        agent_key = agent
    if 'http' in referer:
        referer_key = referer
        refdomain = get_domain(referer.split('/')[2].split(':')[0])
    else:
        referer_key = 'NO REFERER'
        refdomain = 'NONE'
    for report, key in (('hostname', hostname),
                        ('domain', get_domain(hostname)),
                        ('date', date),
                        ('hour', hour),
                        ('status', status),
                        ('method', method),
                        ('version', version),
                        ('url', url),
                        ('agent', agent_key),
                        ('family', get_family(agent)),
                        ('referer', referer_key),
                        ('refdomain', refdomain),
                        ('os', get_os(agent))):
        counts.setdefault(report, {})
        counts[report][key] = counts[report].get(key, 0) + 1
    if nbytes != '-':
        counts['bytes'] = counts.get('bytes', 0) + int(nbytes)

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
        ('Hostnames Report', 'hostname', None),
        ('Domains Report', 'domain', None),
        ('Dates Report', 'date', None),
        ('Hours Report', 'hour', None),
        ('Status Code Report', 'status', int),
        ('Method Report', 'method', None),
        ('HTTP Version Report', 'version', None),
        ('Resource Report', 'url', None),
        ('Browser Report', 'agent', None),
        ('Browser Family Report', 'family', None),
        ('Referer Report', 'referer', None),
        ('Referer Domains Report', 'refdomain', None),
        ('Operating Systems Report', 'os', None),
    )

    with open("Carmine_Adam.summary", "w") as out:
        out.write("Apache Logfile Processor\n\n")
        out.write(f"Logfile(s) processed: {' '.join(sys.argv[1:])} \n\n")
        for title, report, sort_key in reports:
            write_report(out, title, counts.get(report, {}), sort_key)
        out.write(f"Total bytes served: {counts.get('bytes', 0)}\n")
    print("DONE!")

if __name__ == "__main__":
    main()