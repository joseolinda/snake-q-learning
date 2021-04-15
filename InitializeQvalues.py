import itertools
import json

sqs = [''.join(s) for s in list(itertools.product(*[['0','1']] * 4))]
widths = ['0','1','NA']
heights = ['2','3','NA']

states = {}
for i in widths:
	for j in heights:
		for k in sqs:
			states[str((i,j,k))] = [0,0,0,0]

with open("qvalues.json", "w") as f:
	json.dump(states, f)


game_stats = [{"game_count": 0, "score": 0, "reason": None }]
with open("game_stats.json", "w") as f:
	json.dump(game_stats, f)