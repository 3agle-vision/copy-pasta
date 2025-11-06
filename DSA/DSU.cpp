struct DSU {
    vector<int> parent, size;
    
    DSU(int n) { 
        parent.resize(n); 
        size.resize(n, 1);
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    
    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]); // path compression
    }
    
    void unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return; // already in same set
        
        // union by size
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
    }
};
