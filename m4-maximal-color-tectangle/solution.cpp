#include <bits/stdc++.h>
using namespace std;
int N, arr[2005][2005], last[2005], pf[2005];

int histo(vector<int> &flat) {
    vector<int> st;
    int mmax = 0;
    for (int i = 1; i < flat.size(); i++) {
        while (st.size() && flat[st.back()] > flat[i]) {
            int h = flat[st.back()];
            st.pop_back();
            int w;
            if (!st.size()) w = i-1;
            else w = i-1 - st.back();
            mmax = max(mmax, h*w);
        }
        st.push_back(i);
    }
    while (st.size()) {
        int h = flat[st.back()];
        st.pop_back();
        int w;
        if (!st.size()) w = flat.size()-1;
        else w = flat.size()-1-st.back();
        mmax = max(mmax, h*w);
    }
    return mmax;
}

int main(void) {
	
	// All problems use standard input and output.
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) cin >> arr[i][j];
	}
	
	int ans = 0;
    memset(last, 0x3f3f3f3f, sizeof(last));
    for (int i = 0; i < N; i++) {
        vector<int> query;
        query.push_back(0);
        for (int j = 0; j < N; j++) {
            if (arr[i][j] == last[j]) pf[j]++;
            else pf[j] = 1;
            if ((j != 0) && (arr[i][j-1] != arr[i][j])) {
                ans = max(ans, histo(query));
                query.clear();
                query.push_back(0);
            }
            query.push_back(pf[j]);
            last[j] = arr[i][j];
        }
        ans = max(ans, histo(query));
    }

	cout << ans << '\n';

	return 0;
}