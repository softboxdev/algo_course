#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


long getCardCount(int n, int k, const vector<long long> &cards) {
    int sum = 0;
    for (int i = 0; i < k; ++i) {
        sum += cards[i];
        
    }
    int ans = sum;
    int left = k - 1;
    int right = n - 1;
    while(right >= n - k) {
        sum += cards[right] - cards[left];
        if(sum > ans)
            //ans = max(ans, sum);
            ans = sum;
        --left;
        --right;
    }
    return ans;
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