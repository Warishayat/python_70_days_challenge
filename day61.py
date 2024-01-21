# #multithreading is used to download the multiple file parallely  benefit of multithreading....

# import threading
# import time
# from concurrent.futures import ThreadPoolExecutor

# def fun(second) :       #function
#     print(f"Func sleep for {second}")
#     time.sleep(second)
#     print("Fun sleep time is competed")
#     return time

# def main():
        
#     time1=time.perf_counter()
#     # fun(2)
#     # fun(3)
#     # fun(4)
#     # fun(5)     #fun calling


#     t1=threading.Thread(target=fun,args=[2])
#     t2=threading.Thread(target=fun,args=[3])
#     t3=threading.Thread(target=fun,args=[4])
#     t4=threading.Thread(target=fun,args=[5])
#     t1.start()
#     t2.start()
#     t3.start()
#     t4.start()

#     t1.join()          # is tak rukna h
#     time2=time.perf_counter()
#     print(time2-time1)

# def poolingDemo():
#     with ThreadPoolExecutor() as executor:
#         # future = executor.submit(fun, 3)
#         # future = executor.submit(fun, 4)
#         # future = executor.submit(fun, 5)
#         # print(future.result())
#         # print(future.result())
#         # print(future.result())
#         l=[3,4,5,6,7,8,9]
#         result=executor.map(fun,l)
#         for result in result:
#             print(result)
# poolingDemo()


# Question: Implement a multi-threaded Python program that calculates the square of each
# number in a given list concurrently. Create two threads to handle even and odd indices
# separately. Ensure proper synchronization to avoid race conditions.
import threading
def evenNumber(number,lock):
    l=[]
    for i in number:        #iterate the list
        if i % 2==0:
            s=i*i   #make new variable to make square of even number.
            l.append(s)         #shift even number to list
    with lock:
        print("List")
        print(l)


def oddNumber(number,lock):
    l=[]
    for i in number:        #iterate the list to check odd..
        if i % 2 !=0:       #Chec knumber is odd.
            s=i*i           # S to store the square of odd number
            l.append(s)     #append back to list odd number
    with lock:
        print("List")
        print(l)


list_number=[1,2,3,4,5,6,7,8,9,10]
# evenNumber(list_number)
# oddNumber(list_number)
lock=threading.Lock()
even_Number=threading.Thread(target=evenNumber,args=(list_number,lock))
odd_Number=threading.Thread(target=oddNumber,args=(list_number,lock))

even_Number.start()
odd_Number.start()

even_Number.join()
odd_Number.join()