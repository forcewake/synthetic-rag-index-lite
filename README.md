# Synthetic RAG Lite

A streamlined tool for synthesizing content from markdown files and images into high-quality indexed facts for retrieval-augmented generation (RAG) systems.

**Purpose**

This project aims to provide a lightweight alternative to Microsoft's [Synthetic RAG Index](https://github.com/microsoft/synthetic-rag-index), focusing on simplicity and efficiency for users who require core functionalities without the overhead of a full-scale system.

**Key Differences from Synthetic RAG Index**

- **Simplified Processing Pipeline**: While the original project offers a comprehensive multi-stage pipeline, Synthetic RAG Lite condenses this into essential steps to streamline content synthesis.

- **Broader LLM Provider Support**: Leveraging LiteLLM, this tool supports various LLM providers, including OpenAI, Azure OpenAI, Anthropic, Cohere, Ollama, Together.ai, Google VertexAI, AWS Bedrock, and custom providers via LiteLLM proxy.

- **Flexible Output Formats**: Users can choose from multiple output formats - JSON, JSONL, Markdown, or all simultaneously - to suit different integration needs.

- **Optional Image Processing**: Incorporates OCR capabilities for image files, allowing for text extraction from images when needed.

**Improvements and Additions**

- **Enhanced LLM Integration**: By utilizing LiteLLM, the tool offers advanced features such as model fallbacks, load balancing, and caching, ensuring reliability and performance.

- **User-Friendly Configuration**: Simplified setup with clear command-line options and environment variable configurations, making it accessible even for users with limited technical expertise.

- **Modular Design**: The codebase is structured for easy maintenance and scalability, allowing for future enhancements and customizations.

**Why a Lite Version?**

The motivation behind creating Synthetic RAG Lite was to offer a more accessible and efficient solution for users who need the core functionalities of content synthesis and indexing without the complexity and resource requirements of the full Synthetic RAG Index system. This lite version caters to projects with limited resources or those seeking a straightforward implementation.

**Acknowledgment**

This project is inspired by and builds upon the foundational work of Microsoft's [Synthetic RAG Index](https://github.com/microsoft/synthetic-rag-index). I extend our gratitude to the original developers for their contributions to the field.

---

## Features

- Process markdown files (.md) and plain text (.txt)
- Optional image processing with OCR for .jpg, .jpeg, .png, .gif, .bmp (requires PIL and pytesseract)
- Multi-stage processing pipeline:
  1. Extract content from files
  2. Chunk content into manageable pieces
  3. Synthesize chunks into concise summaries
  4. Generate question-answer pairs (facts) from content
  5. Score and filter facts for quality
  6. Index facts for retrieval
- Support for multiple LLM providers via LiteLLM:
  - OpenAI
  - Azure OpenAI
  - Anthropic
  - Cohere
  - Ollama (local LLM)
  - Together.ai
  - Google VertexAI
  - AWS Bedrock
  - Custom providers via LiteLLM proxy
- Advanced LiteLLM features:
  - Model fallbacks for reliability
  - Load balancing (via LiteLLM proxy)
  - Caching (via LiteLLM proxy)
- Multiple output formats:
  - JSON (pretty-printed, default)
  - JSONL (JSON Lines)
  - Markdown (human-readable)
  - All formats simultaneously

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/yourusername/synthetic-rag-lite.git
   cd synthetic-rag-lite
   ```

   > **Note**: For backward compatibility, a symbolic link named `local_rag.py` points to `synthetic_rag_lite.py`. Both filenames will work, but we recommend using `synthetic_rag_lite.py` in new scripts.

2. Create a virtual environment and install dependencies:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. For image processing support (optional):

   ```
   pip install pillow pytesseract
   ```

   You'll also need to install Tesseract OCR:
   - On macOS: `brew install tesseract`
   - On Ubuntu/Debian: `apt-get install tesseract-ocr`
   - On Windows: Download and install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

## Usage

1. Create input and output directories:

   ```
   mkdir -p input output
   ```

2. Place your markdown files and/or images in the input directory.

3. Run the tool:

   ```
   python synthetic_rag_lite.py --input input --output output
   ```

### Command-line Options

```
usage: synthetic_rag_lite.py [-h]
                    [--input INPUT] [--output OUTPUT]
                    [--llm {openai,azure,anthropic,cohere,ollama,together,vertex,bedrock,custom}]
                    [--model-fast MODEL_FAST] [--model-quality MODEL_QUALITY]
                    [--azure-api-base AZURE_API_BASE]
                    [--azure-api-version AZURE_API_VERSION]
                    [--azure-deployment AZURE_DEPLOYMENT]
                    [--ollama-model OLLAMA_MODEL] [--ollama-url OLLAMA_URL]
                    [--litellm-proxy LITELLM_PROXY] [--use-fallbacks]
                    [--fallback-models FALLBACK_MODELS [FALLBACK_MODELS ...]]
                    [--fact-format {json,jsonl,markdown,all}]
                    [--critic-format {json,jsonl,markdown,all}]
                    [--index-format {json,jsonl,markdown,all}]

Synthetic RAG Lite

options:
  -h, --help            show this help message and exit

Input/Output Configuration:
  --input INPUT, -i INPUT
                        Input directory containing markdown files and images
  --output OUTPUT, -o OUTPUT
                        Output directory for processed files

LLM Provider Configuration:
  --llm {openai,azure,anthropic,cohere,ollama,together,vertex,bedrock,custom}
                        LLM provider to use
  --model-fast MODEL_FAST
                        Fast LLM model name for routine tasks
  --model-quality MODEL_QUALITY
                        High quality LLM model name for synthesis and critique

Azure OpenAI Configuration:
  --azure-api-base AZURE_API_BASE
                        Azure OpenAI API base URL (required for Azure provider)
  --azure-api-version AZURE_API_VERSION
                        Azure OpenAI API version
  --azure-deployment AZURE_DEPLOYMENT
                        Azure OpenAI deployment name

Ollama Configuration:
  --ollama-model OLLAMA_MODEL
                        Ollama model name (if using Ollama provider)
  --ollama-url OLLAMA_URL
                        Ollama API base URL

LiteLLM Configuration:
  --litellm-proxy LITELLM_PROXY
                        LiteLLM proxy URL for model routing
  --litellm-proxy-key LITELLM_PROXY_KEY
                        API key for authenticating with the LiteLLM proxy
  --use-fallbacks       Enable model fallbacks in case of errors
  --fallback-models FALLBACK_MODELS [FALLBACK_MODELS ...]
                        List of fallback models to try if primary model fails

Output Format Configuration:
  --fact-format {json,jsonl,markdown,all}
                        Output format for fact stage (default: json)
  --critic-format {json,jsonl,markdown,all}
                        Output format for critic stage (default: json)
  --index-format {json,jsonl,markdown,all}
                        Output format for index stage (default: json)
```

## LLM Configuration with LiteLLM

LiteLLM provides a unified interface to multiple LLM providers, allowing you to easily switch between them or set up fallbacks.

### Setting Environment Variables

You can set environment variables in three ways:

#### 1. Using a .env file (Recommended)

Create a `.env` file in the project directory with your API keys:

```
# .env file
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

A sample `.env.example` file is provided with the project. Simply copy it to `.env` and fill in your values:

```bash
cp .env.example .env
# Then edit .env with your favorite editor
```

You can also specify a custom env file location:

```bash
python synthetic_rag_lite.py --env-file /path/to/your/.env
```

#### 2. Using environment variables directly

Set the appropriate API keys for your chosen provider in your shell:

```bash
# For OpenAI
export OPENAI_API_KEY=your_openai_key

# For Azure OpenAI
export AZURE_API_KEY=your_azure_key

# For Anthropic
export ANTHROPIC_API_KEY=your_anthropic_key

# For Cohere
export COHERE_API_KEY=your_cohere_key

# For Google VertexAI
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# For AWS Bedrock
export AWS_ACCESS_KEY_ID=your_aws_access_key_id
export AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
```

### Example Provider Configurations

#### Using OpenAI

```bash
python synthetic_rag_lite.py --llm openai --model-fast gpt-4o-mini --model-quality gpt-4o
```

#### Using Azure OpenAI

```bash
python synthetic_rag_lite.py --llm azure --azure-api-base "https://your-resource.openai.azure.com" --azure-deployment your-deployment-name
```

#### Using Anthropic

```bash
python synthetic_rag_lite.py --llm anthropic --model-fast claude-3-haiku-20240307 --model-quality claude-3-opus-20240229
```

#### Using Ollama (Local LLM)

```bash
python synthetic_rag_lite.py --llm ollama --ollama-model llama3 --ollama-url "http://localhost:11434"
```

### Advanced Features

#### Using Model Fallbacks

Enable fallbacks to automatically try alternative models if the primary model fails:

```bash
python synthetic_rag_lite.py --llm openai --model-fast gpt-4o-mini --model-quality gpt-4o --use-fallbacks --fallback-models anthropic/claude-3-haiku-20240307 ollama/llama3
```

#### Using Multiple Output Formats

Choose different output formats for each processing stage:

```bash
python synthetic_rag_lite.py --input input --output output --fact-format all --critic-format markdown --index-format jsonl
```

Available formats are:

- `json`: Standard pretty-printed JSON (default)
- `jsonl`: JSON Lines format (one JSON object per line)
- `markdown`: Human-readable Markdown
- `all`: Generate all formats simultaneously

#### Using LiteLLM Proxy

If you're running a LiteLLM proxy for load balancing or custom routing:

```bash
python synthetic_rag_lite.py --litellm-proxy "http://localhost:8000"
```

If your LiteLLM proxy requires authentication (separate from the underlying provider):

```bash
python synthetic_rag_lite.py --litellm-proxy "http://localhost:8000" --litellm-proxy-key "your-proxy-api-key"
```

You can also set these in your .env file:

```
LITELLM_PROXY_URL=http://localhost:8000
LITELLM_PROXY_KEY=your-proxy-api-key
```

### Repetition Detection

The tool automatically filters out content with excessive repetition. You can adjust the sensitivity of this detection:

```bash
# In your .env file or environment
REPETITION_THRESHOLD=2.0  # Higher values are more permissive (default: 2.0)
```

This threshold determines how much repetition is allowed in the content:

- Values below 1.0 are very strict
- Default value is 2.0
- Higher values allow more repetition
- Set to 0 to disable repetition detection

## Output Structure

The tool creates a structured output directory:

```
output/
├── 0-sanitize/          # Sanitized input files
├── 1-extract/           # Extracted text content
├── 2-chunck/            # Content split into chunks
├── 3-synthesis/         # Synthesized chunk summaries
├── 4-page/              # Content split into pages
├── 5-fact/              # Generated facts
├── 6-critic/            # Quality-filtered facts
└── 7-index/             # Indexed facts for retrieval
```

The final output in the `7-index` directory contains files with question-answer pairs derived from your content, ready for use in retrieval systems. Depending on the output format(s) selected, these could be JSON (*.json), JSON Lines (*.jsonl), or Markdown (*.md) files.

The query tool automatically loads both JSON and JSONL formats when searching for facts. If you need to work with multiple output formats, remember to specify the appropriate format in your data loading code.

## Requirements

- Python 3.8+
- OpenAI or Ollama
- For image processing:
  - Pillow
  - pytesseract
  - Tesseract OCR
