# L05 Model Registry and Data Versioning | Presenter Script

Course: AI-18 · Video: 5 min · Words: 672

## Hook
A customer complains about a prediction made three weeks ago. Which model version made it? What data trained that model, and which commit of your code? If you cannot answer in two minutes, you cannot debug, audit or roll back.

## Explain
In the last lesson, experiment tracking recorded every run. A model registry is different. It records only the models you decided to keep, and gives each one a clear name, a version number and a status.

In MLflow, a registered model has a name, such as wine quality classifier. Each time you register a model under that name, MLflow creates a new version: one, two, three, and so on. A version never changes after it is created.

To mark which version is in use, current MLflow releases use aliases. An alias is a movable name that points to one version. For example, champion for the production model, and challenger for a candidate. The serving code always loads the champion. To promote or roll back, you simply move the alias. No code changes.

Older releases used fixed stages instead, such as staging and production. This course uses aliases. If your team's server is older, check which method it supports.

A version is only reproducible if you also know its inputs. So record two tags on every version. First, a data hash. This is a short fingerprint of the exact training data. If one value changes, the hash changes. Second, the Git commit ID, which points to the exact code that trained the model.

Think of a library catalogue. Each edition of a book has a fixed number, and the catalogue records the publisher and the printing. A recommended edition label can move from one edition to another, without anyone reprinting the books.

## Demonstrate
Let's watch Yusuf Demir, an ML engineer at a hypothetical logistics company in Izmir, Türkiye. First, he commits the current code, so the commit ID means something. Then he runs a registration script. It finds the best run by F1, registers its model, adds the two tags, and sets the champion alias.

In the MLflow interface, he clicks Models, and there is the wine quality classifier with version one. He opens it. The champion alias is there, with the data hash and the Git commit as tags.

Next, he changes C in the configuration file, trains, and registers again. Version two appears. But the champion alias still points to version one, because nothing moves until he decides.

Now he promotes it, with one line of Python that moves the alias to version two. He refreshes the page, and champion now points to version two. Then he moves it back to version one. That is a rollback, and it took one line.

One more detail. When Yusuf registered twice on the same data and the same commit, both versions had the same data hash, starting with b f c two five zero. This proves the tags describe the inputs, not the time of the run.

A common mistake is to use the registry like a folder, with names like final, final two or new best. The version number already identifies the model. Use aliases for status and tags for origin. And never put credentials or personal data in tags or descriptions.

## Recap
Let's recap. First, a model registry stores chosen models as numbered versions that never change. Second, aliases such as champion mark which version is in use, and moving an alias promotes or rolls back without code changes. Third, tag every version with a data hash and a Git commit, so it can be rebuilt and explained.

## CTA
In the exercise below this video, you will register your best model, add a second version, choose the champion, and tag each version with its data hash and commit. Then you load the champion and make one prediction. It takes about thirty-five minutes, and your capstone needs exactly this.

That completes week one. In the next lesson, we serve the champion to the world, in Designing a Prediction API with FastAPI. See you there.

## Thumbnail
Headline: Roll Back in One Line
Image: Navy background, three numbered model version cards with a teal 'champion' label moving between cards 1 and 2, headline in teal Inter Bold.

## Production Notes
- [VERSION] MLflow stages versus aliases: confirm that the current release still marks stages as deprecated and recommends aliases, and check the interface labels (Models page, alias and tag display). Tested with MLflow 3.16.1.
- [VERSION] The printed registration message ("Created version '1' of model 'wine-quality-clf'") may differ between MLflow releases; show whatever the current release prints.
- The data hash bfc250d53981 is a real output from the synthetic fallback data; the voiceover reads only its first six characters, the screen shows it in full.
- Screen recording: the Git commit ID shown on screen comes from a demo repository; no tokens, remote URLs with credentials or personal data in tags.
- Yusuf Demir and the Izmir logistics company are hypothetical.
