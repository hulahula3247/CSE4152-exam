#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll V = 100005, INF = ll(2e18);
ll N, K;
vector<pair<ll, ll>> G[V];

int main(void) {
	
	// All problems use standard input and output.
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N >> K;
	for (int i = 0; i < N-1; i++) {
		ll a, b, c;
		cin >> a >> b >> c;
		G[a].push_back({b, c});
		G[b].push_back({a, c});
	}
	// Write your code here
	// You can erase this skeleton code

	vector<ll> pa(N+1, 1), pe(N+1, 0);
	vector<ll> stk, order; stk.push_back(1);
	while (stk.size()) {
		ll cur = stk.back(); stk.pop_back();
		order.push_back(cur);
		for (auto &[nn, nd]: G[cur]) if (nn != pa[cur]) {
			pa[nn] = cur; pe[nn] = nd; stk.push_back(nn);
		}
	}

	vector<ll> sz(N+1, 1), sd(N+1, 0), S1(N+1, 0), S2(N+1, 0);
	for (int i = N-1; i >= 0; i--) {
		int cur = order[i];
		for (auto &[nn, nd]: G[cur]) if (nn != pa[cur]) {
			sz[cur] += sz[nn];
			sd[cur] += sd[nn] + sz[nn]*nd;
			S1[cur] += S1[nn] + sz[nn]*nd;
			S2[cur] += S2[nn] + sz[nn]*sz[nn]*nd;
		}
	}

	ll tot = N*S1[1] - S2[1];
	if (K == 1) {
		cout << tot << '\n';
		exit(0);
	}

	vector<ll> sd_all(N+1, 0);
	sd_all[1] = sd[1];
	for (int cur: order) {
		for (auto &[nn, nd]: G[cur]) if (nn != pa[cur]) {
			sd_all[nn] = sd_all[cur] + nd*(N-2*sz[nn]);
		}
	}

	ll ans = INF;
	for (ll cur = 2; cur <= N; cur++) {
		ll nn = pa[cur], nd = pe[cur];
		ll a_sz = sz[cur], b_sz = N-sz[cur];
		ll a_tot = a_sz*S1[cur] - S2[cur];

		ll a_sd = sd[cur], b_sd = sd_all[nn] - a_sd - nd*a_sz;
		ll loss = a_sd * b_sz + b_sd * a_sz + a_sz*b_sz*nd;
		ll b_tot = tot - a_tot - loss;

		ans = min(ans, max(a_tot, b_tot));
	}
	cout << ans << '\n';

	return 0;
}