# your code goes here

# matrux - m
def old_func():
	def current_box(i,j):
		if i in range(0,3):
			rl,ru = 0,3
		elif i in range(3,6):
			rl,ru = 3,6
		else:
			rl,ru = 6,9
		return

	def fill_mat(mat):
		pos={}
		for i in range(0,9):
			for j in range(0,9):
				pos[(i,j)] = set()
		count = 0 
		while pos != {} and count < 2000:
			for i in range(0,9):
				for j in range(0,9):
					
					if mat[i][j] is None:
						val = check_vals(mat,i,j)
						print("for ==",i," ",j,"   vals=",val)
						if len(val)==1:
							mat[i][j] = val[0]
							print("Updateing ",i," ",j," to ",val[0])
							if pos.get((i,j)) is not None:
								pos[(i,j)]
						elif len(val)>1:
							if pos.get((i,j)) is None:
								pos[(i,j)] = set()
							for v in val:
								pos[(i,j)].add(v)
					elif pos.get((i,j)) is not None:
						del pos[(i,j)]
			count+=1
		
		if count == 2000:
			print("too Many Tries.....")
		return mat

	def check_vals(arr,i,j):
		val_list = [1,2,3,4,5,6,7,8,9]
		for l in range(i,9):
			if arr[i][j] in val_list:
				val_list.remove(arr[i][j])
		for l in range(j,9):
			if arr[i][j] in val_list:
				val_list.remove(arr[i][j])
				
		# to check in current box
		if i in range(0,3):
			rl,ru = 0,3
		elif i in range(3,6):
			rl,ru = 3,6
		else:
			rl,ru = 6,9
		
		for l in range(rl,ru):
			for q in range(rl,ru):
				if arr[l][q] in val_list:
					val_list.remove(arr[l][q])
		return val_list

	mat =[ [None,4,5,8,7,None,9,None,None],
			[None,None,None,9,None,None,None,None,None],
			[2,None,8,None,6,None,None,None,None],
			[None,1,None,2,None,None,4,None,None],
			[9,3,None,5,4,7,2,None,None],
			[None,None,4,6,9,None,7,None,3],
			[None,6,None,4,8,None,None,3,1],
			[3,8,None,7,None,2,6,None,9],
			[None,None,None,None,None,6,None,2,7]
		]

	# mat = fill_mat(mat)
	# print(mat)





# ################################################################

def common_member(a, b):
    result = [i for i in a if i in b]
    return result

def get_unfilled(mat,n):
	count = 0
	for i in range(n):
		for j in range(n):
			if mat[i][j] == 0:
				count+=1
	return count

def get_range(i):
	if i in range(0,3):
		return (0,3)
	elif i in range(3,6):
		return (3,6)
	elif i in range(6,9):
		return (6,9)

def get_all_options(mat,i,j,n,check=True):
	default = list(range(1,n+1))
	# check vertical row
	for vrows in range(0,n):
		if mat[i][vrows] in default:
			default.remove(mat[i][vrows])

	# check horizontal row
	for hrows in range(0,n):
		if mat[hrows][j] in default:
			default.remove(mat[hrows][j])

	# check current box
	ir = get_range(i)
	jr = get_range(j)
	for p in range(ir[0],ir[1]):
		for q in range(jr[0],jr[1]):
			if mat[p][q] in default:
				default.remove(mat[p][q])
	# print("default now===",default, "check", check)
	if len(default) == 1:
		return default[0]
	else:
		if check == False:
			return default
		# check for all non acceptance for each no in default in current box & where  they can be placed
		# get all acceptable palces for each elemnt in default
		el_count = 0
		while el_count<len(default):
			el = default[el_count]
			if len(default) == 1:
				break
			# print("fopr ellllll=============== ",el)
			for p in range(ir[0],ir[1]):
				for q in range(jr[0],jr[1]):
					# print("for p=",p," q=",q," mat=",mat[p][q],"default==",default)
					if mat[p][q] == 0 and (p!=i or q!=j):
						# get all options for p,q th element
						value = get_all_options(mat,p,q,n,check=False)
						print("for p=",p," q=",q," values=",value," type=",type(value))
						if value !="NA":
							if type(value)!= list:
								value = [value]
							if el in value:
								# get common membs
								comm = common_member(default,value)
								default = list(filter(lambda i: i not in value, default))
								if default is None:
									print("default here====",default)
								el_count = 0

					# print("default==",default)
			el_count +=1
		print("here   default==",default)
		if len(default) == 1:
			return default[0]
		else:
			return "NA"

def fill_sudoku(mat,n):
	unfilled = get_unfilled(mat,n)
	while unfilled != 0:
		print("New Looppppppppppppppppppppppppppppppppppppppppppppppppppp")
		for i in range(n):
			for j in range(n):
				print("for i=",i,"j=",j," unfilles=============================",unfilled)
				if mat[i][j] == 0 :
					value = get_all_options(mat,i,j,n)
					print("value===",value)
					if value != "NA":
						mat[i][j] = value
						unfilled -=1
				print("mat===",mat)
			# return
		# return
	print("FINAL mat===",mat)
			

mat =[  [0,0,0,2,7,0,0,9,0],
		[0,9,0,4,0,5,8,1,7],
		[0,0,3,0,0,0,0,0,5],
		[0,0,0,7,0,9,1,2,3],
		[0,0,4,0,1,2,0,8,0],
		[1,0,0,3,5,0,0,4,0],
		[6,5,0,1,0,0,4,0,0],
		[0,3,2,0,6,7,9,0,1],
		[9,1,0,0,0,0,0,3,8]
	]

# mat = [
# 	[0,0,6,2,0,0,0,0,5],
# 	[0,0,0,4,0,0,3,0,0],
# 	[2,0,0,0,0,3,0,1,0],
# 	[0,2,0,3,0,0,0,0,0],
# 	[7,0,3,0,0,0,0,4,9],
# 	[0,1,0,9,0,2,7,0,8],
# 	[0,3,0,6,4,0,0,0,0],
# 	[0,0,2,5,0,0,0,9,0],
# 	[5,0,9,0,0,0,1,0,0]

# ]
fill_sudoku(mat,9)

		
		