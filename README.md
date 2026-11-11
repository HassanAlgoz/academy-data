# Academy datasets

Dataset files, descriptions, attribution, and reading examples for Academy courses live in [`data/`](data/). Each dataset folder has a README and direct file download links.

## Read a dataset locally

```sh
uv add "hassan-academy-data @ git+https://github.com/HassanAlgoz/academy-data.git@v1" pandas
```

```python
import academy
import pandas as pd

url = academy.get_data_url("tips")
print(url)
tips = pd.read_csv(url)
```

`get_data_url` returns an ordinary HTTPS URL string. Missing or unknown names raise an explanatory error listing the available choices and suggesting similar names. The Academy browser imports `academy` automatically; local Python requires the import above.

Some source files use tabs, pipe separators, or no header. Follow the reading example in that dataset's README.

## Maintain the catalog

Edit the metadata comment and prose in `data/<dataset>/README.md`, then run:

```sh
python scripts/build_catalog.py
PYTHONPATH=. python scripts/test_academy.py
```

`catalog.json` and `academy/_registry.py` are generated from those READMEs. Do not edit them by hand. Keep published tags immutable. Release `v1` contains unchanged copies of the files for browser downloads; raw URLs read the files in Git. For a new data version, publish a new tag, update the module URL/version, and advance the LMS's pinned revision deliberately.

Original data retains its source terms; see each README for provenance. This repository does not relicense third-party datasets.
