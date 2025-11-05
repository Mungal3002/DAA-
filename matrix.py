#one thread per row
import threading
import time

def multiply_row(A, B, C, row):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[row][j] += A[row][k] * B[k][j]

def multithread_row(A, B):
    rows = len(A)
    cols = len(B[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    threads = []

    for i in range(rows):
        t = threading.Thread(target=multiply_row, args=(A, B, C, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return C

# Measure time for row-wise threads
start = time.time()
C_thread_row = multithread_row(A, B)
end = time.time()

print("\nResultant Matrix (Thread per Row):")
for row in C_thread_row:
    print(row)
print(f"Execution Time (Thread/Row): {end - start:.6f} seconds")

#one thread per call 
def multiply_cell(A, B, C, i, j):
    for k in range(len(B)):
        C[i][j] += A[i][k] * B[k][j]

def multithread_cell(A, B):
    rows = len(A)
    cols = len(B[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    threads = []

    for i in range(rows):
        for j in range(cols):
            t = threading.Thread(target=multiply_cell, args=(A, B, C, i, j))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    return C

# Measure time for cell-wise threads
start = time.time()
C_thread_cell = multithread_cell(A, B)
end = time.time()

print("\nResultant Matrix (Thread per Cell):")
for row in C_thread_cell:
    print(row)
print(f"Execution Time (Thread/Cell): {end - start:.6f} seconds")
