#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    for (int a = 0; a < 1000; a++) {
        bool flag = true;
        for (int m = 0; m < 500; m++) {
            for (int n = 0; n < 500; n++) {
                if (((2 * m + 3 * n) > 40 or (m < a and n <= a)) == false) {
                    flag = false;
                }
            }
        }
        if (flag == true) {
            cout << a;
            break;
        }
    }
    return 0;
}

// 21
