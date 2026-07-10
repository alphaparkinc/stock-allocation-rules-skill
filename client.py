"""
stock-allocation-rules-skill: Client SDK
Applies channel priority weights to allocate scarce product quantities.
"""
from __future__ import annotations
from typing import Optional

# Channel priority weights (higher gets fulfilled first)
CHANNEL_PRIORITIES = ["wholesale", "shopify", "amazon"]


class StockAllocationClient:
    """
    SDK for supply allocation planning.
    """

    def allocate_stock(
        self,
        available_units: int,
        channels_demand: dict,
    ) -> dict:
        allocated = {}
        remaining = available_units

        # Allocate in order of priority
        for ch in CHANNEL_PRIORITIES:
            demand = int(channels_demand.get(ch, 0))
            if demand > 0:
                assigned = min(remaining, demand)
                allocated[ch] = assigned
                remaining -= assigned
            else:
                allocated[ch] = 0

        # Sum remaining unfulfilled requests
        unfulfilled = sum(int(v) for v in channels_demand.values()) - sum(allocated.values())

        return {
            "allocation_results": allocated,
            "unfulfilled_demand": max(0, unfulfilled),
            "remaining_warehouse_stock": remaining
        }
