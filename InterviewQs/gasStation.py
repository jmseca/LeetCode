#beat 32%

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        size = len(gas)
        start_indx = -1
        current_gas = -1
        laps = 0
        while laps < 2:
            for i in range(size):
                if i==start_indx:
                    return start_indx 
                new_gas = (gas[i]-cost[i] + current_gas)
                
                if current_gas == -1:
                    if new_gas >= -1:
                        current_gas = new_gas + 1
                        start_indx = i
                else:
                    if new_gas < 0:
                        start_indx = -1
                        current_gas = -1
                    else:
                        current_gas = new_gas


            laps += 1

        return -1
        