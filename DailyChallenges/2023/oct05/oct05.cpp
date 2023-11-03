#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
    public:
        vector<int> majorityElement(vector<int>& nums) {
            unordered_map<int,int> mapa;
            size_t i,size = nums.size();
            size_t erase_count = 0, count = size/3;
            vector<int> res;
            int elem;
            i = 0;
            printf("COunt: %ld\n", count);
            while (i<size) {
                elem = nums[i];
                if (mapa.find(elem) == mapa.end()) {
                    mapa[elem] = (count);
                    i++;
                } else {
                    mapa[elem]--;

                    i++;
                    
                }
                if (mapa[elem] == 0){
                    res.push_back(elem);
                    for (auto it = nums.begin() + i; it != nums.end(); ) {
                        if (*it == elem) {
                            it = nums.erase(it);
                            erase_count++;
                        } else {
                            ++it;
                        }
                    }
                    size-=erase_count;
                    erase_count = 0;
                    mapa.erase(elem);
                } 
            }
            return res;
        }
};


int main(){

    Solution sol;

    vector<int> nums = {3,2,3};
    vector<int> ola = sol.majorityElement(nums);

    for (auto it = ola.begin(); it != ola.end(); ++it) {
        cout << *it << endl;
    }

    return 0;
}