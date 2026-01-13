#include <bits/stdc++.h>
using namespace std;

int main(void) {
	
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	// write your code here

    int N; cin >> N;
    int n = N, ans = 0;
    for (int i = 2; i <= N; i++) {
        while (n%i == 0) {
            n /= i;
            ans += i;
        }
    }
    cout << ans << '\n';

	return 0;
}