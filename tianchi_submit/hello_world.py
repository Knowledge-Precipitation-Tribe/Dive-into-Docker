import sys
import json
res = {}

res['Q1'] = "Hello world"
#print("Q1-pycharm", res['Q1'])
tmp = 0

with open("./tcdata/num_list.csv" , 'r') as f:
   data = f.readlines()

num_list = [int(x.strip()) for x in data]
res_sum = sum(num_list)

#print("Q2-pycharm", res_sum)

res['Q2'] = res_sum # np.sum(res_sum)
res['Q3'] = sorted(num_list,reverse=True)[:10]
with open('result.json', 'w', encoding='utf-8') as f:
   f.write(json.dumps(res, ensure_ascii=False))
