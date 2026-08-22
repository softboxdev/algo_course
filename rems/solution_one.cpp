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