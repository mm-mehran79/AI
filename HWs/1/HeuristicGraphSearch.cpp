#include <iostream>
#define ushort unsigned short
#define uint unsigned int
#define myPair(V) pair<unsigned int,ushort[V+1]>

using namespace std;
ushort n;
int main(){
    ushort m, i;
    cin >> n >> m;
    ushort** neighbors = new ushort*[n];
    ushort edge_v1[m], edge_v2[m], state[n+1], neighborsNum[n]={0};
    for (i = 0; i < m; i++) {
        cin >> edge_v1[i] >> edge_v2[i];
        neighborsNum[(uint)edge_v1[i]]++;
        neighborsNum[(uint)edge_v2[i]]++;
    }
    for (i = 0; i < n; i++) {
        cin >> state[i];
        neighbors[i] = new ushort[neighborsNum[i]];
        neighborsNum[i] = 0;
    }
    state[n] = 0;
    for (i = 0; i < m; i++)
    {
        neighbors[(uint)edge_v1[i]][(uint)(neighborsNum[(uint)edge_v1[i]]++)] = edge_v2[i];
        neighbors[(uint)edge_v2[i]][(uint)(neighborsNum[(uint)edge_v2[i]]++)] = edge_v1[i];
    }
    
}
inline uint heuristic(int state[]){
    uint h = 0;
    for (ushort i = 0; i < n; i++)
        if (state[i] != i) h++;
    return h;
}