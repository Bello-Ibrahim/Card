# Screen Demo Pack: AI-18 L05 Model Registry and Data Versioning

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L05_screen_1.mp4`
- **Target length:** about 22 seconds

**Steps**

1. In the terminal, run: git add . and git commit -m "Add registration script"
2. Show register.py in the editor, highlighting search_runs ordered by metrics.f1, register_model, the two set_model_version_tag calls and set_registered_model_alias
3. Run: python register.py
4. Show the printed message that version 1 of wine-quality-clf was created

**Narration over this clip (for pacing)**

> Let's watch Yusuf Demir, an ML engineer at a hypothetical logistics company in Izmir, Türkiye. First, he commits the current code, so the commit ID means something. Then he runs a registration script. It finds the best run by F1, registers its model, adds the two tags, and sets the champion alias.

## Clip 2: scene 9

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L05_screen_2.mp4`
- **Target length:** about 15 seconds

**Steps**

1. Open the MLflow interface in the browser
2. Click Models
3. Click wine-quality-clf and open Version 1
4. Point to the champion alias
5. Point to the tags data_sha256 = bfc250d53981 and git_commit

**Narration over this clip (for pacing)**

> In the MLflow interface, he clicks Models, and there is the wine quality classifier with version one. He opens it. The champion alias is there, with the data hash and the Git commit as tags.

## Clip 3: scene 10

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L05_screen_3.mp4`
- **Target length:** about 13 seconds

**Steps**

1. Edit config.yaml and change model C
2. Run the training and tracking script, then run: python register.py again
3. Refresh the Models page: Version 2 appears
4. Show that the champion alias is still on Version 1

**Narration over this clip (for pacing)**

> Next, he changes C in the configuration file, trains, and registers again. Version two appears. But the champion alias still points to version one, because nothing moves until he decides.

## Clip 4: scene 11

- **Filename:** `ai-18-mlops-deploying-and-monitoring-models_L05_screen_4.mp4`
- **Target length:** about 19 seconds

**Steps**

1. In a Python shell, run: client.set_registered_model_alias(NAME, "champion", 2)
2. Refresh the registry page: champion now on Version 2
3. Run: client.set_registered_model_alias(NAME, "champion", 1)
4. Refresh: champion back on Version 1

**Narration over this clip (for pacing)**

> Now he promotes it, with one line of Python that moves the alias to version two. He refreshes the page, and champion now points to version two. Then he moves it back to version one. That is a rollback, and it took one line.

## Production notes for this lesson

- [VERSION] MLflow stages versus aliases: confirm that the current release still marks stages as deprecated and recommends aliases, and check the interface labels (Models page, alias and tag display). Tested with MLflow 3.16.1.
- [VERSION] The printed registration message ("Created version '1' of model 'wine-quality-clf'") may differ between MLflow releases; show whatever the current release prints.
- The data hash bfc250d53981 is a real output from the synthetic fallback data; the voiceover reads only its first six characters, the screen shows it in full.
- Screen recording: the Git commit ID shown on screen comes from a demo repository; no tokens, remote URLs with credentials or personal data in tags.
- Yusuf Demir and the Izmir logistics company are hypothetical.
