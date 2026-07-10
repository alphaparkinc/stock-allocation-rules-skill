"""
example_usage.py -- Demonstrates StockAllocationClient
"""
from client import StockAllocationClient

def main():
    client = StockAllocationClient()
    result = client.allocate_stock(
        available_units=100,
        channels_demand={"wholesale": 80, "shopify": 40, "amazon": 30}
    )
    print("[Stock Allocation Result]")
    print(f"Allocations: {result['allocation_results']}")
    print(f"Unfulfilled: {result['unfulfilled_demand']} units")

if __name__ == "__main__":
    main()
