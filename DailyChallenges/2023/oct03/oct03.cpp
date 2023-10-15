#include <vector>
#include <algorithm>
#include <iostream>
#include <stdio.h>

using namespace std;


void print2DVector(vector<pair<int,int>>& v){
    cout << '{' << endl;
    for (long unsigned int i = 0; i< v.size(); i++){        
        cout << "\t{ " << v[i].first << ", "  <<  v[i].second  << " }" << endl;
        
    }
    cout << '}' << endl;
        
}



class Solution {
public:

    int binaryCountPairFind(vector<pair<int,int> >& arr, int target){
        int size = arr.size();
        int left = 0, right = size - 1, mid;

        if (!size)
            return -1;

        while (left <= right){
            mid = left + (right - left)/2;
            if (arr[mid].first == target){
                return (mid+1);
            } else if (arr[mid].first < target){
                left = mid + 1;
            } else {
                right = mid - 1;
            }   
        }
        if (arr[mid].first < target)
            return -(mid+2);
        return -(mid+1);
    }

    int numIdenticalPairs(vector<int>& nums) {
        int size = nums.size(), out = 0, ix;
        vector<pair<int,int> > myPairVector;
        myPairVector.reserve(size);
        for (int i = size-1; i >= 0; i--){

            ix = binaryCountPairFind(myPairVector, nums[i]);
            if (ix < 0) {
                ix = abs(ix)-1;
                myPairVector.insert(myPairVector.begin() +ix, pair<int,int>(nums[i],1));
            } else {
                out += myPairVector[(ix-1)].second;
                myPairVector[(ix-1)].second++;
            }
        }
        return out;
    }

};



int main(){

    Solution solution;
    vector<int> t1 = {1,1,1,1};

    cout << solution.numIdenticalPairs(t1) << endl;


    return 0;
}