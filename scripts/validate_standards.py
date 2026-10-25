"""Validate stable identities and declared files in the standards manifest."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "standards" / "standard-manifest.json"
RULE = re.compile(r"`([A-Z][A-Z0-9]*-[0-9]{3})`")
NORMATIVE = re.compile(r"^\d+\. `(?:Must|Must Not|Should|Could|Won't \(for now\))`")


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    seen: set[str] = set()
    errors: list[str] = []
    for standard in manifest["standards"]:
        path = ROOT / standard["path"]
        if not path.is_file():
            errors.append(f"missing standard: {standard['path']}")
            continue
        pattern = re.compile(standard["ruleIdPattern"])
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            ids = RULE.findall(line)
            if NORMATIVE.match(line) and not ids:
                errors.append(f"{standard['path']}:{number}: normative rule has no ID")
            for rule_id in ids:
                if not pattern.fullmatch(rule_id):
                    continue
                if rule_id in seen:
                    errors.append(f"duplicate rule ID: {rule_id}")
                seen.add(rule_id)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(seen)} rules in {manifest['repositoryKey']}.")


if __name__ == "__main__":
    main()
