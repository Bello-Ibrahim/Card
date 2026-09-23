# CertifAI production decisions

These decisions were made on 2026-09-23 on the course owner's instruction ("pick the best and most recommended"). Stage 3 scripts and demos use the tools named here.

The lessons still tell learners they can use "a free … tool of your choice", so the courses keep working if a tool changes. The screen demos, however, show the tool chosen here.

Every item is [VERSION]: before recording, check the free plan, the interface and the licence terms against the live tool.

## Generic tools named in the briefs

| Need | Courses | Demo tool | Backup | Why |
|---|---|---|---|---|
| Free image generator | AI-02, AI-07, AI-20, AI-21, AI-23 | **Google Gemini** (image generation in the Gemini app, or Google AI Studio) | **Adobe Firefly** (free tier) | Gemini is already the main tool in AI-20 and AI-02, and it works with a free Google account. Firefly is the backup because Adobe markets it for commercial use [VERIFY terms]. |
| Text-to-speech | AI-22 | **ElevenLabs** (free plan) | **Piper** (open source, runs offline) | ElevenLabs is the best-known tool and has clear voice, speed and pronunciation controls, which suits a screen demo. Its free plan may not allow commercial use or may require attribution [VERIFY]. Piper has no licence cost. |
| Whisper transcription app | AI-22 (also useful in AI-21) | **Buzz** (free, open-source desktop app for Whisper) | Whisper command line (optional, as in L04) | Buzz runs Whisper locally without code on Windows, macOS and Linux, and exports SRT. This fits beginners and keeps audio private. |
| AI music | AI-22 | **Suno** (free plan) | **Udio** (free plan) | Suno is the most widely used and is simple to demonstrate with mood, genre and instrument prompts. Free-plan songs may be for non-commercial use only [VERIFY]. The lesson already teaches how to check licences. |
| Chatbot builder | AI-26 | **Botpress** (free plan) | **Tidio** (free plan) | Botpress has a visual flow builder, knowledge-base answers and built-in hand-off to a human, which is the centre of the AI-26 capstone. Tidio is simpler and has live chat. |
| No-code app builder | AI-28 | **Glide** (free plan) | **Lovable** (AI app builder, free credits) | Glide builds working apps from a spreadsheet with no code and has built-in AI features. It is stable and suits a first MVP [VERIFY that the free plan includes AI]. Lovable builds an app from a prompt, which shows an "AI-native" path. |
| Three-tool comparison demo | AI-02 L11 (also AI-03 L12) | **Claude, ChatGPT and Google Gemini** (free tiers) | Google AI Studio instead of the Gemini app | These are the three tools named across the briefs; they are widely available and each has a free tier [VERSION]. |
| AI readiness templates | AI-04 | **CertifAI's own templates** (already written into L04, L05, L08 and L10) | none | CertifAI owns the content outright, with no third-party licence. |
| Bias audit case studies | AI-29 | **CertifAI's own hypothetical case** (already in L08) | none | No unchecked claims about real companies. |

## Other open items

| Item | Decision |
|---|---|
| AI-13: 4 broken training notebooks and 4 learning-curve images | Produced from the lesson code and saved in `courses/ai-13-…/assets/`. |
| AI-25: synthetic patient dataset, sample source text, synthetic discharge note | Produced as synthetic files and saved in `courses/ai-25-…/assets/`, each labelled "synthetic, for teaching". |
| AI-22: practice audio clips (L01) and noisy practice recording (L06) | **Human production needed.** Clips with real voices need rights-cleared recordings. The team records them with Audacity using consenting staff, following the script in each lesson. |
| Native-speaker checks (isiZulu/Yoruba in AI-23; Arabic in AI-13, AI-24, AI-26) | These stay as human review items. A machine check does not replace a native speaker. The flags remain in STAGE2_REVIEW.md. |
| Legal (AI-30) and clinical (AI-25) sign-off | These stay as release blockers. Scripting can go ahead, but release cannot. |
| HeyGen avatar and voice IDs | **Still needed from the owner** before Stage 4. Recommendation: one HeyGen standard (non-premium) avatar for the whole catalogue, in a professional style with a neutral, easy-to-follow English voice. Standard avatars use no credits on paid plans [VERIFY]. |
| AI-13 L18: three example datasets for learners | Reuse the three datasets the course already teaches with: **Fashion-MNIST** (images), **beans** (plant images) and **AG News** (text). Learners already know them, and one licence check covers both the lessons and L18 [VERIFY licences before recording]. |
| Arabic caption font | Noto Sans Arabic (SIL Open Font License), as set in the system prompt. |
