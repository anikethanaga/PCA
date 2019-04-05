import numpy as np
import math

def Normalize(M):
	m = M.shape[0]
	n = M.shape[1]
	'''calc Mean and subtract'''
	for i in range(n):
		total = 0.0
		for j in range(m):
			total += M[j][i]
		avg = total/m
		total = 0.0

		for j in range(n):
			M[j][i] -= avg
			total += M[j][i]*M[j][i]

		#print(M)
		total = (float)(total/m)
		std = math.sqrt(total)
		'''print("Variance is ",total)
		print("std is : ",std)'''

		for j in range(m):
			M[j][i] = (float)(M[j][i]/std)
		#print(M)

	return M



def main():
	M = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
	#print(M)
	M = Normalize(M)
	print(M)

if __name__=='__main__':
	main()
