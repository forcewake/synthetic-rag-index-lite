# CLAUDE.md - Synthetic RAG Lite Reference

## Key Commands
- Run main tool: `python synthetic_rag_lite.py --input input --output output`
- Run with specific provider: `python synthetic_rag_lite.py --llm [provider] --model-fast [model1] --model-quality [model2]`
- Run with custom formats: `python synthetic_rag_lite.py --fact-format [format] --critic-format [format] --index-format [format]`
- Query indexed facts: `python query.py --query "your query" --index output/7-index`
- Setup environment: `cp .env.example .env` (then edit with API keys)
- Run example script: `bash run_example.sh`

## Code Style
- Python 3.8+ with type hints
- Import order: stdlib → third-party → local modules
- Error handling: Use try/except with specific exceptions
- Logging: Use the logger from logging module, not print statements
- Type hints: Use Optional[], List[], Dict[], TypeVar for generics
- Async patterns: Use asyncio for concurrent operations

## Naming Conventions
- Variables/functions: snake_case
- Classes: PascalCase
- Constants: UPPER_SNAKE_CASE
- Type variables: Single uppercase letter (T)
- Dataclasses for structured data

## Architecture Notes
- Pipeline-based processing with staged outputs
- LiteLLM as unified interface for LLM providers
- Environment variables via python-dotenv (.env file)
- Multiple output formats (json, jsonl, markdown, all)
- Format-specific serialization with consistent structure