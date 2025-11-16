import pickle
import base64

with open('data/ann_10_params.csv', 'r') as f:
    line = f.readline().strip()

parts = line.split(',')
print('CSV format: id, avg_score, pstdev, best_score, encoded_weights')
print('First row values:', parts[0:4])

player_data = pickle.loads(base64.b64decode(parts[4]))
print('Player data keys:', list(player_data.keys()))
print('Num features:', player_data['num_features'])
print('Num hidden:', player_data['num_hidden'])
print('Weights type/len:', type(player_data['weights']), len(player_data['weights']))

# Look at a few weights to understand structure
weights = player_data['weights']
print('First 10 weights:', weights[:10])
print('Last 10 weights:', weights[-10:])

# Count lines in file to understand population size
with open('data/ann_10_params.csv', 'r') as f:
    lines = f.readlines()
print('Total individuals in population:', len(lines))

# Check the best performer (highest score in column 1)
scores = []
for line in lines:
    parts = line.strip().split(',')
    scores.append(float(parts[1]))  # avg_score column

best_idx = scores.index(max(scores))
print('Best performer index:', best_idx)
print('Best score:', max(scores))
print('Score range:', min(scores), 'to', max(scores))