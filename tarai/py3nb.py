import numba

@numba.jit
def tarai(x,y,z):
	if x<=y: return y
	else: return tarai(tarai(0|x-1,y,z),tarai(0|y-1,z,x),tarai(0|z-1,x,y))

print(tarai(12,6,0))
