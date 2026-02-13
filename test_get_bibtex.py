#!/usr/bin/env python3
"""Test script to get BibTeX citation for a DOI."""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from inspirehep_mcp.api_client import InspireHEPClient
from inspirehep_mcp.tools import get_bibtex


async def main():
    """Get BibTeX citation for DOI: 10.1016/0375-9474(74)90528-4"""
    doi = "10.1016/0375-9474(74)90528-4"

    print(f"Fetching BibTeX citation for DOI: {doi}\n")

    client = InspireHEPClient()
    result = await get_bibtex(client, doi=doi)

    print("Result:")
    print("=" * 80)
    print(result)
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
