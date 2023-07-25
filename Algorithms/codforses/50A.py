# https://codeforces.com/problemset/problem/50/A
P, Q = map(int, input().split())
 
# Calculate the total number of 2x1 squares on the board
total_squares = P * Q
 
# Calculate the maximum number of dominoes that can be placed
max_dominoes = total_squares // 2
 
# Print the maximum number of dominoes
print(max_dominoes) 
#  ребята не понима юкак работет код