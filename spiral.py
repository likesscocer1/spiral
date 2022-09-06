
size = 16


def spiral(size):
	listas = [[],[],[],[]]
	coordinates = [2,0]
	right = True
	up = False
	left = False
	down = False

	count = 0
	time_to_move = 1

	for i in range(1, size+1):
		
		if right:
			listas[coordinates[0]].append(i)

			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])
			

			if i != 1:
				count += 1
			if count == time_to_move:
				right = False
				up = True
				count = 0
				continue

		if up:
			coordinates[0] -=1
			listas[coordinates[0]].append(i)

			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])

			count += 1
			if count == time_to_move:
				up = False
				left = True
				count = 0
				time_to_move += 1
				continue
		if left:
			listas[coordinates[0]].insert(0,i)

			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])

			count += 1
			if count == time_to_move:
				left = False
				down = True
				count = 0
				continue

		if down:
			coordinates[0] +=1
			listas[coordinates[0]].insert(0,i)

			if len(listas[coordinates[0]]) > len(listas):
				listas.append([])

			count += 1
			if count == time_to_move:
				down = False
				right = True
				count = 0
				time_to_move +=1
				continue

	return listas
	

for i in spiral(size):
	for j in i:
		print(str(j).rjust(2), end=' ')
	print()