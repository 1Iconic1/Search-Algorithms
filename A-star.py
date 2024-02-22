map_size=[10,12]
def astar_search(map):
	found = False
	for y in range(0,map_size[1]):
		for x in range(0,map_size[0]):
			if map[y][x] ==2:
				start= (y,x)
			if map[y][x] == 3:
				goal = (y,x)

	mov= [(-1,0),(0,-1),(1,0),(0,1)]
	parent={}
	cost={}
	queue=  []
	queue.append((abs((start[0]-goal[0]))+abs((start[1]-goal[1])),start[1],start[0]))
	while queue:
		ft= sorted(queue)
		z,x,y=  ft.pop(0)
		queue.remove((z,x,y))
		map[y][x]=4
		if y ==  goal[0] and x ==goal[1]:
			backtrack=[(y,x)]
			while backtrack[-1] != (start[0],start[1]):
				backtrack.append(parent[backtrack[-1]][0])
			for path in backtrack:
				map[path[0]][path[1]]=5
			found= True
			break
		bc=[(y,x)]
		count=0
		while bc[-1] != (start[0],start[1]):
				bc.append(parent[bc[-1]][0])
		for path in bc:
			count+=1
		for coord in mov:
			while  0 <= y + coord[0] < map_size[1] and 0<= x + coord[1] < map_size[0] and map[y + coord[0]][x+ coord[1]] != 1:
				Y= coord[0] +y
				X =coord[1] +x
				cost[(Y,X)]= abs(Y-goal[0])+abs(X-goal[1])
				if (Y,X) not in parent.keys():
					parent[(Y,X)]=list()
					parent[(Y,X)].append((y,x))
				else:
					parent[(Y,X)].append((y,x))
				if map[Y][X] !=4:
					queue.append((cost[(Y,X)]+count,X,Y))	
				break
	return found
