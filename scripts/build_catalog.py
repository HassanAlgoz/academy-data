"""Generate the catalog and Python registry from dataset READMEs."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
catalog = {}
for readme in sorted((ROOT / "data").glob("*/README.md")):
    text = readme.read_text()
    match = re.search(r"<!-- academy-data\n(.*?)\n-->", text, re.S)
    if not match:
        raise ValueError(f"Missing metadata: {readme}")
    metadata = json.loads(match[1])
    description = text[:match.start()] + text[match.end():]
    for file in metadata["files"]:
        name = file["name"]
        if name in catalog or not re.fullmatch(r"[a-z0-9-]+(?:/[a-z0-9-]+)?", name):
            raise ValueError(f"Invalid or duplicate name: {name}")
        path = readme.parent / file["file"]
        if path.parent != readme.parent or not path.is_file():
            raise ValueError(f"Invalid dataset file: {path}")
        raw = path.read_bytes()
        rows = list(csv.reader(io.StringIO(raw.decode("utf-8-sig"), newline=""), delimiter=file["delimiter"]))
        columns = rows.pop(0) if file["hasHeader"] else file["columns"]
        catalog[name] = {
            **file,
            "title": metadata["title"],
            "repositoryPath": path.relative_to(ROOT).as_posix(),
            "readmePath": readme.relative_to(ROOT).as_posix(),
            "readme": description.strip(),
            "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "columns": columns,
            "rowCount": len(rows),
            "preview": rows[:3] + (rows[max(3, len(rows)-3):] if len(rows)>3 else []),
        }
(ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n")
registry = {name: item["repositoryPath"] for name, item in catalog.items()}
(ROOT / "academy/_registry.py").write_text('# Generated from data/*/README.md; do not edit.\nFILES = ' + repr(registry) + '\n')
print(f"Validated {len(catalog)} dataset files")
