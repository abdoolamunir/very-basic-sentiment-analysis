# Very Basic Sentiment Analysis API

## Table of Contents
- [Introduction](#introduction)
- [Overview](#overview)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Hugging Face Space](#hugging-face-space)
- [Contributors](#contributors)
- [License](#license)


## Introduction
This API utilizes a machine learning model to analyze text for sentiment, categorizing input as positive, negative, or neutral. It leverages a pre-trained BERT model from Hugging Face Transformers, integrated within a FastAPI framework to provide quick and reliable sentiment analysis.

## Overview
This project was developed to demonstrate the ability to deploy a machine learning model using FastAPI and Docker, making it accessible as a web API. The sentiment analysis model used is based on BERT, a transformer model pre-trained on a large corpus of text and fine-tuned for sentiment analysis.

## Dependencies
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Docker**: A set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers.
- **Pydantic**: Data validation and settings management using python type annotations.
- **Hugging Face Transformers**: Provides thousands of pre-trained models to perform tasks on texts such as classification, information extraction, question answering, summarization, translation, text generation, etc in 100+ languages. This project specifically utilizes the [Sentiment Analysis BERT model by MarieAngeA13](https://huggingface.co/MarieAngeA13/Sentiment-Analysis-BERT?text=I+like+you.+I+love+you) for analyzing text sentiment.
- **pytest**: A framework that makes it easy to write simple tests yet scales to support complex functional testing.


## Installation
Follow these instructions to set up the API locally:

### Clone the repository
```bash
git clone https://github.com/abdoolamunir/very-basic-sentiment-analysis.git
cd very-basic-sentiment-analysis

```

### Build the Docker Container
This command builds the Docker container, which includes installing all the necessary dependencies from 'requirements.txt'.
```bash
docker build -t sentiment-analysis-api .
```

### Run the Docker container
```bash
docker run -p 8000:8000 sentiment-analysis-api
```

## Usage
After Launching the API, you can use it as follows:
### Open Swagger UI
```bash
http://localhost:8000/docs
```

## Analyze text sentiment
To analyze the text sentiment, send a POST requent:
```bash
curl -X 'POST' \
  'http://localhost:8000/analyze' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "This product is great!"}'
```

## Example Response
```json
{
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.9999
    }
  ]
}
```

## Testing
To run the tests, execute the following command:
```bash
pytest
```
## Hugging Face Space
The API is also deployed on Hugging Face Spaces. You can access it here: []()

## Contributors
Abdullah Munir & anyone who wants to use this basic framework and add onto it :)

## License
This project is released under the Apache License 2.0. See the LICENSE file in the repository for more details.
