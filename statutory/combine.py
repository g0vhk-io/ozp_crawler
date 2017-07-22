import json
output = {}
with file('output_all.json', 'r') as f:
    all_outputs = json.loads(f.read())
    first = all_outputs[0]
    all_features = list(first["features"])
    l = len(all_outputs)
    for i in range(1, l):
        features = all_outputs[i]["features"]
        all_features += features
    first["features"] = all_features
    print(len(all_features))
    output = first

with file('output_combined.json', 'w') as f:
    f.write(json.dumps(output, indent=4))
    
    
