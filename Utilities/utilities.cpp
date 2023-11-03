#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

/*A binary search, but can also say in which index* should the target be if it was present in the array
In the case above, the value returned is negative to indicate that it was not found

All indices are returned +1. This means the output 1 refers to 0. This is to solve the problem where the target does not
exist, but should in the first position*/ 
template <typename T>
int binaryFind(vector<T>& arr, T target){
    int size = arr.size();
    int mid, left = 0, right = size-1;

    if (!size){
        return -1;
    }

    while (left <= right){
        mid = left + (right - left) / 2;
        
        if (arr[mid] == target){
            return (mid+1);
        } else if (arr[mid] < target){
            left = mid + 1;
        } else {
            right = mid - 1;
        }   
    }         
    if (arr[mid] < target){
        return -(mid+2);
    }   
    return -(mid+1);
}


template <typename T>
void print2DVector(vector<vector<T>>& v){
    int sizee;
    cout << '{' << endl;
    for (int i = 0; i< v.size(); i++){
        
        sizee = v[i].size();
        cout << "\t{" ;
        for (int j = 0; j<sizee; j++){
            cout << v[i][j] << ", ";
        }
        cout << "}" << endl;
        
    }
    cout << '}' << endl;
        
}

/*
Similar to the binary find above, but it works with count pairs

For example:
[[0,1], [3,2], [5,1]]
Where [i,n]:
i - value
n - times value has been seen
*/
template <typename T>
int binaryCountPairFind(vector<pair<T,int>>& arr, T target){
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

/*
Similar to the binary find above, but it works with ranges
This means that 'arr' is a list of sorted ranges.

For example:
[[0,10], [15,30], [40,40]]
*/
template <typename T>
int binaryRangeFind(vector<vector<T>>& arr, vector<T>& target_range){
    auto target = target_range[0];
    int size = arr.size();
    int left = 0, right = size - 1, mid;

    if (!size)
        return -1;

    while (left <= right){
        mid = left + (right - left)/2;
        if (arr[mid][0] <= target && arr[mid][1] >= target){
            return (mid+1);
        } else if (arr[mid][1] < target){
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    if (arr[mid][0]<target)
        return -(mid+2);
    return -(mid+1);
}

/*
Given a list of sorted deltas ([x,y], with both ints and x<=y) 'sorted'.
And 'i' the position where a new delta 'delta' should be placed.
It adds the new delta to the sorted deltas list, merging any existing deltas, if necessary.

For example:
sorted = [[0,10], [20,30], [35,40]]
delta = [8,21]

It returns:
sorted = [[0,30], [35,40]]
*/
template <typename T>
vector<vector<T>> mergeDeltaWithSorted(vector<vector<T>>& sorted, vector<T>& delta, int i){
    sorted.insert(sorted.begin() + i, delta);

    print2DVector(sorted);

    cout << i << ' ' << (i + 1 < sorted.size()) << ' ' << sorted[i][1] << ' ' << sorted[(i+1)][0] << endl;

    while ( (i + 1 < sorted.size()) && (sorted[i][1] > sorted[(i+1)][0])) {
        delta = {sorted[i][0],max(sorted[i+1][1],sorted[i][1])};
        sorted.erase(sorted.begin() + i);
        sorted[i] = delta;
        print2DVector(sorted);
    }

    return sorted;
}





int main(){
    return 0;
}
    
    
