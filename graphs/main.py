class Vertex:

    def __init__(self, point_from, edges_to):
        self.source_vert_name = point_from
        self.edges = edges_to

edges = [
    Vertex("A", [("B", 5), ("D", 3)]),
    Vertex("B", [("C", 4), ("D", 2), ("E", 3)]),
    Vertex("C", [("E", 3)]),  
    Vertex("D", [("C", 1), ("B",2)]),
    Vertex("E", [])
]

def getIndexEdgeFromLetter(edges_, letter):
    idx = 0
    while idx < len(edges_):
        if edges_[idx].source_vert_name == letter:
            return idx
        idx += 1
    return -1

def getEdgeFromLetter(edges_, letter):
    idx = getIndexEdgeFromLetter(edges_, letter)
    if(idx == -1): return None
    else: return edges_[idx]

def getShortestWay(edges_, start_point_idx, end_point_idx):
    current_point = edges_[start_point_idx]

    j = 0
    min_edge_rel = -1
    rm_index = start_point_idx
    # если 1 из частей ведет в конечную точку сразу, то запоминаем это значение
    while j < len(current_point.edges):
        targ_idx_global = getIndexEdgeFromLetter(edges_, current_point.edges[j][0])
        if(targ_idx_global == end_point_idx):
            target_weight = current_point.edges[j][1]
            if(min_edge_rel == -1): min_edge_rel = target_weight
            else: min_edge_rel = min(min_edge_rel, target_weight)
        j+= 1

    tmp_edges = edges_[:rm_index] + edges_[rm_index + 1:] # удаляем элемент где мы уже были
    if(end_point_idx > rm_index): end_point_idx -= 1 # фикс индекса под измененный массив
    
    for i in current_point.edges:
        e_rel = getShortestWay(tmp_edges, getIndexEdgeFromLetter(tmp_edges, i[0]),
                           end_point_idx) # start_weight + i[1]
        if e_rel == -1:
            continue
        
        current_edge_weight = e_rel + i[1]
        if(e_rel != -1): # есди путь существует
            if(min_edge_rel == -1): min_edge_rel = current_edge_weight
            else: min_edge_rel = min(min_edge_rel, current_edge_weight)
    return min_edge_rel

shortest_edge = getShortestWay(edges, 0, 4)
print(f"shortes way value: {shortest_edge}")
