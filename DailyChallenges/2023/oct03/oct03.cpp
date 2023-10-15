#include <vector>

using namespace std;

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int size = nums.size();
        int out = 0;
        for (int i = 0, j = 1; j<size; i++, j++){
            if (nums[i] == nums[j] ){
                out++;
            }
        }
        return out;
    }

};