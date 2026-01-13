#include <bits/stdc++.h>
using namespace std;
int N, Q, arr[1005][1005], D[1005][1005], query[200005][5];

int main(void) {
	
	// All problems use standard input and output.
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> Q;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) cin >> arr[i][j];
	}

	for (int i = 0; i < Q; i++) {
        int r1, c1, r2, c2, v; cin >> r1 >> c1 >> r2 >> c2 >> v;
        r1--; c1--; r2--; c2--;
        D[r1][c1] += v;
        D[r1][c2+1] -= v;
        D[r2+1][c1] -= v;
        D[r2+1][c2+1] += v;
	}

    for (int i = 0; i < N; i++) {
        for (int j = 1; j < N; j++) D[i][j] += D[i][j-1];
    }

    for (int j = 0; j < N; j++) {
        for (int i = 1; i < N; i++) D[i][j] += D[i-1][j];
    }

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) cout << arr[i][j] + D[i][j] << ' ';
		cout << '\n';
	}

	return 0;
}