# Taxonomy of Medical World Models

This taxonomy groups medical world models by the clinical system they simulate and the action space they condition on.

## 1. Medical Imaging World Models

These models learn latent representations of anatomy, disease, and image formation. They may forecast future images, reconstruct missing regions, or learn projection-aware anatomical representations.

Representative models: Brain-WM, X-WIN, Xray2Xray, CheXWorld, TaDiff-Net.

## 2. EHR and Clinical Trajectory World Models

These models simulate future clinical events from patient histories. They are useful for long-horizon forecasting, digital twins, and clinical event generation.

Representative models: EHRWorld, Foresight, CoMET.

## 3. Treatment Planning and Counterfactual Decision Support

These models explicitly condition future trajectories on treatment options or clinical actions. Their key value is counterfactual simulation: what may happen under treatment A versus treatment B.

Representative models: MeWM, CLARITY, Brain-WM.

## 4. Ultrasound and Probe Guidance World Models

These models learn how ultrasound observations change under physical probe motion. They support next-action guidance and target-view acquisition.

Representative models: EchoWorld, Cardiac Copilot / Cardiac Dreamer.

## 5. Surgical and Robotic Medical World Models

These models simulate surgical environments, robot policy rollouts, or action-conditioned surgical video. They support policy evaluation, synthetic data generation, and autonomous surgical training.

Representative models: Surgical Vision World Model, Cosmos-Surg-dVRK, SurgWorld, MT World Model.

## 6. Molecular, Biological, and Virtual Cell World Models

These models simulate cellular or molecular responses to perturbations. They combine prediction with mechanistic interpretability.

Representative models: VCWorld, Lingshu-Cell.
