
# Day 5 Task: Serving Models Your Way

## 1. Scenario

My scenario is a Study Buddy AI. It helps beginners understand programming concepts using simple English and small examples.

## 2. What is Ollama?

Ollama is a tool for running large language models locally.

Its main components are:
- CLI: Used to run commands.
- API server: Accepts requests from applications.
- Model runtime: Loads and runs the language model.

## 3. Modelfile

A Modelfile defines how to create a customized model.

- FROM: Selects the base model.
- PARAMETER: Configures model behaviour.
- SYSTEM: Defines the default instructions.

My Study Buddy model is configured to give short, beginner-friendly explanations.

## 4. REST API

The /api/generate endpoint generates a response from a prompt.

The /api/chat endpoint accepts a sequence of chat messages.

Streaming sends response chunks as they become available. Non-streaming returns the completed response.

## 5. OpenAI-Compatible API

An OpenAI-compatible endpoint allows applications using the OpenAI Python client format to communicate with a compatible local model server.

A request can include system and user messages.

## 6. Performance Metrics

- TTFT: Time to First Token.
- Total time: Time taken to complete the request.
- Tokens per second: Number of generated tokens divided by generation time.
- P95 latency: Time within which 95% of requests complete.

## 7. Performance and Serving Concepts

- num_ctx controls the context window configured for a request or model.
- OLLAMA_KEEP_ALIVE controls how long a model stays loaded after a request.
- OLLAMA_NUM_PARALLEL controls parallel request processing in Ollama.
- KV-cache stores attention-related values to avoid recomputing the full context.
- PagedAttention manages attention memory in blocks.
- Prefix caching reuses computation for shared prompt prefixes.
- Static batching groups requests together before execution.
- Continuous batching dynamically adds requests as others finish.
- Throughput measures work completed per unit of time.
- TPOT means Time Per Output Token.

## 8. Ollama vs vLLM

| Feature | Ollama | vLLM |
|---|---|---|
| Main focus | Simple local model usage | High-throughput model serving |
| Setup | Beginner-friendly | More serving configuration |
| Interface | CLI and REST API | Serving API |
| Performance focus | Convenient local inference | Efficient concurrent inference |

## 9. Implementation Status

The Modelfile, main.py and openai_test.py files have been prepared.

Ollama was not installed or run for this task. Therefore, model creation, REST API execution, timing measurements and screenshots have not been verified.

Actual performance values and command outputs must be recorded only after the corresponding tests are run.

## 10. Conclusion

This task introduces model customization, REST APIs, streaming and model-serving performance concepts. The implementation files are prepared, but the Ollama-specific experiments remain untested.