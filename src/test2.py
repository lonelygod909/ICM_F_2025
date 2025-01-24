import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import pairwise_distances

# 假设数据：县、年、阿片类药物使用情况
# 假设有五个县的数据，每个县有2010到2017年的数据
data = {
    'county': ['County A', 'County B', 'County C', 'County D', 'County E'],
    '2010': [500, 800, 200, 300, 100],
    '2011': [550, 850, 220, 330, 110],
    '2012': [600, 900, 250, 360, 120],
    '2013': [650, 950, 280, 380, 130],
    '2014': [700, 1000, 300, 400, 140],
    '2015': [750, 1050, 320, 430, 150],
    '2016': [800, 1100, 350, 460, 160],
    '2017': [850, 1150, 380, 490, 170],
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 假设我们使用2010到2016年的数据来预测2017年的数据
X = df.drop(columns=['county'])  # 去掉县名列
y = df['2017']  # 目标是2017年的药物使用数据

# 使用KNN模型进行预测
knn = KNeighborsRegressor(n_neighbors=3)  # 使用k=3的邻居
knn.fit(X.iloc[:, :-1], y)  # 使用2010到2016年的数据来拟合模型

# 使用模型预测每个县2017年的阿片类药物使用情况
y_pred = knn.predict(X.iloc[:, :-1])

# 可视化结果：实际值与预测值
plt.figure(figsize=(10, 6))
plt.bar(df['county'], y, alpha=0.7, label='Actual')  # 实际值
plt.bar(df['county'], y_pred, alpha=0.7, label='Predicted')  # 预测值
plt.title('Comparison of Actual and Predicted Opioid Usage (2017)', fontsize=14)
plt.xlabel('County')
plt.ylabel('Opioid Usage')
plt.legend()
plt.show()

# 模拟未来的阿片类药物传播（基于模型的增长率）
growth_rates = knn.predict(X.iloc[:, :-1]) / X['2016']  # 根据2016年的数据计算增长率
future_years = [2018, 2019, 2020]

# 预测未来几年的药物使用
future_predictions = pd.DataFrame(columns=['County', *future_years])
future_predictions['County'] = df['county']

for i, county in enumerate(df['county']):
    county_data = df.iloc[i, 1:]  # 获取该县2010到2017年的数据
    for year in future_years:
        future_predictions.at[i, year] = county_data.iloc[-1] * (1 + growth_rates[i]) ** (year - 2017)

# 可视化未来的阿片类药物使用预测
plt.figure(figsize=(10, 6))
for i, county in enumerate(future_predictions['County']):
    plt.plot(future_years, future_predictions.iloc[i, 1:], label=county)

plt.title('Predicted Opioid Usage for Future Years', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Opioid Usage')
plt.legend()
plt.show()

