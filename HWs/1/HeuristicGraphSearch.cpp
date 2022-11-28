#include <iostream>
#include <bits/stdc++.h>
#include <limits.h>
#define ushort unsigned int
#define uint unsigned int
#define myPair pair<unsigned int,ushort*>

using namespace std;
ushort n, h[20][20] = {0};
int main(){
    ushort m, i, j;
    cin >> n >> m;
    ushort** neighbors = new ushort*[n];
    ushort edge_v1[m], edge_v2[m], *state, neighborsNum[n]={0};
    state = new ushort[n+3];
    for (i = 0; i < m; i++) {                                                                           //get edges
        cin >> edge_v1[i] >> edge_v2[i];
        neighborsNum[(uint)edge_v1[i]]++;                                                               //number of edges of each vertex
        neighborsNum[(uint)edge_v2[i]]++;
        h[(uint)edge_v1[i]][(uint)edge_v2[i]] = h[(uint)edge_v2[i]][(uint)edge_v1[i]] = 1;
    }
    for (i = 0; i < n; i++) {
        cin >> state[i];
        neighbors[i] = new ushort[neighborsNum[i]];                                                     //neighbors of each vertex
        neighborsNum[i] = 0;
        h[i][i] = USHRT_MAX;
        if (state[i] == 0) state[n+2] = state[n+1] = i;                                                 //state[n+2]: index of 0; state[n+1]: index of parent
    }
    state[n] = 0;                                                                                       //number of steps from start to this step
    for (i = 0; i < m; i++)                                                                             //initialize neighbors[][]
    {
        neighbors[(uint)edge_v1[i]][(uint)(neighborsNum[(uint)edge_v1[i]]++)] = edge_v2[i];
        neighbors[(uint)edge_v2[i]][(uint)(neighborsNum[(uint)edge_v2[i]]++)] = edge_v1[i];
    }
    {                                                                                                   //in this scope: make up heuristic using BFS over every vertices as source
        ushort temp;
        list<ushort> q;
        for (i = 0; i < n; i++)
        {
            for (j = 0; j < neighborsNum[i]; j++) q.push_back(neighbors[i][j]);
            while (!q.empty())
            {
                temp = q.front();
                q.pop_front();
                for (j = 0; j < neighborsNum[temp]; j++)
                {
                    if (h[i][neighbors[temp][j]]) continue;                                             //continue if vertex is visited
                    h[i][neighbors[temp][j]] = h[neighbors[temp][j]][i] = h[i][temp] + 1;               //set heuristic
                    q.push_back(neighbors[temp][j]);                                                    //add neighbors to queue to be checked
                }   
            }
        }
        for (i = 0; i < n; i++) h[i][i] = 0;
    }
    priority_queue<myPair, vector<myPair>, greater<myPair>> minHeap;
    ushort *temp;
    uint heuristic = 0;
    for (j = 0; j < n; j++) heuristic += h[j][state[j]]; 
    while (heuristic != 0)
    {
        for (i = 0; i < neighborsNum[state[n+2]]; i++)
        {
            if (neighbors[state[n+2]][i] == state[n+1]) continue;                                       //continue if checking state is equal to the previous state
            temp = new ushort[n+3];
            for (j = 0; j < n; j++) temp[j] = state[j];
            temp[state[n+2]] = temp[neighbors[state[n+2]][i]];                                          //swap 0 with one of its neighbors
            temp[neighbors[state[n+2]][i]] = 0;                                                         //swap 0 with one of its neighbors
            temp[n+1] = temp[n+2];                                                                      //update index of previous index of zero for next step
            temp[n+2] = neighbors[state[n+2]][i];                                                       //update index of zero in temp
            temp[n] = state[n] + 1;                                                                     //state[n] & temp[n]: number of steps from start so far
            heuristic = 0;
            for (j = 0; j < n; j++) heuristic += h[j][temp[j]];                                         //heuristic: estimate of lowest remaining steps to reach to goal
            minHeap.push(make_pair(heuristic+temp[n], temp));
        }
        state = minHeap.top().second;
        heuristic = minHeap.top().first - state[n];
        minHeap.pop();
    }
    cout << state[n];    
}