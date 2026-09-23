# L06 Designing a Prediction API with FastAPI | Presenter Script

Course: AI-18 · Video: 5 min · Words: 674

## Hook
Your model lives in the registry. The mobile team, the web team and a partner company all want predictions, and none of them uses Python. How do you give all of them the same model, safely, through one door?

## Explain
Welcome to week two. Last time, we registered our champion model. Now we serve it. The usual answer is a small web service, an API, that receives JSON and returns a prediction. FastAPI is a free Python framework that suits this well. It uses Python type hints to check the input, and it builds interactive documentation for you.

A good prediction API has four parts. First, a predict endpoint that takes one input and returns one prediction. Second, a health endpoint that answers quickly and says whether the service and the model are ready. Container platforms and load balancers call it all the time.

Third, request and response schemas. They define the exact fields and types, reject bad input, and appear in the documentation. Fourth, load the model once, when the service starts, not on every request. Loading a model can take seconds. Doing it for every request makes the service slow.

The model location comes from an environment variable, not from the code. So the same code can load the registry alias on your laptop, and a local model folder inside a container later. The same goes for any server address. No address or password ever appears in the code.

Picture the service window of a restaurant kitchen. Customers never enter the kitchen. They order from a fixed menu, which is the schema. The kitchen was prepared before opening, which is the model loaded at start-up. And a sign on the window says whether it is open. That is the health check.

## Demonstrate
Let's watch Mei Nakamura, a data scientist at a hypothetical agricultural technology start-up in Sapporo, Japan. She installs FastAPI and Uvicorn, the server that runs it, and adds both to the requirements file. Then she opens her app file, which contains the code you just saw.

She points MLflow at the local database through an environment variable, and starts the service. In the browser, the health page reports status ok, and model loaded, true. If the model had failed to load, this page would say so at once, before any client sent a real request.

Now the best part. She opens the docs page. FastAPI has built it automatically, with both endpoints and the input schema. She expands the predict endpoint, clicks Try it out, and sends one wine, with an alcohol value of twelve point five.

The response comes back. Good wine, true, with a probability of zero point nine three one eight. That is the real answer from our champion model, trained on the synthetic data. Every client, in any language, can now call the same model in the same way. The mobile team, the web team and the partner company all use one door, and one set of rules.

A common mistake is to load the model inside the predict function. It works in a quick test, so the problem stays hidden. Under real traffic, every request reads the model again, latency rises sharply, and the registry gets many unnecessary calls. Load once at start-up, and let the health endpoint report whether loading worked.

## Recap
Let's recap. First, a prediction API needs a predict endpoint, a health endpoint and clear request and response schemas. Second, FastAPI uses these schemas to check input and to build interactive documentation. Third, load the model once at start-up, and pass its location and any server address through environment variables, not code.

## CTA
In the exercise below this video, you will build this service for your own registered model. You will test three inputs through the docs page, and then send one with a missing field to see what happens. It takes about thirty-five minutes, and this service is the heart of your capstone.

That missing field leads straight to the next lesson, Input Validation, Errors and Logging. See you there.

## Thumbnail
Headline: Your Model, One Door
Image: Navy background, a service window with three arrows (phone, browser, partner building) pointing into it and a teal JSON response coming out, headline in teal Inter Bold.

## Production Notes
- [VERSION] Code uses Pydantic v2 (model_dump, model_config) and the FastAPI lifespan hook; the older startup event is deprecated. Tested with FastAPI 0.141.1 and Pydantic 2.13.5; check current releases and the look of the /docs page before recording.
- [VERSION] The uvicorn command and MLflow model loading were tested with MLflow 3.16.1.
- The response {"good_wine": true, "probability": 0.9318} is a real output from the champion model trained on the synthetic fallback data; it must match on screen.
- Screen recording: the MLFLOW_TRACKING_URI shown is a local SQLite file only. Never show a remote tracking server address, password or token in the terminal or editor.
- Mei Nakamura and the Sapporo start-up are hypothetical.
