"""
Core extraction modules
"""

from .models import (
    ExtractionOutput,
    ExtractionRecord,
    HazardRatioCI,
    OddsRatioCI,
    RiskRatioCI,
    MeanDifference,
    BinaryOutcome,
    Arm,
    Provenance,
    ExtractionConfidence
)

# Optional submodules: this repo ships a subset of the full extractor.
# Guard these imports so the present modules (models, ensemble) stay
# importable even when extractor/evaluation/meta_analysis are not vendored here.
try:
    from .extractor import RCTExtractor
except ImportError:
    RCTExtractor = None

try:
    from .evaluation import (
        Evaluator,
        EvaluationReport,
        load_gold_dataset,
        evaluate_batch
    )
except ImportError:
    Evaluator = EvaluationReport = load_gold_dataset = evaluate_batch = None

try:
    from .meta_analysis import (
        MetaAnalysisFields,
        calculate_se_from_ci,
        detect_outcome_priority,
        classify_effect_direction,
        detect_subgroup_analyses,
        extract_continuous_outcomes,
        calculate_nnt_from_rd,
        enhance_extraction
    )
except ImportError:
    MetaAnalysisFields = calculate_se_from_ci = detect_outcome_priority = None
    classify_effect_direction = detect_subgroup_analyses = None
    extract_continuous_outcomes = calculate_nnt_from_rd = enhance_extraction = None

from .ensemble import (
    EnsembleMerger,
    MergedResult,
    ExtractorResult,
    ConfidenceGrade,
    generate_ensemble_report
)

__all__ = [
    # Main extractor
    'RCTExtractor',

    # Models
    'ExtractionOutput',
    'ExtractionRecord',
    'HazardRatioCI',
    'OddsRatioCI',
    'RiskRatioCI',
    'MeanDifference',
    'BinaryOutcome',
    'Arm',
    'Provenance',
    'ExtractionConfidence',

    # Evaluation
    'Evaluator',
    'EvaluationReport',
    'load_gold_dataset',
    'evaluate_batch',

    # Meta-analysis support (from v4.8)
    'MetaAnalysisFields',
    'calculate_se_from_ci',
    'detect_outcome_priority',
    'classify_effect_direction',
    'detect_subgroup_analyses',
    'extract_continuous_outcomes',
    'calculate_nnt_from_rd',
    'enhance_extraction',

    # Ensemble merger
    'EnsembleMerger',
    'MergedResult',
    'ExtractorResult',
    'ConfidenceGrade',
    'generate_ensemble_report'
]
