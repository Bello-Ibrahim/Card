# L11 Testing ML Code and Models | Presenter Script

Course: AI-18 · Video: 5 min · Words: 693

## Hook
All your tests pass. You deploy the new model. A week later, the business says predictions are worse than before. How can every test be green when the model got worse? Because code tests check the code, not the model.

## Explain
Welcome to week three, where we automate. Automation needs tests first. An ML service needs four kinds of test, and each one catches problems the others miss. Unit tests check small pieces of code, for example that the data loader returns the expected columns. They are fast and run on every change.

Data tests check the inputs. No missing values, values in the expected range, and the expected share of each label. They catch broken data before training. API tests send requests to the service and check status codes and response shapes. FastAPI's test client does this without starting a real server.

The model quality gate is the one that catches a worse model. It trains or loads the model, and checks a metric on a fixed test set against a minimum, for example, F1 must be at least zero point five.

Set the minimum from evidence: the current champion's score on the same test set, minus a small margin you agree with the business. A gate that is too low catches nothing. One that is too high blocks every change.

Think of a car inspection. Unit tests check each part. Data tests check the fuel. The quality gate is the road test, and API tests check that the doors and controls work for the driver. A car can pass every parts check and still fail the road test.

## Demonstrate
Fatima Al-Sayed is an ML engineer at a hypothetical e-commerce company in Alexandria, Egypt. She adds tests to our wine API with pytest. All tests live in a tests folder, and a small settings file lets them import the project code.

The first file holds the unit, data and model tests. One checks the columns, one checks that labels are only zero or one, one checks missing values and the alcohol range, and the last trains a model on a fixed split and checks its F1 score.

The second file holds the API tests. It sends one valid wine and one wine with an alcohol value of forty, and expects the service to reject the second one. The test client runs inside a with block, so the start-up code loads the model.

She points the service at the exported model folder and runs pytest. On our machine, the result was six passed, with one deprecation warning from the test client.

Now the important step. She breaks the gate on purpose and raises the minimum to zero point nine. She runs pytest again. The quality gate fails, and the message shows the real score, about zero point five six, below zero point nine. This is exactly how a real, worse model would fail. The code still works, but the metric is below the minimum.

She changes the gate back and runs again, and all tests pass. A test that has never failed has not proved that it can catch anything.

The common mistake is to compute the gate on a new random split each time. The score then moves for reasons unrelated to the model, and the gate fails or passes by chance. Use a fixed test set with a fixed seed, store its data hash, and keep personal data out of it.

## Recap
Let's recap. First, ML services need unit tests, data tests, model quality gates and API tests. Second, only the quality gate, on a fixed test set, can catch a model that is worse while its code still works. Third, make each test fail on purpose once, to prove that it can catch the problem.

## CTA
In the exercise below this video, you will write at least five tests covering all four types, make one fail on purpose, screenshot it, and fix it. Add one line on how you chose your threshold. It takes about forty minutes.

Next, we make sure these tests run on every change, without anyone remembering, in GitHub Actions: CI for an ML Service. See you there.

## Thumbnail
Headline: All Green, Still Worse?
Image: Navy background, a row of green check marks on the left and a falling line chart on the right, headline in teal Inter Bold.

## Production Notes
- [VERSION] FastAPI TestClient depends on an HTTP client library; with Starlette 1.7.0 it printed a deprecation warning about the httpx package. Check the current recommended dependency before recording. Tested with pytest 9.1.1. The voiceover mentions one warning but does not name the package.
- Test outputs ('6 passed' with one deprecation warning, and 'AssertionError: assert 0.5568181818181818 >= 0.9') are real outputs from the synthetic fallback data. The voiceover rounds the score to about zero point five six. If the recording gives different numbers, show the recorded output and update the voiceover to match.
- The test code is shown on screen, not read aloud. Set MODEL_URI=model before running pytest (the folder exported in L08).
- Fatima Al-Sayed and the Alexandria e-commerce company are hypothetical.
