#include <iostream>
#include <vector>

using namespace std;


long long getNumberOfGoodPairs(int n, const vector<int>& numbers) {

    vector<long long> count(200, 0);
    long long ans = 0;

    for(int i = 0; i < n; ++i) {
        int rem = numbers[i] % 200;
        ans += count[rem];
        count[rem] = count[rem] + 1;
    }
   
    return ans;
}

int readInt() {
    int x;
    cin >> x;
    return x;
}

vector<int> readList(int n) {
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

int main() {
    int n = readInt();
    vector<int> numbers = readList(n);
    cout << getNumberOfGoodPairs(n, numbers);
}