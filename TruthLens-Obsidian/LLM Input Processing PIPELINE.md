# Flowchart Diagram Mermaid Code
flowchart TB

    A[Call to replicate-llava: ] -->|Identify Image Type.| C[Call to replicate-llava: ]   
    C -->|Get Image Description with 'Type-Tailored' Prompt.| D[Call to mistral api: ]
    D -->|Convert to WebSearch Bullet-Point Plan focused on FactChecking. |G[Call to gpt3.5 model: ]
    G -->|Convert to SerpAPI Calls.| J[Call to mistral api: ]
    G -->|Convert to NewsAPI Calls.| J
    G -->|Convert to GoogleFactCheck Calls.| J
    J -->|Aggregate Information in a single Document.| K[End Process] 
    J -->|Aggreate all Source Links in a single list.| K
    


# Flowchart Diagram View
![[Pasted image 20231218100755.png]]


Certainly! Below is an expanded documentation for the TruthLens fact-checking pipeline, integrating the knowledge gathered from the provided documents and web search. 

# TruthLens Fact-Checking Pipeline Documentation

## Overview
The TruthLens fact-checking pipeline is designed to automate the process of validating the authenticity and accuracy of digital media, specifically images. This pipeline utilizes various APIs to analyze images, search for corroborative information, and compile a comprehensive fact-checking report.

## Pipeline Components

### 1. LLava API
- **Purpose**: To identify the content and context of an image.
- **Functionality**: Processes an image to determine its type and extract a detailed description that is tailored to the image's content.
- **Endpoint**: `replicate-llava` endpoint is called with an image file as input.
- **Output**: A JSON object containing the image type and a description.

### 2. SerpAPI
- **Purpose**: To gather search engine results for fact-checking.
- **Functionality**: Queries various search engines using the image description to find corroborative or refuting evidence.
- **Endpoint**: `serpapi.com/search.json` endpoint is used with customized parameters based on the image description.
- **Output**: Search results in JSON format, including links, snippets, and metadata from various search engines.

### 3. Google Fact Check Tools API
- **Purpose**: To access verified fact-check claims related to the image content.
- **Functionality**: Searches the Fact Check Explorer for claims and pages relevant to the image description.
- **Endpoint**: `FactCheckToolsService` with `claims()` and `pages()` methods.
- **Output**: A collection of verified fact-check claims and associated metadata.

### 4. GPT-3.5-turbo API
- **Purpose**: To generate a bullet-point plan for fact-checking based on the image description.
- **Functionality**: Processes the image description to produce a structured plan that outlines key points to be verified.
- **Endpoint**: `openai.com/api/v1/engines/gpt-3.5-turbo/completions` endpoint is used with a prompt derived from the image description.
- **Output**: A set of bullet points outlining the fact-checking strategy.

### 5. Mistral API
- **Purpose**: To analyze text and aggregate information.
- **Functionality**: Synthesizes information from various sources and generates a coherent document summarizing the findings.
- **Endpoint**: `docs.mistral.ai` endpoints for chat completions and embeddings.
- **Output**: A single document aggregating all information and a list of all source links.

### 6. NewsAPI
- **Purpose**: To pull in current news articles related to the image or topic being fact-checked.
- **Functionality**: Retrieves articles from a wide range of news sources using the image description.
- **Endpoint**: `newsapi.org/v2/everything` endpoint is used with parameters based on the image description.
- **Output**: News articles and reports relevant to the fact-checking process.

## Pipeline Flow

1. **Call to LLava API**: 
   - Input: User-provided image.
   - Process: Image type identification and description generation.
   - Output: Image type and tailored description.

2. **Generate Fact-Checking Plan**: 
   - Input: Image description from LLava API.
   - Process: GPT-3.5-turbo generates a structured bullet-point plan for fact-checking.
   - Output: Bullet-point plan.

3. **Execute Web Searches**: 
   - Input: Bullet-point plan.
   - Process: SerpAPI conducts searches based on the plan. NewsAPI and Google Fact Check Tools API called in parallel for additional data.
   - Output: Search results, news articles, and verified claims.

4. **Aggregate Information**: 
   - Input: Data from SerpAPI, NewsAPI, and Google Fact Check Tools API.
   - Process: Mistral API compiles the data into a coherent summary document.
   - Output: Comprehensive fact-checking report and a list of all source links.

## Usage

To use the pipeline, send a POST request with an image file to the LLava API endpoint. The pipeline will then automatically execute the subsequent steps, returning a final fact-checking report that includes the image's description, the bullet-point plan, search results, news articles, and verified claims related to the image content.

## Conclusion

The TruthLens fact-checking pipeline is a sophisticated tool that leverages the power of AI to provide real-time fact-checking capabilities. By combining the strengths of multiple APIs, it offers a robust solution for verifying digital media authenticity, which is vital for maintaining information integrity, especially during critical events such as national elections.