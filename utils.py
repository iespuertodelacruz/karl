import re


def load_groups(filepath):
    groups = []
    with open(filepath) as f:
        for line in f.readlines():
            r = re.match(r'\s*(\S+)\s*=\s*(\S+)', line.strip())
            if r:
                groups.append(r.groups())
    return dict(groups)
