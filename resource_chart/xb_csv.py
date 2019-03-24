from matplotlib import pyplot as plt
import csv
import MySQLdb

with open("xb_origin.csv", encoding="utf-8") as csvfile:
    xb = list(csv.DictReader(csvfile))

print(xb[0].keys()) #把key全部取出来
print(len(xb)) #共1000条数据

#取width和height,各column为list
width_measure = [int(w["width"]) for w in xb]
height_measure = [int(h["height"]) for h in xb ]
# labels = [int(d["id"]) for d in xb]

plt.scatter(width_measure,height_measure)

#label 打标记
# for label width_count, height_count in zip(width_measure,height_measure):
#     plt.annotate(label,xy=(width_count,height_count),xytext=(5,-5),textcoords="offset points")

plt.title("store measure")
plt.xlabel("width")
plt.ylabel("height")
plt.show()
