from src.pagerank.Pagerank import fetch_graph, invert_graph, pagerank

if __name__ == '__main__':
    L, n, ids = fetch_graph("C:\\Personal\\crawler.db")
    A = invert_graph(L, n)
    rank = pagerank(A, L, 0.5)
    pages_rank = []
    for i, e in enumerate(rank):
        pages_rank.append((ids[i], e))
    print(sorted(pages_rank, key=lambda x: -x[1])[:10])
