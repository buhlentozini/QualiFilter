# Allowed columns in the QC matrix by default 
# These can be overridden by user-specified columns in the CLI or config file

DEFAULT_ALLOWED_COLUMNS = [
    "Sample", "Total_reads", "Mapped_reads", "Mapping_pct", "Median_depth",
    "Coverage_gte_10x_pct", "GC_pct", "Kraken_top1_pct", "Kraken_unclassified_pct",
    "Contam_pct", "QC_status", "Total_reads_pass", "Coverage_gte_10x_pct_pass",
    "Contam_pct_pass", "MTB_reads", "Unclassified_reads"
]

DEFAULT_RENAME_MAP = {
    "qualimap_bamqc-total_reads": "Total_reads",
    "qualimap_bamqc-mapped_reads": "Mapped_reads",
    "qualimap_bamqc-percentage_aligned": "Mapping_pct",
    "qualimap_bamqc-median_coverage": "Median_depth",
    "qualimap_bamqc-10_x_pc": "Coverage_gte_10x_pct",
    "qualimap_bamqc-avg_gc": "GC_pct",
    "kraken-pct_top_one": "Kraken_top1_pct",
    "kraken-pct_unclassified": "Kraken_unclassified_pct"
}
