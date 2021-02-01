import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
import seaborn as sns

df = pd.read_csv('Sample_Game_1_RawEventsData.csv')

df['XSTART '] = df['XSTART'] * 120
df['YSTART'] = df['YSTART']*80
df['XEND'] = df['XEND']*120
df['YEND'] = df['YEND']*80

df = df[df['Type']=='PASS']
data = df[df['Team']=='Home']
print(data)

fig, ax = plt.subplots()
fig.set_size_inches(7, 5)

for i in range(len(data)):
    plt.plot([(data['XSTART'][i]),(data['XEND'][i])],
             [(data['YSTART'][i]),(data['YEND'][i])],
             color="blue")
plt.show()









