# #multiprocessing:
# #WHEN WE WAnt to run multipleprocess at the same time.its little bit from threading.

# import multiprocessing

# def CalcSquare(n,lock):      #to calculate the square
#     result=[]
#     for i in n:
#         s=i*i
#         result.append(s)
#     with lock:
#         print(result)   

# def calcCube(n,lock):            #to calculate the cube
#     result=[]
#     for i in n:
#         s=i*i*i
#         result.append(s)
#     with lock:
#         print(result)
# if __name__=="__main__":
#     lock=multiprocessing.Lock()
#     l=[12,13,15,17,19]

#     p1=multiprocessing.Process(target=CalcSquare,args=(l,lock))
#     p2=multiprocessing.Process(target=calcCube,args=(l,lock))
        

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()


#by using multiprcoessing find the even and odd number from the list..
import multiprocessing

def Checkeven(n,lock):
    even=[]
    for i in n:
        if i%2==0:
            even.append(i)
    with lock:
        print(even)

def CheckOdd(n,lock):
    odd=[]
    for i in n:
        if i%2 !=0:
            odd.append(i)
    with lock:
        print(odd)
if __name__ == '__main__':
    list_number=[12,13,14,15,1,17,18,19]
    lock=multiprocessing.Lock()
    check_even=multiprocessing.Process(target=Checkeven,args=(list_number,lock))
    check_odd=multiprocessing.Process(target=CheckOdd,args=(list_number,lock))


    check_even.start()
    check_odd.start()

    check_even.join()
    check_odd.join()