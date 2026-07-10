# stock-allocation-rules-skill

> **GenPark AI Agent Skill** -- Channel-prioritized stock allocation manager.

## Quick Start

```python
from client import StockAllocationClient
client = StockAllocationClient()
res = client.allocate_stock(50, {"shopify": 30, "wholesale": 40})
print(res["allocation_results"])
```
