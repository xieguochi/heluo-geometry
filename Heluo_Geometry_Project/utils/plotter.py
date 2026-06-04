#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一绘图模块
生成 RG 演化图、投影示意图、质量谱分布图
"""

import numpy as np
import matplotlib.pyplot as plt

class HeluoPlotter:
    """河洛几何统一绘图工具"""
    
    @staticmethod
    def set_style():
        """设置绘图风格"""
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
    
    @staticmethod
    def plot_projection_angles(theta1_deg, theta2_deg, save_path='projection_angles.png'):
        """绘制五维投影角示意图"""
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_aspect('equal')
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        
        # 单位圆
        phi = np.linspace(0, 2*np.pi, 100)
        ax.plot(np.cos(phi), np.sin(phi), 'b-', alpha=0.3)
        
        theta1_rad = np.radians(theta1_deg)
        theta2_rad = np.radians(theta2_deg)
        
        # 投影向量
        ax.arrow(0, 0, 1, 0, head_width=0.05, head_length=0.05, fc='blue', ec='blue', label='电磁 U(1)')
        ax.arrow(0, 0, np.sin(theta1_rad)*np.cos(theta2_rad), 
                 np.sin(theta1_rad)*np.sin(theta2_rad), 
                 head_width=0.05, head_length=0.05, fc='red', ec='red', label='弱 SU(2)')
        ax.arrow(0, 0, np.sin(theta1_rad), 0, 
                 head_width=0.05, head_length=0.05, fc='green', ec='green', label='强 SU(3)')
        
        ax.set_title(f'五维几何投影角: θ₁={theta1_deg:.1f}°, θ₂={theta2_deg:.1f}°')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
    
    @staticmethod
    def plot_coupling_evolution(E_range, a1, a2, a3, M_grid, M_susy, M_gut, save_path='coupling_evolution.png'):
        """绘制耦合常数随能标演化图"""
        fig, ax = plt.subplots(figsize=(10, 6))
        
        ax.semilogx(E_range, a1, 'b-', lw=2, label='U(1) 电磁')
        ax.semilogx(E_range, a2, 'g--', lw=2, label='SU(2) 弱')
        ax.semilogx(E_range, a3, 'r-.', lw=2, label='SU(3) 强')
        ax.axvline(x=M_grid, color='purple', linestyle=':', alpha=0.7, label=f'M_grid = {M_grid:.0f} GeV')
        ax.axvline(x=M_susy, color='orange', linestyle='--', alpha=0.7, label=f'M_SUSY = {M_susy:.1e} GeV')
        ax.axvline(x=M_gut, color='k', linestyle='--', alpha=0.7, label=f'E_GUT = {M_gut:.1e} GeV')
        
        ax.set_xlabel('能量 E (GeV)')
        ax.set_ylabel('α⁻¹')
        ax.set_title('耦合常数随能标演化')
        ax.legend()
        ax.grid(True, alpha=0.3)
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
    
    @staticmethod
    def plot_phase_space(phi_samples, mu, sigma, save_path='phase_space.png'):
        """绘制希格斯连续谱的相空间分布"""
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        
        # 直方图 + 正态拟合
        axes[0].hist(phi_samples, bins=50, density=True, alpha=0.6, color='steelblue')
        x = np.linspace(phi_samples.min(), phi_samples.max(), 200)
        axes[0].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', lw=2, label=f'N({mu:.3f}, {sigma:.3f}²)')
        axes[0].set_xlabel('φ = ln(M_phys/M_grid)')
        axes[0].set_ylabel('概率密度')
        axes[0].set_title('希格斯连续谱: φ 分布')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Q-Q 图
        from scipy import stats
        stats.probplot(phi_samples, dist="norm", plot=axes[1])
        axes[1].set_title('Q-Q 图: 正态性检验')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()