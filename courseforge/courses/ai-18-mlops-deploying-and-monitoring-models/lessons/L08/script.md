# L08 Containerising the Model Service | Presenter Script

Course: AI-18 · Video: 5 min · Words: 658

## Hook
Your API runs on your laptop. Will it run on the server with the same Python, the same libraries and the same model file? A container says yes. But a careless container can be slow, large, and a security risk.

## Explain
In the last lesson, our API learned to reject bad input and to log every prediction. Now we package it. You already know basic Docker, so we focus on four choices that matter most for a production model service.

First, a small base image. A slim Python image contains much less than the full one, so it downloads faster and has fewer packages that could contain security problems. Second, a multi-stage build. The first stage installs the dependencies. The final stage copies only the results. Build tools and caches stay behind.

Third, a non-root user. By default, processes in a container run as root. If an attacker breaks into the service, a normal user limits what they can do. Fourth, decide where the model comes from.

You can copy the model into the image. Then the image is self-contained, starts fast, and each image tag means exactly one model. Or you can load it from the registry at start-up. One image serves any version, but start-up depends on the registry, and the container needs credentials. In this course we copy the model in, because rollback becomes simple: run the previous image.

One firm rule. Never put secrets in a Dockerfile or an image. Anyone who can pull the image can read its layers. Pass secrets when the container runs, and keep that file out of Git.

A container is like a shipping container for goods. Everything the product needs travels inside, so it arrives the same at every port. And a multi-stage build packs the product, but leaves the factory tools at home.

## Demonstrate
Let's watch Lars Eriksson, a platform engineer at a hypothetical energy company in Gothenburg, Sweden. First, he exports the champion model from the registry to a local model folder. Then he creates a docker ignore file that keeps out the virtual environment, the database, the data, the logs, the Git folder and any environment file.

Now the Dockerfile, in two stages. The build stage turns the requirements into ready packages. The runtime stage installs them, creates a normal user, copies only the app and the model folder, and switches to that user before starting the server.

He builds the image with a version tag, and runs it. In the browser, the health page answers from inside the container.

Next, he lists the image size, and compares it with a single-stage build on the full Python image. The slim, multi-stage image is clearly smaller. Record your own sizes, because they depend on your requirements and platform. Last, he checks the user. The container prints app user, not root.

A common mistake is to copy the whole project folder into the image. That silently adds the virtual environment, the database, log files, and sometimes a file with passwords. The image grows, and secrets leak to anyone who pulls it. Copy only what the service needs, and keep the ignore file as a second safety net.

## Recap
Let's recap. First, use a slim base image, a multi-stage build and a non-root user for model services. Second, copying the model into the image makes each tag mean one model and makes rollback simple, while loading from the registry is more flexible but adds a start-up dependency. Third, never put secrets in an image.

## CTA
In the exercise below this video, you will write a Dockerfile for your service, build it, and shrink the image with at least one technique. Record the size before and after. It takes about forty minutes, and your capstone will publish exactly this image.

In the next lesson, we measure how fast this container really is, in Batch versus Online Serving and Performance. See you there.

## Thumbnail
Headline: Small, Safe Model Containers
Image: Navy background, a large bulky shipping container next to a small neat teal one with a padlock, headline in teal Inter Bold.

## Production Notes
- [VERSION] Docker base image names and tags (python:3.11-slim, python:3.11) and multi-stage build features: check current tags and supported Python versions before recording. The Dockerfile was not built in the Stage 2 review environment, so build and record it before the shoot.
- No image sizes are given in content.md. The voiceover does not state sizes; the screen shows whatever the recording machine reports. Do not add numbers to the voiceover unless they come from the actual recording.
- [VERSION] Docker Desktop licence terms for organisations change; the voiceover does not discuss licensing.
- Screen recording: never show a real .env file or any secret value. If --env-file is shown, use an empty demo file with a placeholder name only.
- Lars Eriksson and the Gothenburg energy company are hypothetical. Docker basics are a prerequisite, so the lesson recaps them in one sentence (curriculum judgement call).
