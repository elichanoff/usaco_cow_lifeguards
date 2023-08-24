
class Solution:
    def __init__(self, input):
        self.input = input
        self.shifts = self.read_in()

    def read_in(self):
        with open(self.input) as f:
            num_shifts = int(f.readline())
            timepoints = []
            for line in f:
                timepoints_str = line.split()
                timepoints_int = (int(timepoints_str[0]), int(timepoints_str[1]))
                timepoints.append(timepoints_int)
        f.close()
        return timepoints
    
    def maximum_covered_time(self):
        flattened_shifts = []
        alone_time = {}
        for cow, shift in enumerate(self.shifts):
            alone_time[f'cow_{cow}'] = 0
            for timepoint in shift:
                flattened_shifts.append((timepoint, f'cow_{cow}'))


        flattened_shifts.sort()  # Sort the shifts by their starting times

        working = [flattened_shifts[0][1]]
        last = flattened_shifts[0][0]
        total_time = 0

        for timepoint in flattened_shifts[1:]:
            time_passed = timepoint[0] - last
            if len(working) > 0:
                total_time += time_passed
            if len(working) == 1:
                alone_time[working[0]] += time_passed
            if timepoint[1] in working:
                working.remove(timepoint[1])
            else:
                working.append(timepoint[1])
            last = timepoint[0]

        least_alone_time = min(alone_time.values())
        max_covered_time = total_time - least_alone_time
        return max_covered_time