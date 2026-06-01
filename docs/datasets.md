# Datasets for Medical World Models

The machine-readable dataset list is available in [`../data/datasets.csv`](../data/datasets.csv).

## Practical Notes

- Many medical datasets require credentialed access, data-use agreements, or institutional approval.
- Public imaging datasets are often easier to reproduce than EHR and surgical robotics datasets.
- Treatment-planning datasets are frequently private because they combine imaging, treatment protocol, and outcome labels.
- For EHR trajectory world models, patient-level temporal splits are preferred over random event-level splits.
- For surgical world models, action labels and robot kinematics are often the limiting factor.
- For virtual-cell models, perturbation coverage and batch effects are central evaluation concerns.
