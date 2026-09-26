# Screen Demo Pack: AI-14 L09 Tool Use: Letting the Model Call Your Functions

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 9

- **Filename:** `ai-14-building-apps-with-llm-apis_L09_screen_1.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Open tracking.py in VS Code
2. Highlight the SHIPMENTS dictionary with VN-4471 and VN-5820
3. Highlight the tools list: name, description and input_schema with tracking_code required
4. Highlight the get_shipment_status function

**Narration over this clip (for pacing)**

> At the top of her file is the dictionary with two invented shipments. Then the tool definition, with a clear description and a schema that requires a tracking code. The function itself just looks up the code.

## Clip 2: scene 10

- **Filename:** `ai-14-building-apps-with-llm-apis_L09_screen_2.mp4`
- **Target length:** about 16 seconds

**Steps**

1. Highlight messages.create with tools=tools
2. Add print(response.content) after the first call and run the script
3. Show the tool_use block and point to its id, name and input {"tracking_code": "VN-4471"}
4. Show stop_reason: tool_use

**Narration over this clip (for pacing)**

> She sends the question with the tools list, and prints the reply content. On screen, you can see the tool use block, with its ID, the tool name and the input, a parsed dictionary with the tracking code.

## Clip 3: scene 11

- **Filename:** `ai-14-building-apps-with-llm-apis_L09_screen_3.mp4`
- **Target length:** about 22 seconds

**Steps**

1. Highlight while response.stop_reason == "tool_use"
2. Highlight messages.append with role assistant and response.content
3. Highlight block.input["tracking_code"] and the tool_result with tool_use_id=block.id
4. Highlight the second messages.create call

**Narration over this clip (for pacing)**

> Now the loop. While the stop reason is tool use, she appends the full reply as the assistant turn. For each tool use block, she runs the function, reading the input by key, and builds a tool result with the same ID. She sends the results back and calls the API again.

## Clip 4: scene 12

- **Filename:** `ai-14-building-apps-with-llm-apis_L09_screen_4.mp4`
- **Target length:** about 18 seconds

**Steps**

1. Run the full script and show the final answer (labelled 'example output')
2. Change the question to 'What are your opening hours?' and run again
3. Show that no tool_use block appears and the model answers directly

**Narration over this clip (for pacing)**

> She runs it. You'll see something like, your parcel is out for delivery in Da Nang and should reach you soon. Then she asks about opening hours. The model answers without calling the tool, because the description says it is for tracking codes.

## Production notes for this lesson

- [VERSION] Tool-definition options (strict mode, tool choice and other fields) and the exact response block format (tool_use, tool_result, tool_use_id) must be checked against the current tool-use docs before recording.
- The final answer about parcel VN-4471 is example output; the voiceover says 'something like'.
- Nguyen Thi Lan, the Ho Chi Minh City courier company and all tracking codes are invented; the shipment data is a local dictionary, not a real system.
