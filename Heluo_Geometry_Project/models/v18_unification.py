#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
河洛几何 v18.0 — 三种规范力的几何投影模型
核心: α₁⁻¹:α₂⁻¹:α₃⁻¹ = 1/cos²θ₁ : 1/(sin²θ₁cos²θ₂) : 1/(sin²θ₁sin²θ₂)
"""

import numpy as np
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.heluo_axioms import HeluoAxioms
from core.d12_group import D12Group
from core.rg_evolution import RGEvolution

class UnificationV18:
    """v18.0 规范力几何投影模型"""
    
    def __init__(self):
        self.alpha_geo_inv = 6.2430
        self.theta1_deg = 77.68
        self.theta2_deg = 61.65
        self.M_grid = 4080.0  # GeV
    
    def projection_factors(self):
        """计算投影因子"""
        theta1_rad = np.radians(self.theta1_deg)
        theta2_rad = np.radians(self.theta2_deg)
        
        cos2_t1 = np.cos(theta1_rad)**2
        sin2_t1 = np.sin(theta1_rad)**2
        cos2_t2 = np.cos(theta2_rad)**2
        sin2_t2 = np.sin(theta2_rad)**2
        
        return {
            'U1': cos2_t1,
            'SU2': sin2_t1 * cos2_t2,
            'SU3': sin2_t1 * sin2_t2,
        }
    
    def coupling_inverses(self):
        """计算耦合常数倒数"""
        factors = self.projection_factors()
        return {
            'alpha1_inv': self.alpha_geo_inv / factors['U1'],
            'alpha2_inv': self.alpha_geo_inv / factors['SU2'],
            'alpha3_inv': self.alpha_geo_inv / factors['SU3'],
        }
    
    def verify_with_experiment(self):
        """与实验值对比验证"""
        pred = self.coupling_inverses()
        exp = {'alpha1_inv': 137.0, 'alpha2_inv': 29.0, 'alpha3_inv': 8.45}
        
        errors = {}
        for key in pred:
            errors[key] = abs(pred[key] - exp[key]) / exp[key] * 100
        
        return pred, exp, errors
    
    def print_results(self):
        """打印结果"""
        pred, exp, errors = self.verify_with_experiment()
        
        print("=" * 70)
        print("河洛几何 v18.0 — 三种规范力的几何投影模型")
        print("=" * 70)
        print(f"\n几何基础: α_geo⁻¹ = {self.alpha_geo_inv:.4f}")
        print(f"投影角度: θ₁ = {self.theta1_deg:.2f}°, θ₂ = {self.theta2_deg:.2f}°")
        print(f"\n投影因子:")
        factors = self.projection_factors()
        for name, f in factors.items():
            print(f"  {name}: {f:.4f}")
        
        print(f"\n耦合常数对比:")
        print(f"{'力':<10} {'预测 α⁻¹':<12} {'实验 α⁻¹':<12} {'偏差':<10}")
        print("-" * 45)
        for key in pred:
            name = {'U1': '电磁', 'SU2': '弱', 'SU3': '强'}[key]
            print(f"{name:<10} {pred[key]:<12.2f} {exp[key]:<12.2f} {errors[key]:<9.2f}%")


def main():
    model = UnificationV18()
    model.print_results()
    
    # RG 演化
    print("\n" + "=" * 70)
    print("重正化群演化验证")
    print("=" * 70)
    
    M_grid = 4080
    M_susy = 8.70e5
    M_Z = 91.1876
    
    alpha_geo = [1/137.0, 1/29.0, 1/8.45]
    a1, a2, a3 = RGEvolution.evolve_sm_to_susy(alpha_geo, M_grid, M_susy, M_Z)
    
    print(f"\n在 m_Z = {M_Z} GeV 处:")
    print(f"  α₁⁻¹ (计算) = {1/a1:.1f}, 实验 = 137.0")
    print(f"  α₂⁻¹ (计算) = {1/a2:.1f}, 实验 = 29.0")
    print(f"  α₃⁻¹ (计算) = {1/a3:.1f}, 实验 = 8.45")

if __name__ == "__main__":
    main()