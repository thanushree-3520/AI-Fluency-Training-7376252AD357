# Task 4 – Memory Estimation, Quantization and Licensing

## 1. Scenario

I considered a small local language model scenario with:

- Available memory: 8 GB
- Model size: 7B parameters
- Purpose: Running a small AI assistant
- Context length: 4K tokens

The goal is to estimate whether the model can fit within the available memory.

## 2. Important Concepts

### Model Weights

Model weights are the parameters stored by the model. The memory required for weights depends on the number of parameters and the precision used.

### Quantization

Quantization reduces the number of bytes used for each parameter. This reduces memory usage, although it can involve a quality trade-off.

### KV Cache and Context

The KV cache is additional memory used during model inference. Increasing the context length increases the KV cache requirement.

### Model Card

A model card provides information about a model, such as its capabilities, limitations and licensing information.

### Open-Weight vs Open-Source

Open-weight means the model weights are available, but this does not automatically mean that the entire model is open-source. The exact licence conditions must be checked.

## 3. Memory Estimation

For the example 7B model:

| Model | Parameters | Bytes/Parameter | Context | Weights | KV Cache | Total | Fits? |
|---|---:|---:|---:|---:|---:|---:|---|
| Example 7B | 7B | 0.5 | 4K | 3.5 GB | 1.0 GB | 4.5 GB | Yes |

Available memory = 8 GB.

Estimated total memory = 4.5 GB.

Therefore, the example model fits within the available memory.

## 4. Context Length Comparison

| Context | Weights | KV Cache | Total | Fits? |
|---|---:|---:|---:|---|
| 2K | 3.5 GB | 0.5 GB | 4.0 GB | Yes |
| 4K | 3.5 GB | 1.0 GB | 4.5 GB | Yes |
| 8K | 3.5 GB | 2.0 GB | 5.5 GB | Yes |

Observation:

As context length increases, the KV cache increases. The model weights remain unchanged.

## 5. Quantization Comparison

| Quantization | Weights | KV Cache | Total | Fits? |
|---|---:|---:|---:|---|
| FP16 | 14.0 GB | 1.0 GB | 15.0 GB | No |
| 8-bit | 7.0 GB | 1.0 GB | 8.0 GB | Yes |
| 4-bit | 3.5 GB | 1.0 GB | 4.5 GB | Yes |

Observation:

Lower-precision quantization reduces the memory required for model weights.

FP16 does not fit within the 8 GB memory budget, while 8-bit and 4-bit configurations fit.

## 6. Conclusion

Memory requirements depend on model size, precision, context length and runtime requirements.

Quantization can make a model fit into a smaller memory budget. However, the final model choice should also consider model capabilities, licensing conditions and the intended use.
## 7. Open Model Comparison

The following three models were selected from different model families.

| Model | Parameters | Context | Licence | Commercial Use | Tool Calling | Ollama/GGUF |
|---|---:|---:|---|---|---|---|
| Llama 3.2 | To verify | To verify | To verify | To verify | To verify | To verify |
| Qwen2.5 | To verify | To verify | To verify | To verify | To verify | To verify |
| Gemma 3 | To verify | To verify | To verify | To verify | To verify | To verify |

### Model Card and Licence Verification

The model-card and licence information must be checked from the official sources before making the final recommendation.

The date on which each source was checked will also be recorded.

## 8. Suitability and Final Recommendation

For the example scenario, the available memory is 8 GB.

The 7B model with 4-bit quantization requires an estimated 4.5 GB including the assumed KV cache, so it fits within the 8 GB memory budget.

The context comparison shows that increasing context length increases KV cache memory. The quantization comparison shows that reducing precision significantly reduces the memory required for model weights.

For a memory-limited system, a smaller quantized model is therefore more suitable than the same model using FP16.

## 9. Limitations

The memory values in this task are estimates. Actual memory usage can differ because of runtime overhead, model architecture, implementation, context usage and other system requirements.

Ollama was not installed in this environment, so actual `ollama list` and `ollama ps` measurements were not available. Therefore, no local runtime measurement is claimed as actual hardware evidence.

The model licence and model-card information should be checked from the official sources before using a model commercially.

## 10. Conclusion

Model size, parameter precision, context length and licensing all affect the suitability of an open model.

The estimator provides a simple way to determine whether an estimated configuration fits within a memory budget. Quantization can substantially reduce memory requirements, while larger context lengths increase KV-cache requirements.

The final model choice should consider not only memory, but also model capability, licence conditions, intended use and available hardware.