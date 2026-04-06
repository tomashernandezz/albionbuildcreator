import json

with open("items.json", "r") as f:
    data = json.load(f)

# Aplanar capes: de capes.capes.Capes.{subcategoria: [items]} a capes.{subcategoria: [items]}
capes_nested = data["capes"]["capes"]["Capes"]
data["capes"] = capes_nested

with open("items.json", "w") as f:
    json.dump(data, f, indent=2)

print("Listo, capes aplanado correctamente")