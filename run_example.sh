#!/bin/bash
# Example script to run synthetic-rag-lite with LiteLLM

# Create input and output directories
mkdir -p input output

# Copy the example markdown file to the input directory
cp example.md input/

# Environment setup options:

# Option 1: Using .env file (recommended)
# If you don't have a .env file yet, create one from the example:
if [ ! -f .env ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "Please edit .env with your API keys before running this script again."
    echo "Then run this script again."
    exit 1
fi

# Option 2: Set environment variables directly
# Uncomment and set your actual keys if not using .env
# For OpenAI
# export OPENAI_API_KEY="your-openai-api-key"

# For Azure OpenAI
# export AZURE_API_KEY="your-azure-api-key"

# For Anthropic
# export ANTHROPIC_API_KEY="your-anthropic-api-key"

# For running locally with Ollama - make sure Ollama is running
# with: ollama serve
# and you've pulled your model with: ollama pull llama3

# Select the appropriate example based on your preferred LLM provider

# OpenAI Example with custom output formats
echo "Processing markdown file with OpenAI and custom output formats..."
python synthetic_rag_lite.py --input input --output output --llm openai --model-fast gpt-4o-mini --model-quality gpt-4o \
  --fact-format all --critic-format markdown --index-format jsonl

# Ollama Example (uncomment to use instead)
# echo "Processing markdown file with Ollama..."
# python synthetic_rag_lite.py --input input --output output --llm ollama --ollama-model llama3

# Anthropic Example (uncomment to use instead)
# echo "Processing markdown file with Anthropic..."
# python synthetic_rag_lite.py --input input --output output --llm anthropic --model-fast claude-3-haiku-20240307 --model-quality claude-3-opus-20240229

# Azure OpenAI Example (uncomment to use instead)
# echo "Processing markdown file with Azure OpenAI..."
# python synthetic_rag_lite.py --input input --output output --llm azure --azure-api-base "https://your-resource.openai.azure.com" --azure-deployment your-deployment-name

# With Fallbacks Example (uncomment to use instead)
# echo "Processing markdown file with fallbacks..."
# python synthetic_rag_lite.py --input input --output output --use-fallbacks --fallback-models anthropic/claude-3-haiku-20240307 ollama/llama3

# LiteLLM Proxy Example (uncomment to use instead)
# echo "Processing markdown file with LiteLLM proxy..."
# python synthetic_rag_lite.py --input input --output output --litellm-proxy "http://localhost:8000" --litellm-proxy-key "your-proxy-api-key"

# Query the indexed facts
echo -e "\nQuerying indexed facts..."
python query.py --query "What are the benefits of RAG?" --index output/7-index

echo -e "\nTry your own queries:"
echo "python query.py --query \"your query here\" --index output/7-index"