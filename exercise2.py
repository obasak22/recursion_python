def no_replace_no_order(balls, k):
    result_list = []
    nrno([], 0, balls, k, result_list)
    return result_list
    pass

def no_replace_order(balls, k):
    result_list = []
    nro([], k, balls, result_list)
    return result_list
    pass

def replace_no_order(balls, k):
    result_list = []
    rno([], 0, balls, k, result_list)
    return result_list

def replace_order(balls, k):
    result_list = []
    ro([], k, balls, result_list)
    return result_list
    pass

def nrno(current, start, balls, k, result_list):
    if len(current) == k:
        result_list.append(current.copy())
        return
    for i in range(start, len(balls)):
        current.append(balls[i])
        nrno(current, i + 1, balls, k, result_list) #no_replace so it will start after i
        current.pop()

def nro(current, remaining, balls, result_list):
    if remaining == 0:
        result_list.append(current)
        return
    for i in range(len(balls)):
        if balls[i] in current:
            continue
        else:
            nro(current + [balls[i]], remaining - 1, balls, result_list)

def rno(current, start, balls, k, result_list):
    if len(current) == k:
        result_list.append(current.copy())
        return
    for i in range(start, len(balls)):
        current.append(balls[i])
        rno(current, i, balls, k, result_list) #replace so it will start at i
        current.pop()

def ro(current, remaining, balls, result_list):
    if remaining == 0:
        result_list.append(current)
        return
    for i in range(len(balls)):
        ro(current + [balls[i]], remaining - 1, balls, result_list)

if __name__ == '__main__':
    # You can uncomment each line after implementing the corresponding function
    print(len(no_replace_no_order([2, 4, 5, 6, 8], 3)))     # 10
    print(len(no_replace_order([2, 4, 5, 6, 8], 3)))        # 60
    print(len(replace_no_order([2, 4, 5, 6, 8], 3)))        # 35
    print(len(replace_order([2, 4, 5, 6, 8], 3)))           # 125
    pass