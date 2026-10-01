---
name: flyer-design
description: Use for any Cook & Bake Academy flyer, poster, print handout, social graphic, or story image. Apply the project brand-voice skill, verify every factual claim against courses.json or the approved catalogue, generate the requested artwork with imagegen, and hand back the image, its prompt, and a complete text proof.
---

# Cook & Bake flyer design

## Sources and preparation

1. Read `../brand-voice/SKILL.md` and follow its tagline, voice, palette, type, and photo rules.
2. Read the user's creative brief. List every item the finished graphic must carry before making it.
3. Verify all factual text, including course names, fees, dates, weeks, campuses, offers, and links, against `cnbacademy/data/courses.json` (resolve from the project root). Use this catalogue as the offer-fact source. If a requested fact is absent or the sources conflict, mark it **UNKNOWN** and seek clarification; do not put it in finished artwork.

## Produce the artwork

Use `ChatGPT image generation` to create each requested format. Specify exact dimensions or aspect ratio in the prompt: A5 portrait for print, 1:1 for a square post, and 9:16 for a story. Use real-looking food and hands at work in natural light, ample cream space, high-contrast type, and the brand colours.

For print, keep all essential text and marks at least 10 mm inside the trim edge. Keep text away from busy parts of photographs. Preserve legibility at arm's length for print and thumbnail size for social formats. A QR code may be shown as a clearly labelled placeholder only when the brief asks for one; never imply a placeholder is scannable.

Save each final image in `creative/<campaign>/` with the exact generation prompt in an adjacent text file of the same base name. Keep only the approved facts in the text supplied to the image generator.

## Proof and hand back

1. Read each generated image and transcribe **every visible word and number**, line by line. Include text in badges, footers, and QR labels.
2. Compare each transcription with the must-carry list, brand-voice tagline, and source facts. If text is missing, wrong, or illegible, regenerate with the exact correction named and proof the replacement again.
3. Hand back, for **each format**: the final image file, the adjacent prompt file, the complete visible-text transcription, and a short source check identifying which catalogue field supports each factual claim. Call out any item that still needs human proofreading.

Do not publish or post the graphic unless the user separately asks for that action.
