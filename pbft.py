import random

# Define the small language models (3 nodes that for this case are Sml giving clasification outputs)
class SmallLanguageModel:
    def __init__(self, name):
        self.name = name

    def classify(self, input_data):
        # A simulated "classification" output (1 or 0) based on input data.
        # For simplicity, we use random choice for classification.
        return random.choice([0, 1])

# PBFT Algorithm
def pbft_simulation(input_data):
    # Initialize three nodes
    node1 = SmallLanguageModel("Node1")
    node2 = SmallLanguageModel("Node2")
    node3 = SmallLanguageModel("Node3")

    # Step 1: Each node classifies the input data
    result_node1 = node1.classify(input_data)
    result_node2 = node2.classify(input_data)
    result_node3 = node3.classify(input_data)

    # Step 2: Nodes exchange results (for consensus)
    print(f"Node1 classified: {result_node1}")
    print(f"Node2 classified: {result_node2}")
    print(f"Node3 classified: {result_node3}")

    # Step 3: Reach consensus
    # PBFT requires a quorum (majority agreement). With 3 nodes, 2 or more agreeing results determine the consensus.
    results = [result_node1, result_node2, result_node3]
    count_0 = results.count(0)
    count_1 = results.count(1)

    if count_0 > count_1:
        consensus = 0
        print(f"Consensus reached: {consensus} (majority: {count_0} votes)")
    elif count_1 > count_0:
        consensus = 1
        print(f"Consensus reached: {consensus} (majority: {count_1} votes)")
    else:
        print("No consensus could be reached (tie).")

# Test the PBFT simulation
input_data = "Sample input data for classification"
pbft_simulation(input_data)
