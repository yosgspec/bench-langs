import numba
from concurrent import futures

cores=4
maxsum=2000000000
maxsum=int(maxsum/cores)

def main():
	with futures.ThreadPoolExecutor() as TP:
		sum=0
		@numba.jit
		def myFuture():
			global maxsum
			esum=0
			for i in range(maxsum):
				esum+=1
			return esum
		myFutures=[TP.submit(myFuture) for i in range(cores)]
		for esum in futures.wait(myFutures)[0]:
			sum+=esum.result()
		print(sum)

if __name__=="__main__": main()
