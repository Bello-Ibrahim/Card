# L07 Streaming Responses

Course: AI-14 · Module: M2 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Two apps take exactly 12 seconds to write the same answer. In the first, the user stares at a spinner for 12 seconds. In the second, words start to appear after about one second. The second app feels faster, although it is not.

## Explanation
Without streaming, the API waits until the whole reply is finished and then sends it in one response. With **streaming**, the server sends the reply in small pieces while the model generates it. Your app can show each piece immediately.

Two times matter to users:

- **Time to first token (TTFT):** how long until the first text appears. Streaming makes this short.
- **Total time:** how long until the reply is complete. Streaming does not make this shorter.

Streaming does not change the cost. You pay for the same input and output tokens.

**The streaming helper.** The Python SDK has a helper that handles the low-level events for you. You open a stream in a `with` block and loop over `text_stream`, which gives you only the new text pieces. [VERSION]

```python
with client.messages.stream(
    model=MODEL,
    max_tokens=1000,
    messages=[{"role": "user", "content": question}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    final = stream.get_final_message()

print("\nStop reason:", final.stop_reason)
print("Tokens:", final.usage.input_tokens, final.usage.output_tokens)
```

**The final message.** After the loop, `get_final_message()` returns the complete message, in the same form as a normal response: content, stop reason and usage. Use it to log tokens and cost (your L04 helper works unchanged) and to save the reply to the chat history.

**Under the helper**, the API sends a series of named events: the message starts, content blocks start, text deltas arrive, blocks stop, and the message stops with final usage. You only need these events for advanced cases, such as streaming tool calls. Event names are listed in the streaming docs. [VERSION]

**When to stream.** Stream anything a person reads while waiting: chat replies, drafts, summaries. Streaming is also recommended for long outputs, because very long non-streaming requests can hit HTTP timeouts. For short background jobs, such as extracting fields from a batch of invoices, a normal request is simpler.

**Analogy:** Streaming is like a live sports commentary on the radio compared with a match report in tomorrow's newspaper. The match lasts the same time either way. With the radio, you follow it as it happens; with the newspaper, you wait and then get everything at once.

## Worked Example
Kenji Watanabe builds a legal research helper for a small law firm in Osaka, Japan. Lawyers ask for plain-language explanations of contract terms, and replies are often 400 to 600 words long. Without streaming, lawyers complained that the tool "freezes".

He adds timing to the streaming loop:

```python
import time

start = time.perf_counter()
first = None
with client.messages.stream(model=MODEL, max_tokens=1200,
                            system=SYSTEM, messages=messages) as stream:
    for text in stream.text_stream:
        if first is None:
            first = time.perf_counter() - start
        print(text, end="", flush=True)
    final = stream.get_final_message()
total = time.perf_counter() - start
print(f"\nTTFT {first:.2f}s, total {total:.2f}s, "
      f"output tokens {final.usage.output_tokens}")
```

Example output after a long answer:

```text
TTFT 0.9s, total 11.4s, output tokens 610
```

The total time is still over 11 seconds, but lawyers now start reading in under a second (example numbers). Kenji logs TTFT and total time for every call, so he can see later whether a model or prompt change makes the tool feel slower.

## Common Mistake
Many developers stream to the screen but forget the end of the stream. They build the reply by joining text pieces and never read the final message, so they have no stop reason and no token usage. Their cost log shows nothing for streamed calls, and cut-off replies look complete. Always call `get_final_message()` after the loop, check its stop reason and log its usage.

## Key Takeaways
1. Streaming shows text as it is generated. It shortens the time to first token, but not the total time or the cost.
2. Use the SDK's streaming helper and loop over `text_stream` to get the text pieces.
3. After the loop, get the final message to check the stop reason, log usage and save the reply to the history.

## Hands-on Exercise
**Task:** Stream a long answer to the terminal, then record the time to the first token and the total time.
**Tools:** Your L02 setup; a terminal; the current streaming docs. [VERSION]
**Steps:**
1. Write a question that needs a long answer, for example "Explain in about 400 words how a bill of lading works."
2. Copy the worked example code and set max_tokens to 1000.
3. Run it and watch the text appear in the terminal.
4. Record the TTFT, the total time and the output tokens.
5. Run the same question without streaming (`messages.create`) and record the total time until anything appears.
6. Log both calls with your L04 helper, using the final message for the streamed call.
7. Write two sentences: which version felt faster, and did the cost differ?
**What good looks like:** Text appears in pieces in the terminal. You have TTFT and total time for the streamed call, the waiting time for the normal call, and two cost log rows with similar token counts.
**Time:** about 25 minutes

## Review Flags
- [VERSION] The `messages.stream()` helper, `text_stream`, `get_final_message()` and the names of streaming events must be checked against the current SDK docs.
- The timing numbers in the worked example and in the Hook are illustrative, not measured.
