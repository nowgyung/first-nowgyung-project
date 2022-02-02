#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

int check[6];	//방문체크
vector<int> a[5];

void bfs(){
	queue<int> q;
	q.push(1);	//1번 루트노드넣기
	check[1] = true;	//1번 루트노드방문체크
	while(!q.empty()){
		//queue에 있는 front노드를 꺼냅니다. 
		int front = q.front();
		q.pop();
		printf("%d ", front);
		//꺼낸 노드와 인접한 노드를 방문하고 queue에 넣습니다.
		for(int i=0;i<a[front].size();++i){
			int x = a[front][i];
			while(!check[x]){	//이미 방문했으면 넣지 않습니다.
				q.push(x);
				check[x] = true;	//방문하면 check 
			}
		}
	}
}

int main(){
	//1과 2연결 
	a[1].push_back(2);
	a[2].push_back(1);
	//1과 3연결 
	a[1].push_back(3);
	a[3].push_back(1);
	//2와 3연결 
	a[2].push_back(3);
	a[3].push_back(2);
	//2와 4연결 
	a[2].push_back(4);
	a[4].push_back(2);
	//2와 5연결 
	a[2].push_back(5);
	a[5].push_back(2);
	
	bfs();
	
	return 0;
}