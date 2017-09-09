#Implementation of insertion sort, courtesy CLRS

import subprocess

def InsertionSort(arr):
	key=0
	for i in range(1,len(arr)):
		key=arr[i]
		j=i-1
		while(j>=0 and arr[j]>key):
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key

	return arr

subprocess.run("clear",shell=True)
arr=list(map(int,input("Enter your array : ").strip().split()))
s_arr=InsertionSort(arr)
print(arr)
