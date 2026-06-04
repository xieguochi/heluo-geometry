#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
重正化群演化模块
单圈/两圈 β 函数，标准模型/超对称系数
"""

import numpy as np

class RGEvolution:
    """重正化群演化方程"""
    
    # 标准模型单圈 β 系数
    SM_BETA = {
        'b1': 41/10,    # U(1)
        'b2': -19/6,    # SU(2)
        'b3': -7,       # SU(3)
    }
    
    # 超对称单圈 β 系数
    SUSY_BETA = {
        'b1': 33/5,     # U(1)
        'b2': 1,        # SU(2)
        'b3': -3,       # SU(3)
    }
    
    @staticmethod
    def alpha_inv_1loop(alpha_inv0, b, E0, E1):
        """
        单圈 RG 演化（α⁻¹ 形式）
        α⁻¹(E1) = α⁻¹(E0) + b/(2π) * ln(E1/E0)
        """
        if E1 <= 0 or E0 <= 0:
            return alpha_inv0
        return alpha_inv0 + b / (2 * np.pi) * np.log(E1 / E0)
    
    @staticmethod
    def alpha_1loop(alpha0, b, E0, E1):
        """
        单圈 RG 演化（α 形式）
        α(E1) = α0 / (1 + α0 * b/(2π) * ln(E1/E0))
        """
        if alpha0 <= 0 or E1 <= 0:
            return alpha0
        denominator = 1 + alpha0 * b / (2 * np.pi) * np.log(E1 / E0)
        if denominator <= 0:
            return alpha0 * 0.5
        return alpha0 / denominator
    
    @classmethod
    def evolve_sm_to_susy(cls, alpha_inv, E_start, E_susy, M_Z=91.1876):
        """
        从高能标演化到 m_Z，考虑标准模型和超对称区域
        """
        # 第一阶段: E_start → E_susy (标准模型)
        a1_susy = cls.alpha_inv_1loop(alpha_inv[0], cls.SM_BETA['b1'], E_start, E_susy)
        a2_susy = cls.alpha_inv_1loop(alpha_inv[1], cls.SM_BETA['b2'], E_start, E_susy)
        a3_susy = cls.alpha_inv_1loop(alpha_inv[2], cls.SM_BETA['b3'], E_start, E_susy)
        
        # 第二阶段: E_susy → M_Z (超对称)
        a1_z = cls.alpha_inv_1loop(a1_susy, cls.SUSY_BETA['b1'], E_susy, M_Z)
        a2_z = cls.alpha_inv_1loop(a2_susy, cls.SUSY_BETA['b2'], E_susy, M_Z)
        a3_z = cls.alpha_inv_1loop(a3_susy, cls.SUSY_BETA['b3'], E_susy, M_Z)
        
        return a1_z, a2_z, a3_z
    
    @classmethod
    def find_unification_scale(cls, alpha_geo, M_grid=4080):
        """寻找耦合常数汇聚的统一能标"""
        from scipy.optimize import minimize_scalar
        
        def diff(logE):
            E = 10**logE
            a2 = cls.alpha_1loop(alpha_geo[1], cls.SM_BETA['b2'], M_grid, E)
            a3 = cls.alpha_1loop(alpha_geo[2], cls.SM_BETA['b3'], M_grid, E)
            return abs(a2 - a3)
        
        result = minimize_scalar(diff, bounds=(3, 12), method='bounded')
        return 10**result.x