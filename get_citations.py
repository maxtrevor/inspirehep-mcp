#!/usr/bin/env python3
"""Fetch BibTeX citations for a list of DOIs from InspireHEP."""

import asyncio
import json
import sys

# Add src to path
sys.path.insert(0, "/home/user/inspirehep-mcp/src")

from inspirehep_mcp.api_client import InspireHEPClient
from inspirehep_mcp.tools import get_bibtex


async def main():
    """Fetch BibTeX citations for all DOIs."""
    dois = [
        "10.1038/nature09466",
        "10.1126/science.1233232",
        "10.1126/science.1203264",
        "10.1103/PhysRevD.82.101301",
        "10.1088/0264-9381/26/6/063001",
        "10.1016/j.crhy.2013.01.008",
        "10.1086/345812",
        "10.1103/PhysRevD.92.084040",
        "10.1088/0264-9381/34/1/015001",
        "10.1088/0264-9381/28/12/125023",
        "10.1088/0264-9381/32/2/024001",
        "10.1103/PhysRevD.23.1693",
    ]

    client = InspireHEPClient()

    print("=" * 80)
    print("Fetching INSPIRE-HEP citations for DOIs")
    print("=" * 80)
    print()

    # Store all BibTeX entries
    bibtex_entries = []

    for i, doi in enumerate(dois, 1):
        print(f"\n{'=' * 80}")
        print(f"[{i}/{len(dois)}] DOI: {doi}")
        print("=" * 80)

        result_json = await get_bibtex(client, doi=doi)
        result = json.loads(result_json)

        if "error" in result:
            print(f"❌ ERROR: {result['error']}")
        else:
            print(f"\nTitle: {result.get('title', 'N/A')}")
            print(f"INSPIRE ID: {result.get('inspire_id', 'N/A')}")
            print(f"\nBibTeX:\n")
            print(result.get('bibtex', 'N/A'))

            # Add to collection if successful
            if result.get('bibtex'):
                bibtex_entries.append(result['bibtex'])

    await client.close()

    # Write all BibTeX entries to file
    with open('citations.bib', 'w') as f:
        f.write('\n'.join(bibtex_entries))

    print("\n" + "=" * 80)
    print(f"✅ Done! Saved {len(bibtex_entries)} citations to citations.bib")
    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
