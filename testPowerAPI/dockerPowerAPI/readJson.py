import json

jsonfile= "data.json"

def readJsonFiles(jsonfile):
	try:
		with open(jsonfile, 'r') as f:
			datas= json.load(f)
			return datas
	except FileNotFoundError:
		print("Le fichier n'existe pas")
		return None
	except json.JSONDecodeError:
		print("Le fichier n'est pas au format Json valide")
		return None

data= readJsonFiles(jsonfile)

if data:
	print(data)
