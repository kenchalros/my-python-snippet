from dijkstra import Dijkstra

class TestDijkstra:

    def test_dijkstra(self):
        graph = [
            [(2, 1), (5, 2)],
            [(2, 0), (4, 2), (6, 3), (10, 4)],
            [(5, 0), (4, 1), (2, 3)],
            [(2, 2), (6, 1), (1, 5)],
            [(10, 1), (3, 5), (5, 6)],
            [(1, 3), (3, 4), (9, 6)],
            [(5, 4), (9, 5)]
        ]
        djk = Dijkstra()

        actual = djk.dijkstra(graph, 0)
        expected = [0, 2, 5, 7, 11, 8, 16]
        assert actual == expected

        actual = djk.dijkstra(graph, 0, 6)
        expected = [0, 2, 3, 5, 4, 6]
        assert actual == expected

