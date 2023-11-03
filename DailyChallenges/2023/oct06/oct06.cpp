#include <cmath>

class Solution {
public:
    int integerBreak(int n) {
        int out;
        if (n==2){
            return 1;
        } else if (n==3){
            return 2;
        } else {
            int remain = n/3;
            int mod = n%3;
            if (mod==0){
                out = pow(3,remain);
            } else if (mod==1){
                out = 2*2*pow(3,remain-1);
            } else {
                out = 2*pow(3,remain);
            }
        }
        return out;
    }
};

// Beat 100.00% of C++ Users Bo (<- surprised emoji)