import json
f=open("items.json",)
data=json.load(f)



def index(request):
	for i in data["items"]:
		l1.append(i)

	print(l1)

index(1)
