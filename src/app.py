from flask import Flask, jsonify, request

tasks = [
    {'id': 1, 'name': 'Task 1'},
    {'id': 2, 'name': 'Task 2'},
    {'id': 3, 'name': 'Task 3'},
    {'id': 4, 'name': 'Task 4'},
    {'id': 5, 'name': 'Task 5'},
    {'id': 6, 'name': 'Task 6'}
]

app = Flask(__name__)

# curl -v http://localhost:5000
@app.route('/')
def get_message():
    return jsonify("running algorithms")

# curl -v http://localhost:5000/fibbonacci/4
@app.route('/fibbonacci/<int:n>')
def get_fibbonacy(n):
    fib = [0] * n
    if n <= 1:
        return n
    else:
        fib[0] = 0
        fib[1] = 1
        for i in range(2, n):
            fib[i] = fib[i-1] + fib[i-2]
    print(fib)
    return jsonify(fib[n-1])

# curl -v http://localhost:5000/lis/5,7,4,−3,9,1,10,4,5,8,9,3
@app.route('/lis/<string:arr>')
def longest_increasing_subsequence_length(arr):
    arr = arr.split(',')
    arr = [eval(i) for i in arr]
    print(arr)
    n = len(arr)
    lis = [1] * n
    maximum = 0
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] > arr[j] and lis[j] >= maximum):
                maximum = lis[j] 
        lis[i] = maximum + 1  
        maximum = 0      
    
    print(lis)
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return jsonify(maximum)

# curl -v http://localhost:5000/lcs/BCDBCDA,ABECBAB
@app.route('/lcs/<string:arr>')
def longest_common_subsequence_length(arr):
    arr = arr.split(',')
    X = arr[0]
    Y = arr[1]
    m = len(X)
    n = len(Y)
    L = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (X[i-1] == Y[j-1]):
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return jsonify(L[m][n])

# curl -v http://localhost:5000/mscs/5,15,-30,10,-5,40,10
@app.route('/mscs/<string:arr>')
def max_sum_contiguous_subsequence(arr):
    arr = arr.split(',')
    arr = [eval(i) for i in arr]
    n = len(arr)

    T = [0] * n
    for i in range(1,n):
        T[i] = max(T[i-1] + arr[i], arr[i])

    result = max(T)
    return jsonify(result)    

# curl -v http://localhost:5000/mpth/0,120,160,220,320,420
@app.route('/mpth/<string:arr>') 
def min_penalty_traveling_hotel(arr):
    arr = arr.split(',')
    arr = [eval(i) for i in arr]
    n = len(arr)

    T = [0] * n
    P = [0] * n

    for i in range(1,n):
        min_penalty = (200 - (arr[i] - arr[i-1]))**2
        min_penalty_index = i-1
        for j in range(i):
            current_penalty = (200 - (arr[i] - arr[j]))**2
            if (min_penalty > current_penalty):
                min_penalty = T[j] + current_penalty
                min_penalty_index = j

        T[i] = min_penalty
        P[i] = min_penalty_index
    return jsonify(P,T)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
