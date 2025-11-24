# MultiQC QC Extractor

**Version:** 1.0.0

---

## Overview

**MultiQC QC Extractor** is a command-line tool that extracts sequencing quality control (QC) metrics from a MultiQC tabular summary (.tabular) file and generates a consolidated QC matrix containing only the metrics of interest.  

The tool evaluates each sample against user-defined QC thresholds and assigns a **Pass/Fail** status automatically. It supports optional derived metrics and allows you to select which QC metrics to include in the output.

---

## Features

- Extracts key QC metrics from MultiQC tabular reports.
- Generates a summarized QC matrix in **TSV** and **CSV** formats.
- Automatically evaluates samples against **user-defined thresholds**.
- Computes derived read metrics (optional).
- Logs processing steps and warnings for traceability.
- Lists all available columns in the input file for inspection.

---

## Installation

### Using pip

```bash
pip install multiqc-qc-extractor
```

### Using conda (Bioconda)

```bash
conda install -c bioconda multiqc-qc-extractor
```

---

## Usage

Basic example:

```bash
multiqc-qc-extract \
    --input multiqc_data.tabular \
    --thresholds '{"Total_reads":1000000,"Coverage_gte_10x_pct":90,"Contam_pct":5}' \
    --outdir qc_results
```

### Command-line Options

| Option | Description |
|--------|-------------|
| `--input` / `-i` | MultiQC tabular input file (TSV) |
| `--attributes` / `-a` | Comma-separated list of QC metrics to include (optional). If empty, all metrics are included. |
| `--thresholds` / `-t` | JSON string with QC thresholds. Example: `{"Total_reads":1000000,"Coverage_gte_10x_pct":90,"Contam_pct":5}` |
| `--round` / `-r` | Number of decimals to round numeric columns (default: 2) |
| `--derive_reads` | Calculate derived read metrics (optional) |
| `--outdir` / `-o` | Output directory (default: current directory) |
| `--list` | List all available columns in the input file and exit |

---

## Available Metrics / Attributes

- **Sample** – unique sample identifier  
- **Total_reads** – total number of sequencing reads  
- **Mapped_reads** – reads mapped to the reference genome  
- **Median_depth** – median sequencing coverage  
- **Coverage_gte_10x_pct** – percentage of genome covered at ≥10x depth  
- **GC_pct** – GC content percentage of reads  
- **Kraken_top1_pct** – percentage of reads assigned to top taxonomic hit  
- **Kraken_unclassified_pct** – percentage of reads unclassified by Kraken  
- **Contam_pct** – estimated contamination percentage  
- **QC_status** – Pass/Fail based on thresholds  
- **MTB_reads** – reads assigned to target organism (derived if `--derive_reads` is used)  
- **Unclassified_reads** – unclassified reads (derived if `--derive_reads` is used)  

---

## Output

- **TSV**: `QC_matrix_multiqc.tsv`  
- **CSV**: `QC_matrix_multiqc.csv`  

Both outputs include QC Pass/Fail status for each sample and any derived metrics if requested.

---

## Threshold Behavior

- Thresholds are provided as a **JSON-formatted string**.  
- Example thresholds:

```json
{
  "Total_reads": 1000000,
  "Coverage_gte_10x_pct": 90,
  "Contam_pct": 5
}
```

- Samples failing any threshold are marked as `Fail` in the `QC_status` column.  

---

## Notes

- Read counts (`Total_reads`, `Mapped_reads`) are automatically scaled if MultiQC reports them in millions.  
- If no attributes are specified, all available metrics are included.  
- Derived metrics are calculated only if the `--derive_reads` option is enabled.  
- Rounding precision defaults to **2 decimals** but can be customized.  
- Logs are saved as `qc_tool.log` in the output directory.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## References

- [MultiQC](https://multiqc.info/) – for generating the tabular QC summary input.

