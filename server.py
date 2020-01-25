import socket
#from _thread import *
#import threading
from threading import Thread 

def rpc_sub(*all):
    args= list(all)
    diff= args[0]
    
    for i in range (1, len(args)):
        diff -= args[i]
        
    return diff

def rpc_multiply(*all):
    args= list(all)
    sum= args[0]
    
    for i in range (1, len(args)):
        sum *= args[i]
        
    return sum

#process the required function names and their types to call the function defined in server
def process_string(line):
    list= line.split(':')
#    print (list)
    func= str(list[0]) +"("
#    print (func_name)
    
    for i in range (1, len(list)):
        l= str(list[i]).split('\'')
#        print (l)
        d_type= str(l[1])
#        print (d_type)
        func += d_type +"("
        l= str(l[2]).split('-')
#        print (l)
        value= str(l[1])
        func += value + "),"
#        print (value)
#        print()
    
    func = func[:-1]
    func += ")"          
    result= eval(func)
    print (result)
    print()
    return result

class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
#        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        from_client = ''
        while True : 
            data = conn.recv(4096).decode()
            if not data: 
                break
            from_client += data
            result= process_string(from_client)
#        print (from_client)
            conn.send(str(result).encode())
        conn.close()  # echo 

#main (creating connection to clients and sending recieving required results)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
threads= []
while True:
    conn, addr = serv.accept()
    newThread= ClientThread(conn, addr)
    newThread.start()
    threads.append(newThread) 

#    start_new_thread(client_fn, (conn, addr))
#for t in threads: 
#    t.join()    
conn.close()
print ('client disconnected')