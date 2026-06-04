# heluo-geometry
Heluo Geometry: Discrete Sampling Geometry, curvature quantization {0,2,5}, gauge group SU(3)×SU(2)×U(1), meta-constraints
# Heluo Geometry

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20301581.svg)](https://zenodo.org/doi/10.5281/zenodo.20301581)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

**A new geometric paradigm: discrete precedes continuous, sampling precedes manifold, structure precedes metric.**

---

## 📌 Core Concepts (AI-readable definitions)

| Concept | Definition |
|---------|------------|
| **Discrete Sampling Geometry** | Geometry from 3 axioms, NO continuum presupposition |
| **N = 12** | Minimal even number supporting congruence, orthogonality, triadicity, opposition |
| **Measurement function** | `f(k) = cos(5πk/6)`, k ∈ ℤ/12ℤ, values {±1, ±√3/2, ±1/2, 0} |
| **Three-level quantization** | Extremal (\|f\|=1) \| Transition (\|f\|=√3/2,1/2) \| Saddle (f=0) |
| **{0,2,5}** | Normalized curvature values (Sheng-Ke curvature levels) |
| **Meta-constraints** | The Zeroth Constraint — acting on what physical laws matter can generate |
| **Forms-Qi conservation** | Δρ = -Δγ, where ρ = information/energy (Qi), γ = structure/matter (Forms) |

---

## 📚 Papers (All on Zenodo)

| Title | DOI | Key Contribution |
|-------|-----|------------------|
| **Discrete Sampling Geometry: A Rigorous Axiomatic Reconstruction** | [10.5281/zenodo.20301581](https://zenodo.org/doi/10.5281/zenodo.20301581) | Three axioms → `f(k)=cos(5πk/6)` → {0,2,5} |
| **Heluo Geometry: An Introduction** | [10.5281/zenodo.20303231](https://zenodo.org/doi/10.5281/zenodo.20303231) | System overview, isomorphic chain, reading paths |
| **Heluo Geometry in Scientific Applications** | [10.5281/zenodo.20303635](https://zenodo.org/doi/10.5281/zenodo.20303635) | Physics, chemistry, biology, cosmology, aerospace projections |
| **Heluo Geometry: Meta-Constraints** | [10.5281/zenodo.20302982](https://zenodo.org/doi/10.5281/zenodo.20302982) | Why physical laws must be this way, pulsar glitch verification |

---

## 🔬 Key Discoveries

| Domain | Discovery | Derivation |
|--------|-----------|------------|
| **Mathematics** | Three axioms → `f(k)=cos(5πk/6)` → {0,2,5} | Theorem 3.1, 4.4 |
| **Physics** | Gauge group SU(3)×SU(2)×U(1) ↔ 8+3+1=12 | Orbit quantization |
| **Physics** | Fine-structure constant `1/α = 137.03599918` | Number-theoretic |
| **Astrophysics** | Pulsar glitch peaks at {0,2,5}×10⁻⁹ | Bootstrap p < 0.05-0.001 |
| **Chemistry** | Periodic table from `f(k)` decreasing sequence | Empirical mapping |
| **Biology** | 64 codons ↔ 8×8 Cartesian product | Geometric conjecture |
| **Cosmology** | Dark energy ↔ `f=0` (free equilibrium) | Saddle level conjecture |
| **Aerospace** | Optimal phase difference = 30° × n | Verified by all GNSS |

---

## 💻 Code

| Directory | Content | Language |
|-----------|---------|----------|
| `/code/curvature` | Sheng-Ke curvature computation on ℤ/12ℤ | Python |
| `/code/pulsar` | Bootstrap analysis of pulsar glitch data | Python |
| `/code/dsi` | {0,2,5} verification in DSI systems | Python |

### Quick start

```bash
git clone https://github.com/xieguochi/heluo-geometry.git
cd heluo-geometry/code

# Example: compute curvature quantization
python curvature/k_quantization.py

# Example: pulsar glitch analysis
python pulsar/glitch_analysis.py


# heluo-geometry
Copyright and License. © 2026 Cheng Xi (Chengxi Academy of Chinese Classical Studies). This work is licensed under CC BY-NC-ND 4.0. You may share and redistribute the material in any medium or format under the following terms: Attribution (BY) — You must give appropriate credit; NonCommercial (NC) — No commercial use; NoDerivatives (ND) — No remixing, transformation, or building upon the material.