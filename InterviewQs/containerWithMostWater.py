def maxArea(height):
    start = [0, height[0]]
    end = []
    stack = []
    areas = [-1]*len(height)
    for i in range(1, len(height)):
        poss_end = [i, height[i]]
        poss_area = calculateArea(start, poss_end)
        if poss_area > areas[i-1]:
            end = poss_end
            areas[i] = poss_area
        else:
            areas[i] = areas[i-1]
        
        if height[i] > start[1]:
            j = 0
            keep_going = True
            while j<len(stack) and keep_going:
                poss_start = stack[j]
                poss_area = calculateArea(poss_start, end)
                print(f"poss area = {poss_area} with start = {poss_start}, end = {poss_end}")
                if poss_area > areas[i]:
                    print("There will be stack change")
                    print(f"start = {poss_start}, end = {end}, area = {poss_area}")
                    start = poss_start
                    areas[i] = poss_area
                    stack = stack[(j+1):]
                    keep_going = False
                j+=1

            stack += [poss_end]
    print(areas)
    return calculateArea(end, start)

def calculateArea(h1, h2):
    if not(h1) or not(h2):
        return -1
    return min(h1[1],h2[1]) * abs(h1[0] - h2[0])

print(maxArea([1,2,3,4,5,25,24,3,4]))