#91/54 
# very good, didnt even think this would pass all test
# Does not work for [bc,cd] = 2 and than query = [b,d]

def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    #{a : [{b:20, c:10}]}
    output = []
    # Step1 - Build the graph
    graph = {}
    for i,pair in enumerate(equations):
        a,b = pair
        if a not in graph:
            graph[a] = [{}]
        if b not in graph:
            graph[b] = [{}]
        graph[a][0][b] = (values[i])
        graph[b][0][a] = (1/values[i])


    print(graph)
    # Step2 - Search each query (BFS)
    for query in queries:
        start, end = query
        res = 1
        seen = set()
        if not (start in graph and end in graph):
            output+=[-1]

        else:
            queue = [[start,1]]
            found = False
            while queue and not(found):
                el, res = queue.pop()
                seen.add(el)
                if el == end:
                    output += [res]
                    found = True
                else:
                    for key in graph[el][0]:
                        if key not in seen:
                            queue += [[key, graph[el][0][key]*res]]
            if not(found):
                output += [-1]

    return output


eqs = [["a","b"],["b","c"]]
vals = [2,3]
quers = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]


print(calcEquation(eqs, vals, quers))



                    
