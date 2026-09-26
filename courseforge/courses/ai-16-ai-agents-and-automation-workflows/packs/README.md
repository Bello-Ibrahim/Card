# Stage 4 packs: AI-16 AI Agents and Automation Workflows

| Pack | What a person does |
|---|---|
| `heygen_M*.md` | Render one presenter video per lesson in HeyGen with the settings shown |
| `broll_*.md` | Generate the hero clips in Google Flow or Kling, at most 8 a day |
| `screen_L*.md` | Record the screen demos in OBS |
| `stock_queries.csv` | Run the stock_search step (Pexels/Pixabay API), or download manually |

Slides, text cards and thumbnails are already rendered in `lessons/*/assets/slides/`. Slides marked `needs_design` in `assets.json` are working placeholders: a designer can replace one by adding `sNN.html` next to it and re-running `render_slides.py`.

## Files expected in /incoming/ (77 plus 22 stock clips)

- [ ] `ai-16-ai-agents-and-automation-workflows_M1_L01_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M1_L02_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M1_L03_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L03_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L03_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L03_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L03_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L03_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L03_screen_6.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M1_L04_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L04_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L04_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L04_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L04_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L04_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M2_L05_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L05_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L05_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L05_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L05_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L05_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M2_L06_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L06_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L06_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L06_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L06_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L06_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M2_L07_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L07_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L07_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L07_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L07_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L07_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M2_L08_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L08_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L08_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L08_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M3_L09_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M3_L10_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L10_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L10_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L10_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L10_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L10_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M3_L11_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L11_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L11_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L11_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L11_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L11_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M3_L12_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L12_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L12_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L12_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L12_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M4_L13_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L13_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L13_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L13_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L13_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M4_L14_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L14_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L14_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L14_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L14_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L14_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M4_L15_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L15_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L15_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L15_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L15_screen_4.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L15_screen_5.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_M4_L16_presenter.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L16_screen_1.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L16_screen_2.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L16_screen_3.mp4`
- [ ] `ai-16-ai-agents-and-automation-workflows_L16_screen_4.mp4`
