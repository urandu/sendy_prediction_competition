import pandas as pd
train_data = pd.read_csv('Train.csv')
print(train_data.head()[:6])

import matplotlib.pyplot as plt
# %%matplotlib
# %matplotlib inline

fig, ax = plt.subplots()
ax.scatter(train_data['Distance (KM)'], train_data['Time from Pickup to Arrival'])
ax.set_title('Time from pick up to arrival')
ax.set_xlabel('Distance KM')
ax.set_ylabel('Time from pick up to arrival')
