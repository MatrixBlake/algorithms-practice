
# – Input: Set of n jobs. Each job i starts at time sj and finishes at time fj.
# – Two jobs are compatible if they don't overlap in time.
# – Goal: find maximum subset of mutually compatible jobs.

A=[0,6]
B=[1,4]
C=[3,5]
D=[3,8]
E=[4,7]
F=[5,9]
G=[6,10]
H=[8,11]
original_list=[A,B,C,D,E,F,G,H]


def sort(o_list):
	for i in range(len(o_list)):
		min_value=o_list[i][1]
		min_index=i
		for j in range(i,len(o_list)):
			if(o_list[j][1]<min_value):
				min_value=o_list[j][1]
				min_index=j
		a=o_list[i]
		o_list[i]=o_list[min_index]
		o_list[min_index]=a
	return o_list

sorted_list=sort(original_list)

print(sorted_list)

output_list=[sorted_list[0]]
finish=sorted_list[0][1]
for i in range(1,len(sorted_list)):
	if(sorted_list[i][0]>=finish):
		output_list.append(sorted_list[i])
		finish=sorted_list[i][1]

print(output_list)