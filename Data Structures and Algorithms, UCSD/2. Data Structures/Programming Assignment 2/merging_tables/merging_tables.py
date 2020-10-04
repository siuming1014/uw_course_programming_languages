# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
assert n == len(lines)
rank = [1] * n
parent = list(range(n))
tables = list(range(n))
ans = max(lines)


def getParent(table):
    # find parent and compress path
    tables_in_path = []
    while table != parent[table]:
        tables_in_path.append(table)
        table = parent[table]
    for _table in tables_in_path[:-1]:
        parent[_table] = table
    return table


def merge(destination, source, ans):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination != realSource:
        if rank[realDestination] < rank[realSource]:
            parent[realDestination] = realSource
            lines[realSource] = lines[realDestination] + lines[realSource]
            lines[realDestination] = 0
            tables[realDestination], tables[realSource] = tables[realSource], tables[realDestination]
            if lines[realSource] > ans:
                ans = lines[realSource]
        else:
            parent[realSource] = realDestination
            lines[realDestination] = lines[realDestination] + lines[realSource]
            lines[realSource] = 0
            if rank[realDestination] == rank[realSource]:
                rank[realSource] += 1
            if lines[realDestination] > ans:
                ans = lines[realDestination]

    return ans


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ans = merge(destination - 1, source - 1, ans)
    print(ans)
    
