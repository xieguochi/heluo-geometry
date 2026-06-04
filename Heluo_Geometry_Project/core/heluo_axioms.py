#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
河洛几何基础公理模块
包含: 单位区间 [0,1] 及其对合 σ(x)=1-x
"""

import numpy as np

class HeluoAxioms:
    """河洛几何公理系统"""
    
    @staticmethod
    def sigma(x):
        """对合映射 σ(x) = 1 - x"""
        return 1 - x
    
    @staticmethod
    def unit_interval():
        """单位区间 I = [0,1]"""
        return (0, 1)
    
    @staticmethod
    def is_involution(x):
        """验证 σ² = id"""
        return abs(HeluoAxioms.sigma(HeluoAxioms.sigma(x)) - x) < 1e-12
    
    @staticmethod
    def symmetry_principle():
        """对称性优先原则 (A3)"""
        return "几何由变换群作用下的不变量定义"
    
    @staticmethod
    def minimality_principle():
        """极小性原理 (A4)"""
        return "基本单元数、对称群阶数、不可约直和项数取最小非平凡值"
    
    @staticmethod
    def parameter_uniqueness():
        """参数唯一化 (A5)"""
        return "无自由参数，内蕴不变量唯一锁定几何结构"
    
    # 黄金数字: 来自 D₁₂ 群的不变量
    D12_ORDER = 24                    # 群阶
    D12_ORBITS = [1, 1, 2, 4, 4]      # 轨道大小
    D12_CURVATURE = [0, 2, 5]         # 曲率谱
    
    @classmethod
    def geometric_constants(cls):
        """返回所有几何不变量"""
        return {
            'mu': -0.5 * np.log(2),           # -ln(√2)
            'sigma': 1.247,                   # 实测宽度
            'M_grid': 4080.0,                 # MeV
            'D12_order': cls.D12_ORDER,
            'D12_orbits': cls.D12_ORBITS,
            'D12_curvature': cls.D12_CURVATURE,
            'alpha_geo_inv': 6.2430,          # 五维几何基础
        }
    
    @classmethod
    def projection_angles(cls):
        """五维投影角（来自 v20.2 拟合）"""
        return {
            'theta1_deg': 77.68,
            'theta2_deg': 61.65,
            'theta1_rad': np.radians(77.68),
            'theta2_rad': np.radians(61.65),
        }