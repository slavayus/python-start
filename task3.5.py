import csv
import json
from collections import Counter


def fun():
    with open('Crimes.csv') as f:
        reader = csv.DictReader(f)
        print(Counter([row['Date'][6:10] + row['Primary Type'] for row in reader if row['Date'][6:10] == '2015'])
              .most_common(3))


inp = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
loads = json.loads(input())

classes = {load['name']: load['parents'] for load in loads}

search_list = []

parents = dict()


def search_super_clas(clas):
    if len(search_list) == 0:
        return
    cur_class = search_list.pop()
    parents[clas] = parents[clas].union(set(classes[cur_class])) if clas in parents else set(classes[cur_class])
    search_list.extend(classes[cur_class])
    search_super_clas(clas)


for clas in classes:
    search_list = [clas]
    search_super_clas(clas)

for clas in sorted(classes):
    print('%s : %d' % (clas, sum(clas in v for v in parents.values()) + 1))
