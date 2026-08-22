#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;


long long getNumberOfGoodPairs(int n, const vector<int>& numbers) {
    unordered_map<int, long long> count;
    long long ans = 0;
    int i = 0;
    int rem;
    while(i < n) {
       rem = numbers[i] % 200;
       ans += count[rem];
       count[rem]++;
       i++;
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