#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int, int>;
using pll = pair<ll, ll>;
#define all(v) v.begin(), v.end()
int N, K, fail[100050];
string s;

int get_fail(int x, int tg) {
	for (int i = 1, j = 0; i < N; i++) {
		if (x+i == N) return x+i;
		fail[i] = 0;
		while (j > 0 && s[x+i] != s[x+j]) j = fail[j-1];
		if (s[x+i] == s[x+j]) fail[i] = ++j;
		if (i+1 - fail[i] > tg) return x+i;
	}
    return N;
    // cout << x << ' ' << tg << '\n';
}

bool ok(int tg) {
    memset(fail, 0, sizeof(fail));
    int cur = 0, idx = 0;
	while (idx < N) {
		cur++;
		idx = get_fail(idx, tg);
	}
    return (cur <= K);
}

void solve() {

	cin >> N >> K >> s;
    int lo = 0, hi = N;
    while (lo + 1 < hi) {
        int mid = (lo+hi)/2;
        if (ok(mid)) hi = mid;
        else lo = mid;
    }
    cout << hi << '\n';

}

int main(void) {
	
	ios::sync_with_stdio(false);
	cin.tie(0);
	int T = 1;
	//cin >> T;
	while (T--) solve();
	return 0;
}