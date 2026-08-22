#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<long long> count(200, 0);
    long long ans = 0;
    
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        int rem = x % 200;
        
        // Добавляем все пары с этим остатком
        // (текущий элемент образует пару с каждым из уже встреченных)
        ans += count[rem];
        
        // Увеличиваем счётчик
        count[rem]++;
    }
    
    cout << ans << '\n';
    return 0;
}

#include <iostream>
#include <vector>

using namespace std;


long long getNumberOfGoodPairs(int n, const vector<int>& numbers) {

    vector<long long> count(200, 0);
    for(int i = 0; i < n; ++i) {
        int rem = numbers[i] % 200;
        count[rem] = count[rem] + 1;
    }
    long long ans = 0;
    for (int r = 0; r < 200; ++r) {
        long long cnt = count[r];
        ans += cnt * (cnt - 1) / 2;
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