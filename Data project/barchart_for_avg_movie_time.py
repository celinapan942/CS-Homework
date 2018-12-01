import pickle 
import matplotlib.pyplot as plt

avg_time = {}

with open("dictionary.pickle","wb")as f:
    pickle.dump(dictionary,f)

with open("dictionary.pickle","rb")as f:
    avg_time = pickle.load(f)
    
fig, ax = plt.subplots()
num = 0
num1 = 0
bar_width = 0.35
bar1_index = []
bar2_index = []
label_tick = []
labels = []
y_coor = []

for i in range(0, len(avg_time)):
    bar1_index += i

for i in range(0, len(avg_time)):
    num = i +0.35
    bar2_index += num
    
for i in range(0, len(avg_time)):
    num1 = i+0.18
    label_tick += num1

for i in avg_time: 
    y_coor += avg_time[i]
    
for i in avg_time:
    labels += i
    
rects1 = ax.bar(bar1_index, y_coor, bar_width, color = "b", label = "")

ax.set_xlabel("Year")
ax.set_ylabel("Average length of movies")
ax.set_title("The average length of all movies in a year")
ax.set_xticks(label_tick)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()
plt.show()
    

    

