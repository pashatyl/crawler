import numpy as np

from src.Database import Database
from src.Graph import Graph
from src.Helpers import Ids


def pagerank(A: list, L: list, alpha: float):
    # A - reversed incedency list (incoming only)
    # L - incedency list
    # alpha - jump coefficient
    N = len(A)
    pr = np.ones(N, np.float64) / N

    for _ in range(15):
        pr_prev = np.copy(pr)
        pr /= np.sum(pr)
        for i in range(N):
            pr[i] = (1 - alpha) / N + \
                    alpha * np.sum(np.fromiter(
                        (pr[j] / (len(L[j]) if len(L[j]) > 0 else 1) for j in A[i]),
                        dtype=np.float64))
        eps = np.mean(pr - pr_prev, dtype=np.float64)
        print(eps)
        print(np.sum(pr))

    return pr


def fetch_graph(db: str):
    db = Database(db)
    graph = Graph(db)
    e = graph.size()
    # TODO: calculate n
    A = [[] for _ in range(e)]
    ids = Ids()
    for src, dst in graph.iterate_all():
        s = ids.add(src)
        d = ids.add(dst)
        A[s].append(d)
    return A, ids.size(), ids.get_map()


def invert_graph(L, n):
    A = [[] for _ in range(n)]
    for i, row in enumerate(L):
        for e in row:
            A[e].append(i)
    return A


if __name__ == '__main__':
    L, n, ids = fetch_graph("C:\\Personal\\crawler.db")
    A = invert_graph(L, n)
    rank = pagerank(A, L, 0.5)
    pages_rank = []
    for i, e in enumerate(rank):
        pages_rank.append((ids[i], e))
    print(sorted(pages_rank, key=lambda x: -x[1])[:10])
