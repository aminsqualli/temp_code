import concurrent.futures
import time

class ConcurrentRunner:
    def __init__(self):
        pass
    
    # Define your methods with arguments
    def method_one(self, arg1):
        time.sleep(1)  # Simulate a delay
        return f"Result from method one with argument {arg1}"

    def method_two(self, arg1, arg2):
        time.sleep(2)  # Simulate a delay
        return f"Result from method two with arguments {arg1} and {arg2}"

    def method_three(self, arg1, arg2, arg3):
        time.sleep(3)  # Simulate a delay
        return f"Result from method three with arguments {arg1}, {arg2}, and {arg3}"

    # Method to run methods concurrently using multi-threading
    def run_methods_concurrently(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Submit each method to the executor with their respective arguments
            future_one = executor.submit(self.method_one, "arg1_for_one")
            future_two = executor.submit(self.method_two, "arg1_for_two", "arg2_for_two")
            future_three = executor.submit(self.method_three, "arg1_for_three", "arg2_for_three", "arg3_for_three")
            
            # Collect results
            results = []
            for future in concurrent.futures.as_completed([future_one, future_two, future_three]):
                try:
                    result = future.result()
                    results.append(result)  # Collect the results
                except Exception as e:
                    print(f"An error occurred: {e}")
            return results

# Create an instance of the class
runner = ConcurrentRunner()

# Run the methods concurrently
results = runner.run_methods_concurrently()

# Print the results
for result in results:
    print(result)