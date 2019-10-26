import json

with open('squad.json') as json_file:
	data = json.load(json_file)
datas = data['data']

# datas[0]
#   |--paragraphs---(index)
#	|					|--context
#	|					|--qas---(index)
#	|					|			|--question
#	|					|			|--answer--text
#	|					|--id
#   |--section_title
#   |--background
#   |--title

vec = [[0 for i in range(0,100)] for j in range(100)]

for i in datas:
	for j in i['paragraphs']:
		for k in j['qas']:
			ques = k['question']
			ans = k['answer']['text']
			vec[len(ques)][(ans)] += 1

print(vec)
