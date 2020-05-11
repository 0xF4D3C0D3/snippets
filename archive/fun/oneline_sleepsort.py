[__import__('threading').Thread(target=(lambda x:lambda:[__import__('time').sleep(x),print(x)])(n)).start()for n in map(int,input().split())]
