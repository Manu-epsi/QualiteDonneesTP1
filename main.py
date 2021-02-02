# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pandas
import matplotlib.pyplot as plt
import numpy as np
import cursor as cursor


# ---------------------------------------------------
# SI
# ---------------------------------------------------
df = pandas.read_excel('datas/Climat.xlsx', 'SI', 2, usecols="D:O")
print(df)
moyennes=df.mean()
et = df.std()
minMois = df.min()
maxMois = df.max()
minAnnee = df.min(axis = 1)
maxAnnee = df.max(axis = 1)
plt.plot(minMois)
plt.plot(maxMois)
plt.plot(minAnnee)
plt.plot(maxAnnee)
d = {'mois': [], 'jour': [], 'temperature': []}
for (columnName, columnData) in df.iteritems():
    print('Column Name : ', columnName)
    print('Column Contents : ', columnData.values)
    i = 0
    for value in columnData.values:
        if not np.isnan(value):
            d['mois'].append(columnName)
            d['jour'].append(i)
            d['temperature'].append(value)
        i += 1

dfyear = pandas.DataFrame(data=d)
ax = dfyear.plot(x="mois", y="temperature")

cursor1 = cursor.SnaptoCursor(ax, 365, 20)
cid = plt.connect('motion_notify_event', cursor1.mouse_move)


# ---------------------------------------------------
# SI -erreur
# ---------------------------------------------------
df2 = pandas.read_excel('datas/Climat.xlsx', 'SI -erreur', 2, usecols="D:O")

d2 = {'mois': [], 'jour': [], 'temperature': []}
for (columnName, columnData) in df2.iteritems():
    i2 = 0
    lastvalue = 0
    for value in columnData.values:
        if (not type(value) == str) and (not np.isnan(value)):
            if (not (value > lastvalue+15)) and (not (value < lastvalue-15)):
                d2['mois'].append(columnName)
                d2['jour'].append(i2)
                d2['temperature'].append(value)

            lastvalue = value
        i2 += 1

df2year = pandas.DataFrame(data=d2)
ax2 = df2year.plot(x="mois", y="temperature")
cursor2 = cursor.SnaptoCursor(ax2, 365, 35)
cid2 = plt.connect('motion_notify_event', cursor2.mouse_move)

plt.show()