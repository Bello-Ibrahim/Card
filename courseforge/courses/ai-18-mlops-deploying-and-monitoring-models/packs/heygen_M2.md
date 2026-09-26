# HeyGen Batch Pack: AI-18 M2 (Serving Models as APIs)

Course: MLOps: Deploying and Monitoring Models. Make one HeyGen video per lesson below, using these settings for every video.

| Setting | Value |
|---|---|
| Avatar | **Vaness** (standard avatar), ID `1bd001e7e50f421d891986aad5c8bbd2` |
| Voice | `1bd001e7e50f421d891986aad5c8bbd2` (the same ID as the avatar: if HeyGen does not list it as a voice, use Vaness's paired English voice and record its ID in DECISIONS.md) |
| Background | Solid colour **#00FF00** (pure green, no gradient, no image) |
| Resolution | 1080p (1920×1080) |
| Aspect ratio | 16:9 |
| Avatar framing | Centred, head and shoulders, same size in every lesson |
| Captions/subtitles | **Off** (captions are added in Stage 6) |
| Music | Off |
| Speed | Normal (1.0×) |

How to paste: copy the whole text block for a lesson into a single HeyGen scene. Each blank line is a natural pause. Do not add or change words, because the edit is timed to this exact narration.

Save each finished video with the exact filename shown, and upload it to `/incoming/`.

## L06 Designing a Prediction API with FastAPI

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M2_L06_presenter.mp4`
- **Expected length:** about 4.8 minutes (669 words). The quality gate accepts ±10%.

```text
Your model lives in the registry. The mobile team, the web team and a partner company all want predictions, and none of them uses Python. How do you give all of them the same model, safely, through one door?

Welcome to week two. Last time, we registered our champion model. Now we serve it. The usual answer is a small web service, an API, that receives JSON and returns a prediction. FastAPI is a free Python framework that suits this well. It uses Python type hints to check the input, and it builds interactive documentation for you.

A good prediction API has four parts. First, a predict endpoint that takes one input and returns one prediction. Second, a health endpoint that answers quickly and says whether the service and the model are ready. Container platforms and load balancers call it all the time.

Third, request and response schemas. They define the exact fields and types, reject bad input, and appear in the documentation. Fourth, load the model once, when the service starts, not on every request. Loading a model can take seconds. Doing it for every request makes the service slow.

The model location comes from an environment variable, not from the code. So the same code can load the registry alias on your laptop, and a local model folder inside a container later. The same goes for any server address. No address or password ever appears in the code.

Picture the service window of a restaurant kitchen. Customers never enter the kitchen. They order from a fixed menu, which is the schema. The kitchen was prepared before opening, which is the model loaded at start-up. And a sign on the window says whether it is open. That is the health check.

Let's watch Mei Nakamura, a data scientist at a hypothetical agricultural technology start-up in Sapporo, Japan. She installs FastAPI and Uvicorn, the server that runs it, and adds both to the requirements file. Then she opens her app file, which contains the code you just saw.

She points MLflow at the local database through an environment variable, and starts the service. In the browser, the health page reports status ok, and model loaded, true. If the model had failed to load, this page would say so at once, before any client sent a real request.

Now the best part. She opens the docs page. FastAPI has built it automatically, with both endpoints and the input schema. She expands the predict endpoint, clicks Try it out, and sends one wine, with an alcohol value of twelve point five.

The response comes back. Good wine, true, with a probability of zero point nine three one eight. That is the real answer from our champion model, trained on the synthetic data. Every client, in any language, can now call the same model in the same way. The mobile team, the web team and the partner company all use one door, and one set of rules.

A common mistake is to load the model inside the predict function. It works in a quick test, so the problem stays hidden. Under real traffic, every request reads the model again, latency rises sharply, and the registry gets many unnecessary calls. Load once at start-up, and let the health endpoint report whether loading worked.

Let's recap. First, a prediction API needs a predict endpoint, a health endpoint and clear request and response schemas. Second, FastAPI uses these schemas to check input and to build interactive documentation. Third, load the model once at start-up, and pass its location and any server address through environment variables, not code.

In the exercise below this video, you will build this service for your own registered model. You will test three inputs through the docs page, and then send one with a missing field to see what happens. It takes about thirty-five minutes, and this service is the heart of your capstone.

That missing field leads straight to the next lesson, Input Validation, Errors and Logging. See you there.
```

## L07 Input Validation, Errors and Logging

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M2_L07_presenter.mp4`
- **Expected length:** about 4.6 minutes (642 words). The quality gate accepts ±10%.

```text
A client sends an alcohol value of forty instead of twelve point five. Your model does not complain. It returns a confident prediction for a wine that cannot exist. Nobody sees an error, and nobody can find the request later.

In the last lesson, we built a prediction API. Today we close two gaps: bad input and missing records. A model will produce a number for almost any input. It cannot tell you that the input makes no sense. So the API must check the data before the model sees it.

Reject three kinds of bad input early. Missing fields, where a required feature is absent. Wrong types, such as the word high where a number is expected. And values outside the training range, where the model's behaviour is unknown. Take the limits from your own training data, and write down where they came from.

With Pydantic, you add these rules to the schema. Each feature gets a lower and an upper limit. A setting forbids extra fields, which also stops clients from sending personal data by mistake. FastAPI then returns status four two two with a clear message, and the model is never called.

The second job is structured logging. Write one JSON line per prediction, with the same fields every time. Include a request ID, a timestamp, the model version, the input features, the prediction and the latency. Later in the course, you will read these lines to build a dashboard and to detect drift.

Never log personal data, such as names, emails, addresses or free-text notes. If a feature is personal, log a coarse group, or leave it out.

Think of an airport. Validation is the security check at the entrance. It stops items that should not go on the plane. Logging is the boarding record. It tells you later exactly who boarded which flight, without storing their private conversations.

Let's watch Chidi Okafor, who maintains a hypothetical price prediction API for a farm marketplace in Lagos. He replaces the wine schema with the validated version, adds the logging code, restarts the server and opens the docs page.

First, he sends an alcohol value of forty. The answer is four two two: input should be less than or equal to fifteen. Then he removes sulphates. Four two two again: field required.

Next, he sets citric acid to the word high. The service says the input should be a valid number. Finally, he adds an email field. The answer: extra inputs are not permitted. Four clear errors, and the model was never called.

Now he sends a valid request, and opens the log file. There is one new line. It shows the event, model version one, the four features, a probability of zero point nine three one eight, and a latency of about nineteen milliseconds on our machine.

Two common mistakes. The first is free-text logs. A person can read them, but a program cannot analyse them reliably. The second is logging the whole raw request, just in case. That often captures personal data. Log a fixed list of fields that you chose on purpose.

Let's recap. First, validate input in the schema, so missing fields, wrong types and out-of-range values return a clear four two two before the model runs. Second, write one structured JSON line per prediction, with a request ID, timestamp, model version, inputs, prediction and latency. Third, never log personal data, and forbid unexpected fields.

In the exercise below this video, you will add these rules to your own service and send ten test requests, six valid and four bad. Then you check that the log has exactly six clean lines. It takes about thirty-five minutes. Your capstone monitoring will read this log.

In the next lesson, we package this service so it runs the same way everywhere, in Containerising the Model Service. See you there.
```

## L08 Containerising the Model Service

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M2_L08_presenter.mp4`
- **Expected length:** about 4.7 minutes (647 words). The quality gate accepts ±10%.

```text
Your API runs on your laptop. Will it run on the server with the same Python, the same libraries and the same model file? A container says yes. But a careless container can be slow, large, and a security risk.

In the last lesson, our API learned to reject bad input and to log every prediction. Now we package it. You already know basic Docker, so we focus on four choices that matter most for a production model service.

First, a small base image. A slim Python image contains much less than the full one, so it downloads faster and has fewer packages that could contain security problems. Second, a multi-stage build. The first stage installs the dependencies. The final stage copies only the results. Build tools and caches stay behind.

Third, a non-root user. By default, processes in a container run as root. If an attacker breaks into the service, a normal user limits what they can do. Fourth, decide where the model comes from.

You can copy the model into the image. Then the image is self-contained, starts fast, and each image tag means exactly one model. Or you can load it from the registry at start-up. One image serves any version, but start-up depends on the registry, and the container needs credentials. In this course we copy the model in, because rollback becomes simple: run the previous image.

One firm rule. Never put secrets in a Dockerfile or an image. Anyone who can pull the image can read its layers. Pass secrets when the container runs, and keep that file out of Git.

A container is like a shipping container for goods. Everything the product needs travels inside, so it arrives the same at every port. And a multi-stage build packs the product, but leaves the factory tools at home.

Let's watch Lars Eriksson, a platform engineer at a hypothetical energy company in Gothenburg, Sweden. First, he exports the champion model from the registry to a local model folder. Then he creates a docker ignore file that keeps out the virtual environment, the database, the data, the logs, the Git folder and any environment file.

Now the Dockerfile, in two stages. The build stage turns the requirements into ready packages. The runtime stage installs them, creates a normal user, copies only the app and the model folder, and switches to that user before starting the server.

He builds the image with a version tag, and runs it. In the browser, the health page answers from inside the container.

Next, he lists the image size, and compares it with a single-stage build on the full Python image. The slim, multi-stage image is clearly smaller. Record your own sizes, because they depend on your requirements and platform. Last, he checks the user. The container prints app user, not root.

A common mistake is to copy the whole project folder into the image. That silently adds the virtual environment, the database, log files, and sometimes a file with passwords. The image grows, and secrets leak to anyone who pulls it. Copy only what the service needs, and keep the ignore file as a second safety net.

Let's recap. First, use a slim base image, a multi-stage build and a non-root user for model services. Second, copying the model into the image makes each tag mean one model and makes rollback simple, while loading from the registry is more flexible but adds a start-up dependency. Third, never put secrets in an image.

In the exercise below this video, you will write a Dockerfile for your service, build it, and shrink the image with at least one technique. Record the size before and after. It takes about forty minutes, and your capstone will publish exactly this image.

In the next lesson, we measure how fast this container really is, in Batch versus Online Serving and Performance. See you there.
```

## L09 Batch vs Online Serving and Performance

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M2_L09_presenter.mp4`
- **Expected length:** about 4.6 minutes (635 words). The quality gate accepts ±10%.

```text
Does your model need to answer in fifty milliseconds, or is tomorrow morning fast enough? The answer changes your architecture, your costs, and what you must measure.

In the last lesson, we packed our API into a container. Now we ask how it should serve, and how fast it is. There are two main ways to serve predictions. Online serving answers one request at a time, while a user or a system waits. Our API is online serving. It needs low latency, and it must stay available all day.

Batch serving scores many rows together, on a schedule, and stores the results in a file or a table. Nobody waits for a single answer. It is simpler to run, easier to retry, and usually cheaper. But the predictions are only as fresh as the last run. Choose online when the input exists only at request time. Choose batch when a delay of hours is fine.

For online services, measure two things under load. First, latency percentiles. The median is the typical request. The ninety-fifth percentile, or p ninety-five, is the time that ninety-five percent of requests stay under. Averages hide slow requests, and users notice the slow ones. Second, throughput: how many requests per second the service handles without errors.

Think of a coffee bar and a bakery. The coffee bar makes each drink while the customer waits. That is online. The bakery bakes all the bread at night for the morning. That is batch. It is efficient, but it cannot make a fresh loaf at three in the afternoon for one customer.

Katarzyna Nowak leads data science at a hypothetical online shop in Kraków, Poland. She owns two models. A delivery time model shows arrives in two days on the checkout page. The customer is waiting, so it needs online serving. A monthly churn score gives marketing a list once a month. One scheduled batch job is enough.

She load-tests the online service with Locust, a free, open-source tool. A short Python file describes one user who keeps sending a valid wine to the predict endpoint. She starts the service, starts Locust, and opens its web page.

The first test uses five users for twenty seconds. On our machine, the service handled sixteen requests per second, with a median of six milliseconds and a p ninety-five of eleven milliseconds.

Then she repeats with fifty users. Now it handled one hundred and forty-five requests per second. The median rose only to nine milliseconds, but the p ninety-five nearly tripled, to thirty milliseconds. That is queueing, and an average from one user would hide it.

Finally, the batch path. A short script loads the same champion model, scores a whole file, and writes a probability column. It prints scored five hundred rows. Because both paths use the same model version, online and batch predictions agree.

The common mistake is to report only the average latency from a single user. Always test at more than one load level, report the median and p ninety-five, and test the way you will deploy. Your numbers will differ with hardware, model and container settings.

Let's recap. First, online serving answers each request at once, while batch serving scores many rows on a schedule, and is simpler and cheaper when a delay is acceptable. Second, measure median latency, p ninety-five latency and throughput at more than one load level. Third, use the same registered model version for both paths.

In the exercise below this video, you will load-test your own container at two load levels, record the median and p ninety-five, and write a batch scoring script for the same model. It takes about forty minutes.

In the next lesson, we decide where models run and how new versions reach users safely, in Deployment Targets and Release Strategies. See you there.
```

## L10 Deployment Targets and Release Strategies

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_M2_L10_presenter.mp4`
- **Expected length:** about 5.2 minutes (718 words). The quality gate accepts ±10%.

```text
You have a new model version that scored better offline. Do you switch all users to it at once? If it fails, how fast can you switch back, and who decides? A release strategy answers these questions before anything goes wrong.

In the last lesson, we measured our container's speed. Now, where does it run? There are three common targets. A single server is simple, but you handle restarts, updates and scaling yourself. A container platform restarts failed containers, runs several copies and can shift traffic between versions, but it takes more set-up and knowledge.

A managed ML service from a cloud provider does much of the serving for you, but you depend on its features, limits and prices. Free tiers are useful for learning, but they change often. Check the current terms, and never rely on a free tier for a critical service.

Now, how do new versions reach users? Blue-green runs the old and new versions side by side, then switches all traffic at once. Rollback is switching back. Canary sends a small share of real traffic, say five percent, to the new version. You watch errors, latency and prediction quality, then increase the share step by step.

Shadow sends a copy of real traffic to the new version, but users only see the old version's answers. You compare both sets of predictions with no risk to users, but serving costs double for that period. And every release needs a rollback plan: what signal triggers it, who can trigger it, and how.

A rollback trigger must be measurable. For example, an error rate above two percent for ten minutes. Choose the numbers for your own service. These are examples, not standards. With our registry and image tags, rollback means running the previous image, or moving the champion alias back.

Think of a restaurant chain changing a recipe. Blue-green prepares a second kitchen and switches all orders at once. Canary serves the new recipe in one branch first. Shadow cooks the new dish in the back for every order and tastes it, while guests still receive the old dish.

Let's look at two hypothetical teams. In Kisumu, Kenya, Doctor Achieng Odhiambo's team uses a model that suggests how urgent each patient is, to help nurses order the waiting list. A nurse always makes the final decision. But a wrong new model could delay urgent care, so the risk to people is high.

So the team starts with shadow deployment. For two weeks, the new model scores every case, but only the old suggestion appears on screen. Clinicians review the cases where the two models disagree. Only then do they release with blue-green, keeping the old version ready. Local regulations may also require approval before any change.

In Recife, Brazil, Lucas Ferreira's team runs product recommendations for an online fashion shop. A weaker recommendation costs some sales, but harms nobody, and they want to learn from real clicks quickly. They choose a canary: five percent of traffic for one day, then twenty-five percent, then everyone.

Their rollback trigger is simple. If the canary group's click-through rate falls clearly below the old version, or the p ninety-five latency goes over the page's budget, they switch back. The same technology leads to different choices, because the cost of a mistake is different.

A common mistake is to write a rollback plan but never test it. Then, in the first real incident, the old image was deleted, or nobody has permission to deploy. Practise the rollback on a normal day, and keep the previous image and model version available.

Let's recap. First, models can run on a single server, a container platform or a managed ML service, and each trades control for convenience. Second, blue-green, canary and shadow releases reduce risk in different ways, so choose by the cost of a mistake. Third, every release needs a measurable rollback trigger and a tested rollback procedure.

In the exercise below this video, you will choose a release strategy and a rollback trigger for three scenarios, a bank in Morocco, a news site in Indonesia and a water utility in Peru. It takes about twenty-five minutes. Your capstone demo will include a real rollback.

That completes week two. Next week we automate everything, starting with Testing ML Code and Models. See you there.
```
