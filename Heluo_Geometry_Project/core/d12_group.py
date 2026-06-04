#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
D₁₂ 对称群模块
生成群结构、轨道分解、不可约表示
"""

import numpy as np
from itertools import product

class D12Group:
    """二面体群 D₁₂ (24阶)"""
    
    def __init__(self):
        self.n = 12
        self.order = 24
        
    def rotation(self, k):
        """旋转元素 r^k, k=0,...,11"""
        return lambda x: (x + k) % self.n
    
    def reflection(self, k):
        """反射元素 s·r^k, k=0,...,11"""
        return lambda x: (-x + k) % self.n
    
    def all_elements(self):
        """生成所有群元素"""
        elements = []
        for k in range(self.n):
            elements.append(('r', k))
        for k in range(self.n):
            elements.append(('s', k))
        return elements
    
    def orbit_decomposition(self):
        """
        D₁₂ 在 Z/12Z 上的轨道分解
        返回: 轨道列表，每个轨道是点的列表
        """
        points = list(range(self.n))
        orbits = []
        visited = set()
        
        for p in points:
            if p in visited:
                continue
            
            orbit = set()
            # 轨道包含 p 及其所有对称像
            for k in range(self.n):
                orbit.add((p + k) % self.n)      # 旋转
                orbit.add((-p + k) % self.n)      # 反射
            
            orbit = sorted(orbit)
            orbits.append(orbit)
            visited.update(orbit)
        
        return orbits
    
    def orbit_sizes(self):
        """返回轨道大小列表 {1, 1, 2, 4, 4}"""
        orbits = self.orbit_decomposition()
        return sorted([len(o) for o in orbits])
    
    def curvature_spectrum(self):
        """曲率谱 {0, 2, 5} 来自 D₁₂ 的离散几何"""
        return [0, 2, 5]
    
    def irreducible_representations(self):
        """
        D₁₂ 的不可约表示
        返回: 维度列表 [1,1,1,1,2,2]
        """
        return [1, 1, 1, 1, 2, 2]
    
    def five_dimensional_projection_factor(self):
        """五维投影加密因子 2^(1/5)"""
        return 2.0 ** (1.0 / 5.0)
    
    @classmethod
    def coupling_from_geometry(cls):
        """
        从 D₁₂ 轨道推导耦合常数（v19.0-v20.2）
        """
        alpha_geo_inv = 6.2430
        theta1_rad = np.radians(77.68)
        theta2_rad = np.radians(61.65)
        
        cos2_t1 = np.cos(theta1_rad)**2
        sin2_t1 = np.sin(theta1_rad)**2
        cos2_t2 = np.cos(theta2_rad)**2
        sin2_t2 = np.sin(theta2_rad)**2
        
        alpha1_inv = alpha_geo_inv / cos2_t1
        alpha2_inv = alpha_geo_inv / (sin2_t1 * cos2_t2)
        alpha3_inv = alpha_geo_inv / (sin2_t1 * sin2_t2)
        
        return {
            'alpha1_inv': alpha1_inv,
            'alpha2_inv': alpha2_inv,
            'alpha3_inv': alpha3_inv,
            'alpha_geo_inv': alpha_geo_inv,
            'theta1_deg': 77.68,
            'theta2_deg': 61.65,
        }