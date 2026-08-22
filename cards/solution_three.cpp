#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long getCardCount(int n, int k, const vector<long long> &cards) {
    int sum = 0;
    vector<int> prefix(k + 1, 0);
    for (int i = 1; i <= k; ++i) {
        prefix[i] = prefix[i-1] + cards[i-1];
    }

    vector<int> suffix(k+1,0);
    for(int i = 1; i <= k; ++i) {
        suffix[i] = suffix[i-1] + cards[n-i];
    }
    int max_sum = 0;
    for(int left_count = 0; left_count <= k; ++left_count) {
        int right_count = k - left_count;
        int sum = prefix[left_count] + suffix[right_count];
        if (sum > max_sum)
            max_sum = sum;        
    }
    return max_sum;
}

int readInt() {
    int x;
    cin >> x;
    return x;
}

vector<long long> readList(int n) {
    vector<long long> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

int main() {
    int n = readInt();
    int k = readInt();
    vector<long long> cards = readList(n);
    cout << getCardCount(n, k, cards);
}