
import time

MODEL = "study-buddy"

def generate_response(prompt):
    prompt_lower = prompt.lower()

    if "variable" in prompt_lower:
        return "A variable stores a value. Example: age = 18"
    elif "loop" in prompt_lower:
        return "A loop repeats instructions. Example: for i in range(3): print(i)"
    elif "api" in prompt_lower:
        return "An API allows two software applications to communicate."
    else:
        return "I am Study Buddy. Ask me about a programming concept!"

def run_non_streaming(prompt):
    print("\n--- NON-STREAMING ---")
    print("Model:", MODEL)
    print("Prompt:", prompt)

    start = time.perf_counter()
    answer = generate_response(prompt)
    total_time = time.perf_counter() - start

    print("Answer:", answer)
    print("Total execution time:", round(total_time, 6), "seconds")
    print("Mode: Local mock simulation (not a real AI model)")

def run_streaming(prompt):
    print("\n--- STREAMING SIMULATION ---")
    print("Prompt:", prompt)

    start = time.perf_counter()
    answer = generate_response(prompt)
    first_token_time = None

    print("Answer: ", end="", flush=True)

    for word in answer.split():
        if first_token_time is None:
            first_token_time = time.perf_counter()
        print(word, end=" ", flush=True)
        time.sleep(0.05)

    total_time = time.perf_counter() - start

    print("\nTTFT (simulation):",
          round(first_token_time - start, 3), "seconds")
    print("Total time:", round(total_time, 3), "seconds")

def main():
    prompts = [
        "Explain a variable with one simple example.",
        "What is an API?",
        "Explain a loop using a small example."
    ]

    for prompt in prompts:
        run_non_streaming(prompt)

    print("\n=== REPEATED PROMPT ===")
    run_non_streaming(prompts[0])

    run_streaming(prompts[1])

if __name__ == "__main__":
    main()