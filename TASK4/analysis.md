# Day 4 – Open LLM Memory, Quantization and Licence Analysis

## 1. Scenario

### Scenario
Local AI assistant for daily coding and question-answering tasks.

### Machine
- OS: Windows 11 (AMD64)
- Processor: 13th Gen Intel(R) Core(TM) i5-13420H
- System RAM: 16 GB
- GPU: NVIDIA GeForce RTX 3050
- Dedicated GPU VRAM: 6 GB
- Usable GPU memory budget: 5.4 GB

### Purpose
The purpose of this analysis is to estimate whether different open models can fit within the available GPU memory before downloading or running them.

### Users
The intended users are students and individual developers who want to run a small language model locally.

### Memory Budget
The available dedicated GPU memory is 6 GB. The practical estimator uses a recommended budget of 5.4 GB after driver overhead.


## 2. Key Concepts

### 2.1 Model Weights

Model weights are the learned parameters of a language model. The number of parameters and the precision used to store them affect the memory required by the model.

For example, a larger model with more parameters requires more memory than a smaller model.

In this scenario, checking model weights helps determine whether a model can fit within the available 5.4 GB GPU memory budget.

### 2.2 Quantization

Quantization reduces the number of bits used to represent model weights.

Lower-precision formats such as Q4_K_M require less memory than FP16. This makes larger models easier to run on limited hardware, although lower precision can involve some quality trade-offs.

In this scenario, quantization is important because the GPU has only 6 GB of dedicated VRAM.

### 2.3 KV Cache and Context Length

The KV cache stores information from previous tokens while the model processes a conversation.

As the context length increases, the KV cache also increases. Therefore, a model using the same weights can require significantly more memory at a larger context length.

The practical experiment showed that increasing context from 4K to 8K and 32K increased the estimated total memory.

### 2.4 Memory Estimate

The practical estimator calculates memory approximately using:

- Model weights
- KV cache
- 10% overhead

The estimate is useful for deciding whether a model may fit before downloading it. However, it is only an estimate and actual memory usage can differ.

### 2.5 Model Card

A model card provides important information about a model, including its capabilities, limitations, parameters, context length, and licence.

Checking the model card before using a model helps understand whether it is suitable for the intended scenario.

### 2.6 Open-Weight vs Open-Source

An open-weight model provides access to model weights, but this does not automatically mean that it has a conventional open-source licence.

The exact licence and its conditions must be checked before commercial use, modification, or redistribution.


## 3. Memory Estimate Results

The estimator was run on my HP Victus laptop with 6 GB dedicated GPU VRAM and a recommended usable budget of 5.4 GB.

| Model | Params | Precision | Context | Weights (GB) | KV Cache (GB) | Total (GB) | Fits in 5.4 GB? |
|---|---:|---|---:|---:|---:|---:|---|
| Qwen small | 1.5B | Q4_K_M | 8K | 0.85 | 0.24 | 1.20 | Yes |
| Granite / Qwen mid | 8B | Q4_K_M | 8K | 4.56 | 1.28 | 6.42 | No |
| Mid model | 8B | FP16 | 8K | 16.00 | 1.28 | 19.01 | No |
| Large local (Command-R/Qwen) | 30B | Q4_K_M | 8K | 17.10 | 4.80 | 24.09 | No |
| Server class (Llama) | 70B | Q4_K_M | 8K | 39.90 | 11.20 | 56.21 | No |

### Observation

The 1.5B Q4_K_M model uses approximately 1.20 GB and fits comfortably within the 5.4 GB usable GPU memory budget.

The 8B Q4_K_M model requires approximately 6.42 GB, which is already above the available budget.

The larger 30B and 70B models require substantially more memory and therefore do not fit within the available GPU memory.

This shows that parameter count and precision have a major effect on memory requirements.

For this machine, the 1.5B Q4_K_M configuration is the most memory-efficient option among the tested configurations.


## 4. Context Length Experiment

The same 8B model with Q4_K_M quantization was tested at different context lengths.

| Model | Precision | Context | Weights (GB) | KV Cache (GB) | Total (GB) | Fits in 5.4 GB? |
|---|---|---:|---:|---:|---:|---|
| 8B model | Q4_K_M | 4K | 4.56 | 0.64 | 5.72 | No |
| 8B model | Q4_K_M | 8K | 4.56 | 1.28 | 6.42 | No |
| 8B model | Q4_K_M | 32K | 4.56 | 5.12 | 10.65 | No |
| 8B model | Q4_K_M | 128K | 4.56 | 20.48 | 27.54 | No |

### Observation

The model weights remain approximately constant because the model and quantization are unchanged.

As context length increases, the KV cache increases. Therefore, the total estimated memory also increases.

In this experiment, even the 4K configuration is slightly above the 5.4 GB usable GPU memory budget. Therefore, none of the tested 8B Q4_K_M context configurations fit within the available budget.

The largest tested context was 128K, but it required approximately 27.54 GB of memory and therefore does not fit on this machine.


## 5. Quantization Experiment

The same 8B model was tested at a fixed 8K context length using different quantization levels.

| Model | Precision | Context | Weights (GB) | KV Cache (GB) | Total (GB) | Fits in 5.4 GB? |
|---|---|---:|---:|---:|---:|---|
| 8B model | Q3_K_M | 8K | 3.44 | 1.28 | 5.19 | Yes |
| 8B model | Q4_K_M | 8K | 4.56 | 1.28 | 6.42 | No |
| 8B model | Q5_K_M | 8K | 5.44 | 1.28 | 7.39 | No |
| 8B model | Q8_0 | 8K | 8.00 | 1.28 | 10.21 | No |
| 8B model | FP16 | 8K | 16.00 | 1.28 | 19.01 | No |

### Observation

The context length was kept constant at 8K, so the KV cache remained approximately 1.28 GB.

Changing the quantization mainly changed the model weight memory.

Q3_K_M used the least memory and, at approximately 5.19 GB total, fits within the 5.4 GB usable GPU memory budget.

Q4_K_M required approximately 6.42 GB and therefore did not fit.

Higher-precision configurations such as Q8_0 and FP16 required significantly more memory.

This demonstrates the trade-off between memory usage and precision. Lower quantization can make a model possible to run on limited hardware, while higher precision requires more memory.


## 6. Open Model Comparison

The following three models were selected from different model families. Their model cards and licence information were reviewed before making the suitability decision.

| Model / Version | Publisher | Parameters | MoE | Context Window | Exact Licence | Commercial Use | Extra Conditions | Tool Calling | GGUF Available | Ollama Available | Q4 Download Size | Estimated Memory | Fits 5.4 GB? | Date Checked |
|---|---|---:|---|---:|---|---|---|---|---|---|---:|---:|---|---|
| Qwen2.5-1.5B-Instruct | Qwen | 1.54B | No | 32K | Apache 2.0 | Yes, subject to licence | Follow Apache 2.0 terms | Check model documentation | Yes | Yes | To be verified | ~1.20 GB at Q4_K_M, 8K | Yes | 03-10-2026 |
| Granite 3.3-2B-Instruct | IBM | 2B | No | 128K | Apache 2.0 | Yes, subject to licence | Follow Apache 2.0 terms | Check model documentation | Yes | Yes | To be verified | To be calculated | To be calculated | 03-10-2026 |
| Llama 3.2-1B-Instruct | Meta | 1.24B | No | 128K | Llama 3.2 Community License | Subject to licence terms | Community License and Acceptable Use Policy apply | Stated in supported tooling | Yes | Yes | To be verified | To be calculated | To be calculated | 03-10-2026 |

### Licence Observation

The licence must be checked separately from model size and memory requirements.

Apache 2.0 and the Llama 3.2 Community License have different terms. Therefore, a model that fits the hardware is not automatically suitable for every intended use.

The licence, acceptable-use requirements, redistribution conditions, and other restrictions should be checked before using a model in a real project.


## 7. Suitability Analysis

### Recommended Model

Based on the memory estimates, the recommended model for this machine is:

**Qwen2.5-1.5B-Instruct, Q4_K_M, 8K context**

The practical estimator shows approximately 1.20 GB of total memory usage for the 1.5B Q4_K_M configuration. This is comfortably below the 5.4 GB usable GPU memory budget.

The model is therefore suitable for a lightweight local coding and question-answering assistant where memory efficiency is important.

### Runner-up

The 8B Q4_K_M configuration was considered as a larger-model alternative. However, the estimated memory requirement is approximately 6.42 GB at 8K context, which is above the available 5.4 GB GPU budget.

Therefore, the 8B configuration was not selected for this machine.

### When the Recommendation Could Change

The recommendation could change if the hardware had more dedicated GPU VRAM or if a larger system memory budget were available.

A larger memory budget would allow higher-parameter models or higher-precision configurations to be considered.

Similarly, if the main requirement were very long context rather than low memory usage, a model with a larger context window could become more relevant, provided sufficient memory were available.


## 8. Estimate vs Reality

### Local Ollama Run

Ollama was not installed on this machine for this exercise. Therefore, an actual local model was not pulled or started using Ollama.

Because of this, the following runtime measurements were not collected:

- `ollama list` model size
- `ollama ps` processor information
- Actual runtime memory usage
- CPU/GPU split information

The memory values reported in this analysis are therefore estimates produced by the provided practical estimator rather than measurements from a running Ollama model.

### Limitation

The estimator is useful for deciding whether a model is likely to fit before downloading it, but it does not replace an actual runtime measurement.

Actual memory usage can differ because of runtime overhead, backend implementation, GPU/CPU offloading, and other factors.

For this reason, the estimate-versus-reality comparison could not be completed without installing and running Ollama.


## 9. Conclusion

Model size, quantization, context length, and licensing all affect the choice of a local open model.

From the memory experiments, larger parameter counts require more memory. Quantization can reduce the memory required by model weights, making smaller or lower-precision configurations more practical on limited hardware.

Context length also affects memory usage because the KV cache grows as the context increases. The 8B Q4_K_M experiment showed that increasing context from 4K to 32K increased the estimated total memory substantially.

For this machine, the 1.5B Q4_K_M configuration was the most suitable among the tested configurations because its estimated memory usage was approximately 1.20 GB, below the 5.4 GB usable GPU memory budget.

A memory-driven situation would be choosing a smaller or more highly quantized model when the available GPU memory is limited.

A licence-driven situation would be checking the model licence and its conditions before using a model in a commercial application or redistributing it.

Overall, memory estimation should be performed before downloading a model, while the model card and licence should be checked before using it for a real project.