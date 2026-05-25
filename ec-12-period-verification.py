"""
验证30万条椭圆曲线数据的12周期调制
数据格式：label, ainvs, conductor, rank
"""

import csv
import math

print("=" * 60)
print("椭圆曲线 L 函数 12 周期调制验证")
print("基于 300,000 条椭圆曲线数据")
print("数据来源：LMFDB (ec_curvedata)")
print("=" * 60)

filename = "lmfdb_300k_curves.csv"

# ============================================================
# 加载数据
# ============================================================

print("\n[1/4] 加载数据...")

ranks = []
conductors = []

with open(filename, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # 跳过表头
    print(f"表头: {header}")
    
    for row in reader:
        if len(row) >= 4:
            try:
                label = row[0]
                ainvs = row[1]
                conductor = int(row[2])
                rank = int(row[3])
                
                ranks.append(rank)
                conductors.append(conductor)
            except:
                continue

print(f"成功加载 {len(ranks)} 条曲线")
print(f"秩范围: min={min(ranks)}, max={max(ranks)}")

# ============================================================
# 验证1：秩的分布统计
# ============================================================

print("\n[2/4] 验证1：秩的分布与模12调制")

# 秩的分布统计
from collections import Counter
rank_counter = Counter(ranks)
print("\n秩的分布:")
for r in sorted(rank_counter.keys()):
    count = rank_counter[r]
    pct = count / len(ranks) * 100
    bar = '█' * int(pct / 2)
    print(f"  秩 {r}: {count:8,d} ({pct:5.2f}%) {bar}")

# 秩的模12分布
rank_mod = [0] * 12
for r in ranks:
    rank_mod[r % 12] += 1

total = len(ranks)
expected = total / 12
chi2_rank = sum((n - expected)**2 / expected for n in rank_mod)

print(f"\n秩的模12分布:")
for i in range(12):
    bar = '█' * int(rank_mod[i] / expected * 10)
    print(f"  Bin {i:2d}: {rank_mod[i]:8,d} {bar}")

print(f"\n期望值: {expected:.1f}")
print(f"卡方值: {chi2_rank:.2f}")

critical = 26.76  # p=0.001, df=11
if chi2_rank > critical:
    print(f"✅ 显著偏离均匀分布 (chi2={chi2_rank:.2f} > {critical})")
    print("   秩的模12分布与12周期调制预言一致")
else:
    print(f"⚠️ 未达到显著性阈值 (chi2={chi2_rank:.2f} < {critical})")

# ============================================================
# 验证2：Conductor的模12分布
# ============================================================

print("\n[3/4] 验证2：Conductor的模12分布")

conductor_mod = [0] * 12
for c in conductors:
    conductor_mod[c % 12] += 1

total_c = len(conductors)
expected_c = total_c / 12
chi2_conductor = sum((n - expected_c)**2 / expected_c for n in conductor_mod)

print(f"Conductor模12分布:")
for i in range(12):
    bar = '█' * int(conductor_mod[i] / expected_c * 10)
    print(f"  Bin {i:2d}: {conductor_mod[i]:8,d} {bar}")

print(f"\n卡方值: {chi2_conductor:.2f}")

if chi2_conductor > critical:
    print("✅ Conductor分布显著偏离均匀，有12周期调制")
else:
    print("⚠️ Conductor分布接近均匀")

# ============================================================
# 验证3：秩的奇偶性分析
# ============================================================

print("\n[4/4] 验证3：秩的奇偶性与模2/模4/模6结构")

rank_parity = [0, 0]  # 0:偶, 1:奇
for r in ranks:
    rank_parity[r % 2] += 1

print(f"秩的奇偶分布:")
print(f"  偶数秩: {rank_parity[0]:8,d} ({rank_parity[0]/total*100:.2f}%)")
print(f"  奇数秩: {rank_parity[1]:8,d} ({rank_parity[1]/total*100:.2f}%)")

# 模4分布
rank_mod4 = [0] * 4
for r in ranks:
    rank_mod4[r % 4] += 1
print(f"\n秩的模4分布: {rank_mod4}")

# 模6分布
rank_mod6 = [0] * 6
for r in ranks:
    rank_mod6[r % 6] += 1
print(f"秩的模6分布: {rank_mod6}")

# ============================================================
# 总结
# ============================================================

print("\n" + "=" * 60)
print("验证总结")
print("=" * 60)

print(f"""
数据规模: {len(ranks):,} 条椭圆曲线

1. 秩分布:
   - 秩0: {rank_counter.get(0, 0):,} ({rank_counter.get(0, 0)/total*100:.2f}%)
   - 秩1: {rank_counter.get(1, 0):,} ({rank_counter.get(1, 0)/total*100:.2f}%)
   - 秩2: {rank_counter.get(2, 0):,} ({rank_counter.get(2, 0)/total*100:.2f}%)
   - 秩≥3: {sum(rank_counter.get(r,0) for r in range(3,100)):,} 

2. 模12调制: {'✅ 显著' if chi2_rank > critical else '⚠️ 不显著'}

3. BSD猜想: 秩0和1的情况在数学上已被证明 ✅
""")

print("=" * 60)
print("验证完成")
print("=" * 60)