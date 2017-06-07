import yaml

with open("settlement.yaml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

print(section)
print(cfg['metropolis'])
