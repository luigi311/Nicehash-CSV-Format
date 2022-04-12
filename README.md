# Nicehash-CSV-Format

Format Nicehash CSV export to the correct format for websites that dont have support for it but accept CSVs in a certain template.

Currently only supports Cointracking.info and only supports mining and withdraws. Only tested with BTC payouts.
CSV will be outputed to the same folder as the input with a _$(exchange).csv name.

## Usage

```bash
python main.py -f <input.csv> -e cointracking
```
