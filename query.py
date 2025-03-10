#!/usr/bin/env python3
# Simple query script for synthetic-rag-lite
# Demonstrates how to query the indexed facts

import argparse
import json
import os
from pathlib import Path
import re
from typing import List, Dict, Any


def normalize_text(text: str) -> str:
    """Normalize text for better matching."""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def load_indexed_facts(index_dir: Path) -> List[Dict[str, Any]]:
    """Load all indexed facts from the index directory."""
    facts = []
    
    if not index_dir.exists():
        print(f"Error: Index directory {index_dir} does not exist.")
        return facts
    
    # Load all JSON files in the index directory
    for file_path in index_dir.glob("*.json"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                fact = json.load(f)
                facts.append(fact)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    
    # Also load JSONL files if they exist
    for file_path in index_dir.glob("*.jsonl"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        fact = json.loads(line)
                        facts.append(fact)
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
    
    print(f"Loaded {len(facts)} facts from {index_dir}")
    return facts


def search_facts(facts: List[Dict[str, Any]], query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """Search facts using simple keyword matching."""
    query_normalized = normalize_text(query)
    query_words = set(query_normalized.split())
    
    # Score each fact based on word overlap
    scored_facts = []
    for fact in facts:
        # Combine all text fields for matching
        text_fields = [
            fact.get('question', ''),
            fact.get('answer', ''),
            fact.get('context', ''),
            fact.get('document_synthesis', '')
        ]
        fact_text = normalize_text(' '.join(text_fields))
        fact_words = set(fact_text.split())
        
        # Calculate simple overlap score
        overlap = len(query_words.intersection(fact_words))
        if overlap > 0:
            scored_facts.append((overlap, fact))
    
    # Sort by score (descending) and take top_k
    scored_facts.sort(reverse=True)
    return [fact for _, fact in scored_facts[:top_k]]


def format_fact(fact: Dict[str, Any]) -> str:
    """Format a fact for display."""
    question = fact.get('question', 'N/A')
    answer = fact.get('answer', 'N/A')
    context = fact.get('context', '')
    
    formatted = f"Q: {question}\nA: {answer}"
    if context:
        formatted += f"\nContext: {context}"
    
    return formatted


def main():
    parser = argparse.ArgumentParser(description="Query indexed facts from synthetic-rag-lite")
    parser.add_argument(
        "--index", "-i", type=str, default="output/7-index",
        help="Path to the index directory containing fact JSON files"
    )
    parser.add_argument(
        "--query", "-q", type=str, required=True,
        help="Query to search for in the indexed facts"
    )
    parser.add_argument(
        "--top", "-k", type=int, default=3,
        help="Number of top results to return"
    )
    args = parser.parse_args()
    
    index_dir = Path(args.index)
    
    # Load indexed facts
    facts = load_indexed_facts(index_dir)
    if not facts:
        return
    
    # Search for matching facts
    results = search_facts(facts, args.query, args.top)
    
    # Display results
    if not results:
        print(f"No matching facts found for query: '{args.query}'")
        return
    
    print(f"\nTop {len(results)} results for query: '{args.query}'\n")
    for i, result in enumerate(results, 1):
        print(f"Result {i}:")
        print(format_fact(result))
        print()


if __name__ == "__main__":
    main()