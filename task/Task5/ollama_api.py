import requests
import time
import json

URL = "http://localhost:11434/api/generate"
MODEL = "college-assistant"


def check_ollama():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=3)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def run_non_streaming(prompt):
    print("\n=== NON-STREAMING ===")

    start = time.time()

    try:
        response = requests.post(
            URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )

        end = time.time()

        if response.status_code != 200:
            print("Ollama request failed.")
            print("Status code:", response.status_code)
            return

        data = response.json()

        print("Prompt:", prompt)
        print("Response:", data.get("response", ""))
        print("Total time:", round(end - start, 2), "seconds")

    except requests.exceptions.ConnectionError:
        print("Ollama server is not available.")
        print("Expected address: http://localhost:11434")


def run_streaming(prompt):
    print("\n=== STREAMING ===")

    start = time.time()
    first_token_time = None
    full_response = ""

    try:
        response = requests.post(
            URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": True
            },
            stream=True,
            timeout=30
        )

        if response.status_code != 200:
            print("Ollama request failed.")
            print("Status code:", response.status_code)
            return

        for line in response.iter_lines():

            if line:
                data = json.loads(line.decode("utf-8"))

                token = data.get("response", "")

                if first_token_time is None and token:
                    first_token_time = time.time()

                print(token, end="", flush=True)

                full_response += token

                if data.get("done"):
                    break

        end = time.time()

        print()

        ttft = (
            first_token_time - start
            if first_token_time
            else 0
        )

        total_time = end - start

        print("TTFT:", round(ttft, 2), "seconds")
        print("Total time:", round(total_time, 2), "seconds")

        if total_time > 0:
            words = len(full_response.split())
            print(
                "Approximate words/second:",
                round(words / total_time, 2)
            )

    except requests.exceptions.ConnectionError:
        print("Ollama server is not available.")
        print("Streaming test could not be performed.")


if __name__ == "__main__":

    print("=== Ollama Availability Check ===")

    if not check_ollama():
        print("Ollama is not installed/running on this computer.")
        print("REST API tests cannot be executed.")
        print("This is documented as an environment limitation.")
    else:
        prompt = "Explain what an AI agent is in two simple sentences."

        run_non_streaming(prompt)
        run_streaming(prompt)