
class Solution:
    def __init__(self, input):
        self.input = input
        self.shifts = self.read_in()

    def read_in(self):
        with open(self.input) as f:
            ## The first line of the input file is the number of shifts
            num_shifts = int(f.readline())
            timepoints = []
            ## For each subsequent line, split the string into start and end time point tuples,
            ## convert the strings to integers, and put them in the timepoints list.
            for line in f:
                timepoints_str = line.split()
                timepoints_int = (int(timepoints_str[0]), int(timepoints_str[1]))
                timepoints.append(timepoints_int)
        f.close()
        return timepoints
    
    def maximum_covered_time(self):
        flattened_shifts = []
        alone_time = {}
        ## Split each shift into tuples (cow_n, start) and (cow_n, end).
        ## Add tuples to the list flattened_shifts.
        for cow, shift in enumerate(self.shifts):
            ## Also add to the dict alone_time key: value pairs for each cow.
            ## Each cow starts with alone time of 0.
            alone_time[f'cow_{cow}'] = 0
            for timepoint in shift:
                flattened_shifts.append((timepoint, f'cow_{cow}'))

        ## Sort the flattened shifts
        flattened_shifts.sort()

        ## Keep track of which cows are working, the previously encountered time point, and the total time.
        ## Here, we start these off based on the first time point in flattened_shifts.
        working = [flattened_shifts[0][1]]
        last = flattened_shifts[0][0]
        total_time = 0

        ## Since we instantiated the above variables with the first time point in flattened shifts,
        ## we will start iterating from the second time point.
        for timepoint in flattened_shifts[1:]:
            ## Calculate time pass since previous time point
            time_passed = timepoint[0] - last
            ## If a cow was working in that period, increment the total time.
            if len(working) > 0:
                total_time += time_passed
            ## If only one cow was working, increment that cow's alone time.
            if len(working) == 1:
                alone_time[working[0]] += time_passed
            ## If the cow in the current time point was already working, then their shift is over.
            ## Remove that cow from working
            if timepoint[1] in working:
                working.remove(timepoint[1])
            ## Otherwise, their shift is starting. Add that cow to working.
            else:
                working.append(timepoint[1])
            ## Update the previously encountered endpoint
            last = timepoint[0]

        ## The cow with the least alone time is the minimum value in the alone_time dict.
        least_alone_time = min(alone_time.values())
        ## Finally, calculate the maximum covered time by subtracting the least alone time from the total time.
        max_covered_time = total_time - least_alone_time
        return max_covered_time