

def warshall_floyd(dist):
    '''
        Args:
            Distance matrix between two points.

        Returns:
            Matrix of shortest distance.

        Landau notation: O(n ** 3).
    '''

    v_count = len(dist[0])

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
