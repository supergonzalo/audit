import pickle
f=open('Calc-g-uni.csv','r')
a=f.readlines()
mat=list()
for each in range(len(a)):
	b=a[each].split(';')
	try:
		if not b[3] == '':
			mat.append((float(b[3]),b[0].strip('"')+" k=%s"%b[3]))
	except:
		pass


handl=open('matlist.pickle','w')
pickle.dump(mat,handl)

f=open('IRAM11603_invierno.csv','r')
e=open('IRAM11603_verano.csv','r')
g=e.readlines()
a=f.readlines()
summer=g.pop(0).strip('\n').split(',')
winter=a.pop(0).strip('\n').split(',')
choices=list()
weather=dict()
for line in range(len(a)):
	invierno=dict()
	verano=dict()
	b=a[line].strip('\n').split(',')
	choices.append((b[0],b[0]))
	for each in range(len(b)):
		invierno[winter[each]]=b[each] #datos de invierno de la estacion
        b=g[line].strip('\n').split(',')
        for each in range(len(b)):
                verano[summer[each]]=b[each] #datos de verano de la estacion
	weather[b[0]]={'invierno':invierno,'verano':verano}
handl=open('loc_choices.pickle','w')
pickle.dump(choices,handl)
handl=open('weather.pickle','w')
pickle.dump(weather,handl)


