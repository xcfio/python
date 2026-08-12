import re

string = "ed12hniuh3iuh4ou1h4ouh23u4h2o3u4huo324huo23"
p = r"\d+"

f = re.findall(p, string)
print(f"{len(f)} num found")
