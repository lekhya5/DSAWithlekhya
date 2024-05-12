def get_min(A):
    min_in = A[0]
    for i in range(1, len(A)-1):
        if A[i] < min_in:
            min_in = A[i]
    return min_in

def get_max(A):
    max_in = A[0]
    for i in range(1, len(A)-1):
        if A[i] > max_in:
            max_in = A[i]
    return max_in

if __name__ == "__main__":
    A = [4,9,6,5,2,3]
    print(get_min(A))
    print(get_max(A))
