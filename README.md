# Algorithmic Modeling of Morphogenetic Fields: Continuous Bioelectric Cellular Automata (CBCA)

## 1. Executive Research Summary
This repository contains a high-performance **Continuous Bioelectric Cellular Automaton (CBCA)** written in Python. It provides a computational validation of developmental bioelectricity, specifically modeling the foundational paradigms established by Dr. Michael Levin.

Traditional computational biology models cellular morphology through genetic sequencing or localized chemical signaling pathways. This project implements an alternative paradigm: **treating tissue matrices as open, self-organizing computational networks governed by continuous membrane voltage gradients ($V_{mem}$) and gap-junction communication channels.**

The simulation demonstrates that a tissue matrix can store a robust anatomical memory and coordinate body-wide structural regeneration following severe physical trauma **without requiring modifications to the underlying genetic hardware.**

## 2. Mathematical & Algorithmic Foundations

### A. Intercellular Voltage Diffusion (The Discrete Laplacian)
Communication between adjacent cellular nodes is modeled as an electrical diffusion process across a continuous 2D spatial grid. The slow-moving intercellular voltage gradient is calculated using a discrete numerical approximation of the 2D Laplacian operator across a standard 4-point localized stencil:

$$\nabla^2 V_{mem} \approx V(x+1, y) + V(x-1, y) + V(x, y+1) + V(x, y-1) - 4V(x, y)$$

The state updates are evaluated at each time increment ($\Delta t$) across the network graph via:

$$V_{mem}^{t+1}(x, y) = V_{mem}^{t}(x, y) + D \cdot \nabla^2 V_{mem}^{t}(x, y)$$

Where $D$ represents the non-dimensional diffusion coefficient modeling the conductivity of intercellular **gap junctions**.

### B. Bioelectric Error-Gradient Correction (Anatomical Memory Retrieval)
The tissue grid actively compares its local structural state against a global morphogenetic target memory template. When structural deviations or amputations occur, a top-down error-gradient loop drives the cellular nodes to reconstruct their missing components until the system arrives back at its homeostatic resting potential.
