#include <bits/stdc++.h>
using namespace std;
int N, K, A[100005], B[100005];
int dp[100005][5][2];
const int INF = 0x3f3f3f3f;

int re_dp(int idx, int k, int fg) {
    if (idx == N) return 0;
    if (dp[idx][k][fg] != INF) return dp[idx][k][fg];
    int ret = -int(2e9);
    if (k) ret = max(ret, re_dp(idx, k-1, fg^1));
    if (!fg) ret = max(ret, re_dp(idx+1, k, fg)+A[idx]);
    else ret = max(ret, re_dp(idx+1, k, fg)+B[idx]);
    dp[idx][k][fg] = ret;
    return ret;
}

int main(void) {
	
	// All problems use standard input and output.
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> K;
	for (int i = 0; i < N; i++) cin >> A[i];
	for (int i = 0; i < N; i++) cin >> B[i];

	// Write your code here
	// You can erase this skeleton code

    memset(dp, INF, sizeof(dp));
	cout << re_dp(0, K, 0) << '\n';

	return 0;
}