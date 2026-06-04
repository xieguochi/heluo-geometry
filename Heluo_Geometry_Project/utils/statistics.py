#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统计工具模块
正态性检验、对数正态分布拟合、熵计算
"""

import numpy as np
from scipy import stats

class StatisticsUtils:
    """统计检验工具"""
    
    @staticmethod
    def shapiro_test(data):
        """Shapiro-Wilk 正态性检验"""
        if len(data) > 5000:
            sample = np.random.choice(data, 5000, replace=False)
        else:
            sample = data
        return stats.shapiro(sample)
    
    @staticmethod
    def ks_test(data, dist='norm', params=None):
        """Kolmogorov-Smirnov 检验"""
        if params is None:
            mu, sigma = np.mean(data), np.std(data)
        else:
            mu, sigma = params
        return stats.kstest(data, dist, args=(mu, sigma))
    
    @staticmethod
    def lognormal_fit(data):
        """拟合对数正态分布"""
        log_data = np.log(data)
        mu = np.mean(log_data)
        sigma = np.std(log_data)
        return mu, sigma
    
    @staticmethod
    def shannon_entropy(data, bins=50):
        """计算香农熵"""
        hist, _ = np.histogram(data, bins=bins, density=True)
        hist = hist[hist > 0]
        if len(hist) == 0:
            return 0
        bin_width = (data.max() - data.min()) / bins
        return -np.sum(hist * np.log(hist)) * bin_width
    
    @staticmethod
    def boltzmann_inversion(phi_samples, bins=80):
        """
        玻尔兹曼反演: V(φ) ∝ -ln P(φ)
        从样本分布反推势能函数
        """
        hist, bin_edges = np.histogram(phi_samples, bins=bins, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
        hist_safe = np.maximum(hist, 1e-8)
        potential = -np.log(hist_safe)
        potential = potential - np.min(potential)
        return bin_centers, potential