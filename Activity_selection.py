from operator import itemgetter
#list with start and finish time
l=[[7,9],[2,4],[2,3],[4,6]]

def activity_sel(l):
	#sort the list
	sort_l =sorted(l,key=itemgetter(1))
	n=len(sort_l)

	l1=[]
	l1.append(sort_l[0])
	i=1
	k=0
	for j in range(1,n):
		if sort_l[k][i] <= sort_l[j][i-1]:
			l1.append(sort_l[j])
			k=j

	print(l1)


activity_sel(l)
