import sys, time, os

start = time.time()
os.system(sys.argv[1])
print(time.time() - start)
