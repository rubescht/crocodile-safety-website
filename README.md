# Crocodile Safety Australia — website

Static HTML site. The published site is in `dist/`.

## Deploy (Render static site)
- Build command: `./fetch-media.sh`
- Publish directory: `dist`

`fetch-media.sh` pulls the hero video and photo into `dist/assets/media/` at deploy time. For permanent hosting, commit final files there as `hero.mp4` and `hero.jpg`.

## Editing
Content lives in `build.py`. Edit it, run `python3 build.py`, commit the updated `dist/`.

## Before go-live
1. Enquiry form: create a Formspree form and replace `YOUR-FORM-ID` (search the HTML). Until then the form opens the visitor's email app addressed to Chris.
2. Fill in the [BRACKETED] placeholders: founder bio, licence/permit numbers, insurance cover, feral species, training length, mobilisation times, Film & TV credits.
3. Replace the AI-generated footage (labelled "Illustrative footage") with real field footage when available.
4. Point crocodilesafety.com.au at the host only once the client has signed off.
