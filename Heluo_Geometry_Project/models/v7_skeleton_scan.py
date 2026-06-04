#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
河洛几何 v7.0 — 五维投影与 D₁₂ 对称性深度扫描
核心: 粒子质量比 2^(k/5) 结构验证
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.heluo_axioms import HeluoAxioms
from core.d12_group import D12Group
from utils.plotter import HeluoPlotter

def load_masses(filepath='data/processed_masses.txt'):
    """加载粒子质量数据"""
    masses = []
    names = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            parts = line.split(',')
            mass = float(parts[0].strip())
            name = parts[1].strip()
            masses.append(mass)
            names.append(name)
    return np.array(masses), names

def scan_5d_grid(masses, base_scale=3414.75, tolerance=0.001):
    """
    扫描 2^(k/5) 网格匹配
    返回: hit_pairs, hit_details, total_pairs
    """
    n = len(masses)
    total_pairs = 0
    hit_pairs = 0
    hit_details = []
    
    # 确定 k 范围
    k_min = int(np.floor(np.log2(masses.min() / base_scale) * 5))
    k_max = int(np.ceil(np.log2(masses.max() / base_scale) * 5))
    
    for i in range(n):
        for j in range(i + 1, n):
            m_low = masses[i]
            m_high = masses[j]
            ratio = m_high / m_low
            
            k_step = np.round(np.log2(ratio) * 5)
            
            if k_step < k_min or k_step > k_max:
                continue
            
            theory = 2.0 ** (k_step / 5.0)
            deviation = abs(ratio - theory) / theory
            
            total_pairs += 1
            
            if deviation < tolerance:
                hit_pairs += 1
                hit_details.append({
                    'low_mass': m_low,
                    'high_mass': m_high,
                    'ratio': ratio,
                    'k_step': int(k_step),
                    'theory': theory,
                    'deviation': deviation
                })
    
    return hit_pairs, hit_details, total_pairs

def main():
    print("=" * 70)
    print("河洛几何 v7.0 — 五维投影与 D₁₂ 对称性深度扫描")
    print("=" * 70)
    
    # 加载数据
    masses, names = load_masses()
    print(f"\n[1/4] 成功加载 {len(masses)} 个有效粒子质量点。")
    
    # 执行扫描
    print("\n[2/4] 执行全局对数网格搜索 (Target: 2^(1/5))...")
    hit_pairs, hit_details, total_pairs = scan_5d_grid(masses)
    hit_rate = hit_pairs / total_pairs * 100
    
    print(f"扫描完成。总有效粒子对: {total_pairs}")
    print(f">>> 命中 5D 网格 (2^(k/5)): {hit_pairs} 对")
    print(f">>> 命中率: {hit_rate:.1f}%")
    
    # 输出典型匹配
    print("\n[4/4] 典型五维加密匹配示例 (Top 10):")
    hit_details_sorted = sorted(hit_details, key=lambda x: x['deviation'])
    for d in hit_details_sorted[:10]:
        print(f"  {d['low_mass']:.2f} → {d['high_mass']:.2f}: "
              f"比={d['ratio']:.4f}, k={d['k_step']}, "
              f"理论={d['theory']:.4f}, 偏差={d['deviation']:.6f}")
    
    print("\n分析完成。如果图1呈现明显的五峰结构，则 D₁₂ 五维投影假设成立。")

if __name__ == "__main__":
    main()