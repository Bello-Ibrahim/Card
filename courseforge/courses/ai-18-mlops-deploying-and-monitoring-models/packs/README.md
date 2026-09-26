# Stage 4 packs: AI-18 MLOps: Deploying and Monitoring Models

| Pack | What a person does |
|---|---|
| `heygen_M*.md` | Render one presenter video per lesson in HeyGen with the settings shown |
| `broll_*.md` | Generate the hero clips in Google Flow or Kling, at most 8 a day |
| `screen_L*.md` | Record the screen demos in OBS |
| `stock_queries.csv` | Run the stock_search step (Pexels/Pixabay API), or download manually |

Slides, text cards and thumbnails are already rendered in `lessons/*/assets/slides/`. Slides marked `needs_design` in `assets.json` are working placeholders: a designer can replace one by adding `sNN.html` next to it and re-running `render_slides.py`.

## Files expected in /incoming/ (85 plus 33 stock clips)

- [ ] `ai-18-mlops-deploying-and-monitoring-models_M1_L01_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M1_L02_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M1_L03_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L03_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L03_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L03_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L03_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L03_screen_5.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L03_screen_6.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M1_L04_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L04_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L04_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L04_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L04_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M1_L05_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L05_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L05_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L05_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L05_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M2_L06_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L06_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L06_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L06_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L06_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M2_L07_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L07_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L07_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L07_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L07_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M2_L08_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L08_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L08_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L08_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L08_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M2_L09_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L09_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L09_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L09_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L09_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M2_L10_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M3_L11_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L11_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L11_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L11_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L11_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L11_screen_5.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M3_L12_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L12_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L12_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L12_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L12_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L12_screen_5.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M3_L13_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L13_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L13_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L13_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L13_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L13_screen_5.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M3_L14_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L14_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L14_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L14_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L14_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L14_screen_5.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L14_screen_6.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M4_L15_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L15_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L15_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L15_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L15_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M4_L16_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L16_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L16_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L16_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L16_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M4_L17_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L17_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L17_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L17_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L17_screen_4.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_M4_L18_presenter.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L18_screen_1.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L18_screen_2.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L18_screen_3.mp4`
- [ ] `ai-18-mlops-deploying-and-monitoring-models_L18_screen_4.mp4`
