import pandas as pd
from ta.volume import VolumeWeightedAveragePrice

# PTA合约乘数5
multiplier = 5

df = pd.read_csv('dataset/CZCE.TA209_1m_kline_2022-06-21 13:55:00-2022-07-22 14:59:00.csv')
df.drop(columns=['id', 'datetime', 'open_oi', 'close_oi', 'symbol', 'duration'], inplace=True)

# 每分钟交易资金=vwap * volume * 合约乘数
# vwap参考ta.volume.VolumeWeightedAveragePrice，=(close+high+low)/3*volume
df['money'] = (df[['close', 'high', 'low']].mean(axis=1) * df['volume'] * multiplier).round(decimals=0)
df = df.rename(columns={"dt": "date"})
df = df.set_index(df['date'])
df = df.drop(columns=['date'])
df.to_csv('dataset/PTA1分钟历史数据.csv')
