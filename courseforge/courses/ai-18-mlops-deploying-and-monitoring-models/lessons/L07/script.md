# L07 Input Validation, Errors and Logging | Presenter Script

Course: AI-18 · Video: 5 min · Words: 647

## Hook
A client sends an alcohol value of forty instead of twelve point five. Your model does not complain. It returns a confident prediction for a wine that cannot exist. Nobody sees an error, and nobody can find the request later.

## Explain
In the last lesson, we built a prediction API. Today we close two gaps: bad input and missing records. A model will produce a number for almost any input. It cannot tell you that the input makes no sense. So the API must check the data before the model sees it.

Reject three kinds of bad input early. Missing fields, where a required feature is absent. Wrong types, such as the word high where a number is expected. And values outside the training range, where the model's behaviour is unknown. Take the limits from your own training data, and write down where they came from.

With Pydantic, you add these rules to the schema. Each feature gets a lower and an upper limit. A setting forbids extra fields, which also stops clients from sending personal data by mistake. FastAPI then returns status four two two with a clear message, and the model is never called.

The second job is structured logging. Write one JSON line per prediction, with the same fields every time. Include a request ID, a timestamp, the model version, the input features, the prediction and the latency. Later in the course, you will read these lines to build a dashboard and to detect drift.

Never log personal data, such as names, emails, addresses or free-text notes. If a feature is personal, log a coarse group, or leave it out.

Think of an airport. Validation is the security check at the entrance. It stops items that should not go on the plane. Logging is the boarding record. It tells you later exactly who boarded which flight, without storing their private conversations.

## Demonstrate
Let's watch Chidi Okafor, who maintains a hypothetical price prediction API for a farm marketplace in Lagos. He replaces the wine schema with the validated version, adds the logging code, restarts the server and opens the docs page.

First, he sends an alcohol value of forty. The answer is four two two: input should be less than or equal to fifteen. Then he removes sulphates. Four two two again: field required.

Next, he sets citric acid to the word high. The service says the input should be a valid number. Finally, he adds an email field. The answer: extra inputs are not permitted. Four clear errors, and the model was never called.

Now he sends a valid request, and opens the log file. There is one new line. It shows the event, model version one, the four features, a probability of zero point nine three one eight, and a latency of about nineteen milliseconds on our machine.

Two common mistakes. The first is free-text logs. A person can read them, but a program cannot analyse them reliably. The second is logging the whole raw request, just in case. That often captures personal data. Log a fixed list of fields that you chose on purpose.

## Recap
Let's recap. First, validate input in the schema, so missing fields, wrong types and out-of-range values return a clear four two two before the model runs. Second, write one structured JSON line per prediction, with a request ID, timestamp, model version, inputs, prediction and latency. Third, never log personal data, and forbid unexpected fields.

## CTA
In the exercise below this video, you will add these rules to your own service and send ten test requests, six valid and four bad. Then you check that the log has exactly six clean lines. It takes about thirty-five minutes. Your capstone monitoring will read this log.

In the next lesson, we package this service so it runs the same way everywhere, in Containerising the Model Service. See you there.

## Thumbnail
Headline: Stop Bad Inputs Early
Image: Navy background, a checkpoint gate stopping a red card labelled 40 while a teal card labelled 12.5 passes into a log file, headline in teal Inter Bold.

## Production Notes
- [VERSION] Pydantic v2 syntax (Field ge/le, ConfigDict extra=forbid) and the exact 422 message texts were tested with Pydantic 2.13.5 and FastAPI 0.141.1; Pydantic v1 used different syntax and messages. Re-check the message wording before recording.
- The feature limits come from the synthetic fallback data and are approximate; learners use their own training data.
- The logged line (probability 0.9318, latency 18.83 ms, model_version 1) is a real output; latency is spoken with 'on our machine'.
- Screen recording: the test email in step 6 is the dummy a@b.c; never type a real person's email or name.
- Chidi Okafor and the Lagos farm marketplace are hypothetical.
