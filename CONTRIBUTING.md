# Contributing to Awesome Medical World Models

Thank you for improving this resource.

## How to Add a Paper

Please open a pull request and update `data/papers.csv`. Add one row with:

- year
- category
- model name
- full paper title
- venue / type
- modality
- main task
- paper URL
- code URL if available
- project URL if available
- code status
- short note

## Accepted Categories

- Survey / Review
- Foundational World Models
- Medical Imaging World Models
- EHR / Clinical Trajectory World Models
- Treatment Planning / Counterfactual Decision Support
- Ultrasound / Probe Guidance World Models
- Surgical / Robotic Medical World Models
- Molecular / Biological / Virtual Cell World Models

## Code Status Rules

Use one of these values:

- `available`
- `repository available; code coming soon`
- `related model suite available`
- `official code not found`
- `not found`
- `n/a`

Do not add random mirrors or unofficial code unless clearly labeled as unofficial.

## Pull Request Checklist

- [ ] Paper URL is valid.
- [ ] Code URL is official or clearly labeled.
- [ ] Category is appropriate.
- [ ] Notes are concise.
- [ ] No duplicate paper already exists.
- [ ] `python scripts/check_links.py data/papers.csv data/datasets.csv` runs locally.
