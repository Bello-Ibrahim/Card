# L09 Batch vs Online Serving and Performance | Presenter Script

Course: AI-18 · Video: 5 min · Words: 647

## Hook
Does your model need to answer in fifty milliseconds, or is tomorrow morning fast enough? The answer changes your architecture, your costs, and what you must measure.

## Explain
In the last lesson, we packed our API into a container. Now we ask how it should serve, and how fast it is. There are two main ways to serve predictions. Online serving answers one request at a time, while a user or a system waits. Our API is online serving. It needs low latency, and it must stay available all day.

Batch serving scores many rows together, on a schedule, and stores the results in a file or a table. Nobody waits for a single answer. It is simpler to run, easier to retry, and usually cheaper. But the predictions are only as fresh as the last run. Choose online when the input exists only at request time. Choose batch when a delay of hours is fine.

For online services, measure two things under load. First, latency percentiles. The median is the typical request. The ninety-fifth percentile, or p ninety-five, is the time that ninety-five percent of requests stay under. Averages hide slow requests, and users notice the slow ones. Second, throughput: how many requests per second the service handles without errors.

Think of a coffee bar and a bakery. The coffee bar makes each drink while the customer waits. That is online. The bakery bakes all the bread at night for the morning. That is batch. It is efficient, but it cannot make a fresh loaf at three in the afternoon for one customer.

## Demonstrate
Katarzyna Nowak leads data science at a hypothetical online shop in Kraków, Poland. She owns two models. A delivery time model shows arrives in two days on the checkout page. The customer is waiting, so it needs online serving. A monthly churn score gives marketing a list once a month. One scheduled batch job is enough.

She load-tests the online service with Locust, a free, open-source tool. A short Python file describes one user who keeps sending a valid wine to the predict endpoint. She starts the service, starts Locust, and opens its web page.

The first test uses five users for twenty seconds. On our machine, the service handled sixteen requests per second, with a median of six milliseconds and a p ninety-five of eleven milliseconds.

Then she repeats with fifty users. Now it handled one hundred and forty-five requests per second. The median rose only to nine milliseconds, but the p ninety-five nearly tripled, to thirty milliseconds. That is queueing, and an average from one user would hide it.

Finally, the batch path. A short script loads the same champion model, scores a whole file, and writes a probability column. It prints scored five hundred rows. Because both paths use the same model version, online and batch predictions agree.

The common mistake is to report only the average latency from a single user. Always test at more than one load level, report the median and p ninety-five, and test the way you will deploy. Your numbers will differ with hardware, model and container settings.

## Recap
Let's recap. First, online serving answers each request at once, while batch serving scores many rows on a schedule, and is simpler and cheaper when a delay is acceptable. Second, measure median latency, p ninety-five latency and throughput at more than one load level. Third, use the same registered model version for both paths.

## CTA
In the exercise below this video, you will load-test your own container at two load levels, record the median and p ninety-five, and write a batch scoring script for the same model. It takes about forty minutes.

In the next lesson, we decide where models run and how new versions reach users safely, in Deployment Targets and Release Strategies. See you there.

## Thumbnail
Headline: Now or Tomorrow Morning?
Image: Navy background, a stopwatch on the left and a moon over a stack of rows on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] Locust is not in the brief's tool list; it is used as a free load-testing tool. Its web interface (port 8089, Statistics tab) and HttpUser API were checked against Locust 2.46.6 only. Check the current interface before recording.
- Load-test results (5 users: 16 requests per second, median 6 ms, p95 11 ms; 50 users: 145 requests per second, median 9 ms, p95 30 ms) and 'scored 500 rows' are real outputs from one laptop test with a local Uvicorn process (not the container), one worker and the synthetic model. The voiceover says 'on our machine'. If the recording gives different numbers, show the recorded numbers and update the voiceover to match.
- Katarzyna Nowak and the Kraków online shop are hypothetical.
