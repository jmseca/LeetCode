#include <vector>


using namespace std;

class MyHashMap {
    private:
        vector<int> v;
        int size;


    public:
        MyHashMap() {
            v = vector<int>(1000001, -1);
        }
        
        void put(int key, int value) {
            int indx = key % size;
            v[indx] = value;
        }
        
        int get(int key) {
            return v[key % size];
        }
        
        void remove(int key) {
            v[key % size] = -1;
        }
};