# Small data cleanup: explicit rules, visible checks

Original fictional examples for two everyday jobs: CSV cleanup and selectable-text PDF table extraction. This is an AI-assisted demo, not customer work or proof of sales.

## Try the CSV example locally

Requires Python 3 only. No API, account or network call.

```sh
python3 clean_csv.py messy-inventory.csv cleaned-inventory.csv --trim product --drop-exact
```

The script preserves the original, trims only the named column, optionally removes exact duplicates **after** the agreed trim, and writes a row-count/change report. All values stay strings, including SKU `0012`. It refuses malformed rows and existing output files. Do not choose deduplication rules without checking what a row represents.

CSV itself cannot enforce spreadsheet column types. When opening the result in Excel, import identifier columns as Text to preserve leading zeros. Review untrusted CSV values beginning with formula characters before opening them in a spreadsheet; this demo is not a general CSV security sanitizer.

## Check the PDF example

`fictional-pdf-table.pdf` is an original selectable-text PDF. `service-demonstration.xlsx` includes its extraction and a separate cleaning example with raw source and change log. Compare source rows and columns, SKU values, quantities and page references. A selectable PDF can still have an unsuitable layout. Scans, handwriting, ambiguous cells and complex merged tables need separate review; never invent missing values.

## Prefer a done-for-you pilot?

Disclosure: I operate these Fiverr services. You can use the free examples without ordering.

- [Excel/CSV cleanup — $20, 2 days](https://www.fiverr.com/fghjhbcv/clean-and-organize-excel-csv-data-with-a-documented-change-log): one flat sheet, up to 100 data rows and 10 columns, agreed cleanup plus change log, one revision.
- [Selectable PDF tables to Excel/CSV — $20, 2 days](https://www.fiverr.com/fghjhbcv/convert-selectable-pdf-tables-to-excel-or-csv-with-source-checks): one PDF, up to 5 pages, 500 table rows and 10 columns, one revision. Send a de-identified sample on Fiverr first to confirm extractability.

AI may assist code or planning; outputs are checked against source material. Remove personal/confidential information and provide only authorized material. No account credentials needed. All orders, payment, communication and delivery stay on Fiverr. No revenue, ranking or business outcome is guaranteed.

## License

The original code and fictional examples in this repository are provided under the MIT License; see LICENSE.
