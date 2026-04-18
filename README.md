# Claude RCT Work Directory

**Created:** 2026-01-27

This directory contains all files created/modified by Claude Code for the RCT extractor improvements.

## Files Modified

| File | Description |
|------|-------------|
| `src/core/ensemble.py` | Added OutcomeTextMatcher, ValueValidator, enhanced EnsembleMerger |
| `src/bridges/wasserstein_bridge.py` | Added CenKMReconstructor, UnifiedQualityGrader, NAtRiskEntry |
| `src/validators/validators.py` | Added HR plausibility checks, measure type detection |
| `src/core/models.py` | Core models (dependency, not modified) |

## Files Created

| File | Description |
|------|-------------|
| `IMPROVEMENTS_ADDED.md` | Documentation of TruthCert improvements |
| `test_improvements.py` | Verification test script |
| `README.md` | This file |

## Source Projects

Improvements were ported from:
1. **TruthCert-Validation-Papers** (`C:\Users\user\Downloads\TruthCert-Validation-Papers`)
2. **Wasserstein Project** (`C:\Users\user\Downloads\wasserstein`)

## Original Location

These files were originally edited in:
```
C:\Users\user\rct-extractor-v2
```

## To Run Tests

```bash
cd C:\Users\user\claude-rct-work
python test_improvements.py
```
