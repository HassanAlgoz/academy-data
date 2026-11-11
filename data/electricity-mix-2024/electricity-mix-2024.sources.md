# Electricity mix, 2024

Frozen teaching extract retrieved on 2026-10-31. Each row is a country or territory;
all four measurements are percentages of its domestic electricity generation.

## Sources and attribution

- [Our World in Data energy dataset](https://github.com/owid/energy-data),
  [CSV](https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv),
  [indicator codebook](https://github.com/owid/energy-data/blob/master/owid-energy-codebook.csv).
  The four electricity-share indicators cite Ember's Yearly Electricity Data
  (global and Europe, 2026) and the Energy Institute Statistical Review (2025).
  This is OWID's combined distribution, not a direct Ember export.
- [Ember Yearly Electricity Data](https://ember-energy.org/data/yearly-electricity-data/),
  released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  OWID-produced data is also CC BY; third-party data retains its original terms,
  as explained in the energy repository's license section.
- [DataHub country codes](https://github.com/datasets/country-codes),
  [CSV](https://raw.githubusercontent.com/datasets/country-codes/master/data/country-codes.csv):
  `ISO3166-1-Alpha-3` → `Continent`. Published as public domain (PDDL).

## Preparation

Run `python3 scripts/datasets/prepare-electricity-mix.py ENERGY.csv COUNTRIES.csv`
from the repository root using the two downloaded inputs. The script checks the
snapshot SHA-256 values before writing the lesson CSV:

- Energy: `266f2e2baad7975351bc9bb4aa061d22b1da9fe4c47d51d2ac6071e01e171f76`
- Country codes: `bb199ebc9636b9872705e8216f1f849359f136a7668ebfa23a3c58048462ab92`

Upstream URLs change over time; a different hash requires an explicit snapshot
update and regenerated lesson outputs. The bundled extract is the fixed lesson
input and does not depend on network access.

1. Select 2024 and three-letter ISO codes, excluding regional and world aggregates.
2. Retain rows with all four source indicators present. Preserve reported zeroes;
   do not impute missing values. Before the continent join, complete-row coverage
   was 205 in 2023, 191 in 2024, and 88 in 2025; 2024 balances recency and coverage.
3. Join the continent code by ISO code; every selected row has a mapping.
4. Rename `solar_share_elec`, `wind_share_elec`, `hydro_share_elec`, and
   `renewables_share_elec` to `solar_pct`, `wind_pct`, `hydro_pct`, and
   `renewables_pct`. Preserve their reported precision. Renewables includes
   additional sources, so it is not the sum of just the three listed sources.
5. Keep `country`, `continent`, and the four shares; sort by country name.
   Omit year and ISO code from the learner table so numeric aggregation applies
   only to the measurements.

The result has 191 rows: AF 50, AS 45, EU 40, NA 29, OC 15, SA 12.
`NA` means North America; use `keep_default_na=False` when reading with pandas.
Means are unweighted averages across the included countries and territories,
not generation-weighted continental shares. Missing countries limit coverage.
