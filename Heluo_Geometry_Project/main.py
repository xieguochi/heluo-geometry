#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
河洛几何项目主入口
一键运行三个核心版本: v7.0 (骨架扫描), v18.0 (规范力统一), v20.2 (引力嵌入)
"""

import sys
import os

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.v7_skeleton_scan import main as v7_main
from models.v18_unification import main as v18_main
from models.v20_gravity_embed import main as v20_main

def print_banner():
    print("=" * 70)
    print("   河洛几何 — 从离散对称性到基本相互作用的几何统一")
    print("   版本: v7.0 | v18.0 | v20.2")
    print("   作者: 承曦 (承曦国学苑)")
    print("=" * 70)

def main():
    print_banner()
    
    print("\n请选择要运行的版本:")
    print("  1. v7.0 - 五维投影与 D₁₂ 对称性扫描 (粒子质量比 2^(k/5) 验证)")
    print("  2. v18.0 - 三种规范力的几何投影模型 (α₁⁻¹:α₂⁻¹:α₃⁻¹)")
    print("  3. v20.2 - 引力嵌入与大统一模型 (四种基本力的统一)")
    print("  4. 运行全部版本")
    
    choice = input("\n请输入选项 (1/2/3/4): ").strip()
    
    if choice == '1':
        v7_main()
    elif choice == '2':
        v18_main()
    elif choice == '3':
        v20_main()
    elif choice == '4':
        print("\n" + "=" * 70)
        print("运行 v7.0...")
        v7_main()
        print("\n" + "=" * 70)
        print("运行 v18.0...")
        v18_main()
        print("\n" + "=" * 70)
        print("运行 v20.2...")
        v20_main()
    else:
        print("无效选项，退出。")

if __name__ == "__main__":
    main()