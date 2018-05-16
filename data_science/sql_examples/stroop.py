import sqlite3 
import matplotlib.pyplot as plt
db = sqlite3.connect('stroop_data.db')

cur = db.cursor()
cur.execute('SELECT congruency, rt FROM data')
data = cur.fetchall()

congruent = 0
incongruent = 0
rt_con = []
rt_incon = []

for i in range(0,len(data)):
    if data[i][0] == 'I':
        rt_incon.append(data[i][1])
        incongruent += 1
    elif data[i][0] == 'C':
        rt_con.append(data[i][1])
        congruent += 1

con_hist = sum(rt_con)/len(rt_con)
incon_hist = sum(rt_incon)/len(rt_incon)

xvalues = [1,2]
labels = [' ',' ']
plt.xticks(xvalues, labels)
plt.axis([1,2,500,640])
plt.bar(xvalues[0], con_hist, align='center', width=1,color='purple',label='Congruent')
plt.bar(xvalues[1], incon_hist, align='center',width=1,color='pink', label='Incongruent')
plt.legend()
plt.ylabel("Reaction Time (ms)")
plt.show()
db.close()

print((con_hist, incon_hist))
