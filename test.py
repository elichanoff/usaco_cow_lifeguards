from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from solution import Solution
import os

path = "./test_data"

def extract_test_data():
    ## Retrieve the test data from the USACO website. Extract the zip file, and put the test data files into ./test_data.
    url = "http://www.usaco.org/current/data/lifeguards_silver_jan18.zip"
    resp = urlopen(url)
    myzip = ZipFile(BytesIO(resp.read()))
    myzip.extractall(path=path)


def test_solution():
    results = {}
    ## There are 10 test cases, each with an input and an output file.
    ## Since the test data files are named eg. '2.in', '2.out', we can iterate through range(1, 11) to hit all cases.
    for i in range(1, 11):
        input_path = f"/Users/eli/pet_projects/coding_minds_solution/test_data/{i}.in"
        output_path = f"/Users/eli/pet_projects/coding_minds_solution/test_data/{i}.out"
        ## Instantiate Solution with the test input data.
        test_solution = Solution(input_path)
        print("solution response: ", test_solution.maximum_covered_time())
        print("Actual solution:")
        with open(output_path) as f:
            expected = int(f.readline())
            ## Write the Solution output, the expected output, and if they match, into the results dict.
            results[f"test_{i}"] = {
                "Actual": test_solution.maximum_covered_time(),
                "Expected": expected,
                "Pass": test_solution.maximum_covered_time() == expected,
            }
        f.close()
    return results

def run():
    ## Only retrieve the test data if ./test_data is empty.
    dir = os.listdir(path)
    if len(dir) == 0:
        print("Retrieving test data")
        extract_test_data()
    else:
        print("Test data already found!")
    print("checking answers...")
    ## Test Solution against all test cases, and print the results.
    test_results = test_solution()
    print(test_results)

run()