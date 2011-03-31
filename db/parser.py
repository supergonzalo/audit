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

f=open('datosclima.csv','r')
a=f.readlines()
choices=list()
weather=dict()
temp=dict()
for line in range(len(a)):
	b=a[line].split(';')
	choices.append((b[0],b[0]))
	gen=b[1].split(',')
	temp[gen[0]]={'LAT':gen[1],'LONG':gen[2],'ASNM':gen[3],'ZBIO':gen[4]}
        gen=b[2].split(',')
        temp[gen[0]]={'TMED':gen[1],'TMAX':gen[2],'TMIN':gen[3],'TDMD':gen[4],'TDMN':gen[5],'TROC':gen[6],'TVAP':gen[7],'HR':gen[8],'PREC':gen[9],'HELRE':gen[10],'GD18':gen[11],'GD20':gen[12],'GD22':gen[13]}
        gen=b[3].split(',')
        temp[gen[0]]={'TMAX':gen[1],'TMED':gen[2],'TMIN':gen[3],'TDMD':gen[4],'TDMX':gen[5],'TEC-MD':gen[6],'TEC-MX':gen[7],'TROC':gen[8],'TVAP':gen[9],'HR':gen[10],'PREC':gen[11],'HELRE':gen[12]}
	weather[b[0]]=temp
handl=open('loc_choices.pickle','w')
pickle.dump(choices,handl)
handl=open('weather.pickle','w')
pickle.dump(weather,handl)


