#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int u, v, weight;
} Edge;

int compare_edges(const void *a, const void *b) {
    Edge *edge1 = (Edge *)a;
    Edge *edge2 = (Edge *)b;
    return edge1->weight - edge2->weight;
}

int find(int parent[], int i) {
    if (parent[i] == -1)
        return i;
    return find(parent, parent[i]);
}

void union_sets(int parent[], int x, int y) {
    int xset = find(parent, x);
    int yset = find(parent, y);
    parent[xset] = yset;
}

void kruskal(Edge edges[], int n, int e) {
    qsort(edges, e, sizeof(Edge), compare_edges);

    int parent[n];
    for (int i = 0; i < n; i++)
        parent[i] = -1;

    Edge result[n - 1];
    int edge_count = 0;
    int minimum_cost = 0;

    for (int i = 0; i < e; i++) {
        int x = find(parent, edges[i].u);
        int y = find(parent, edges[i].v);

        if (x != y) {
            result[edge_count++] = edges[i];
            minimum_cost += edges[i].weight;
            union_sets(parent, x, y);
        }
    }

    printf("Edges in the minimum spanning tree:\n");
    for (int i = 0; i < edge_count; i++)
        printf("%d -- %d == %d\n", result[i].u, result[i].v, result[i].weight);

    printf("Minimum cost: %d\n", minimum_cost);
}

int main() {
    int MAX_EDGES = 100;  // Adjust as needed
    Edge edges[MAX_EDGES];
    int n, e;

    printf("Enter the number of vertices: ");
    scanf("%d", &n);

    printf("Enter the number of edges: ");
    scanf("%d", &e);

    printf("Enter the edges (u, v, weight):\n");
    for (int i = 0; i < e; i++) {
        scanf("%d %d %d", &edges[i].u, &edges[i].v, &edges[i].weight);
    }

    kruskal(edges, n, e);

    return 0;
}

