"""Small explicit-rule CSV demo; no network, no third-party dependencies."""
import argparse
import csv
import json
from pathlib import Path


def clean(source, destination, trim_columns=(), drop_exact=False):
    source, destination = Path(source), Path(destination)
    if source.resolve() == destination.resolve():
        raise ValueError('Use a new output path; preserve the original.')
    with source.open(newline='', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        if not fields or len(fields) != len(set(fields)):
            raise ValueError('Missing or duplicate headers require review.')
        if not set(trim_columns).issubset(fields):
            raise ValueError('Unknown trim column.')
        rows = list(reader)
    if any(None in r or any(v is None for v in r.values()) for r in rows):
        raise ValueError('Uneven row width requires review.')
    changes, result, seen = [], [], set()
    for line, raw in enumerate(rows, 2):
        row = dict(raw)
        for field in trim_columns:
            value = row[field].strip()
            if value != row[field]:
                changes.append({'source_line': line, 'column': field, 'action': 'trim'})
                row[field] = value
        key = tuple(row[f] for f in fields)
        if drop_exact and key in seen:
            changes.append({'source_line': line, 'action': 'drop_exact_after_trim'})
            continue
        seen.add(key)
        result.append(row)
    with destination.open('x', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(result)
    report = {'input_rows': len(rows), 'output_rows': len(result),
              'trim_columns': list(trim_columns), 'drop_exact': drop_exact, 'changes': changes}
    with Path(str(destination) + '.changes.json').open('x', encoding='utf-8') as f:
        json.dump(report, f, indent=2)
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source')
    p.add_argument('destination')
    p.add_argument('--trim', action='append', default=[])
    p.add_argument('--drop-exact', action='store_true')
    a = p.parse_args()
    print(json.dumps(clean(a.source, a.destination, a.trim, a.drop_exact), indent=2))
