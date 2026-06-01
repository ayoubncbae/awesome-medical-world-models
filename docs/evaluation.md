# Evaluation of Medical World Models

Medical world models should be evaluated beyond standard generative fidelity. In clinical settings, the simulated future must be plausible, calibrated, and intervention-sensitive.

## Recommended Evaluation Axes

| Axis | Question | Example Metrics |
|---|---|---|
| Temporal consistency | Does the patient state remain coherent over long rollouts? | Success@k, retention rate, event consistency |
| Image fidelity | Does the generated image look realistic? | SSIM, PSNR, LPIPS, FID, expert Turing test |
| Clinical correctness | Does the simulation preserve anatomy and pathology? | expert review, disease-specific scoring, lesion metrics |
| Treatment validity | Does the model respond correctly to treatment changes? | counterfactual agreement, treatment ranking accuracy |
| Risk calibration | Are risk estimates calibrated? | Brier score, ECE, calibration plots |
| Surgical usefulness | Does simulated policy performance correlate with real performance? | task success, rank correlation, rollout agreement |
| Biological plausibility | Are predicted mechanisms consistent with known biology? | pathway consistency, DE prediction, perturbation ranking |

## Minimum Reporting Checklist

- Report dataset split and patient-level separation.
- Report uncertainty or confidence where possible.
- Separate image realism from clinical correctness.
- Compare against non-world-model baselines.
- Evaluate counterfactual sensitivity if the model is used for treatment planning.
- Include human expert evaluation for high-risk generative outputs.
