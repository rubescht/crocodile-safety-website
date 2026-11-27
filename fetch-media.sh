#!/usr/bin/env bash
# Render build step: pulls the hero video and photo into the published site.
# Replace with committed files in dist/assets/media/ once you have final footage.
set -euo pipefail
mkdir -p dist/assets/media
[ -s dist/assets/media/hero.mp4 ] || curl -fsSL -o dist/assets/media/hero.mp4 "https://cdn.creativeclaw.co/u/48eaa2c1/videos/68b182a8-f0cd-4dfe-a70f-ccfaeaf1f7bc.mp4"
[ -s dist/assets/media/hero.jpg ] || curl -fsSL -o dist/assets/media/hero.jpg "https://cdn.creativeclaw.co/u/48eaa2c1/images/de1fdcf4-3008-4f37-bacc-2dfa10351fca.jpg"
[ -s dist/assets/media/six-lines.mp4 ] || curl -fsSL -o dist/assets/media/six-lines.mp4 "https://cdn.creativeclaw.co/u/48eaa2c1/videos/dcfcf79a-9bcc-4081-bb32-dcbc097996fb.mp4"
[ -s dist/assets/media/six-lines-poster.jpg ] || curl -fsSL -o dist/assets/media/six-lines-poster.jpg "https://cdn.creativeclaw.co/u/48eaa2c1/images/1b5c4ecd-2fe9-4cd0-a8c1-f043cc7cd9b5.jpg"
[ -s dist/assets/media/night-hero.mp4 ] || curl -fsSL -o dist/assets/media/night-hero.mp4 "https://cdn.creativeclaw.co/u/48eaa2c1/videos/b754639c-152d-497a-b161-a4ed99ddee5b.mp4"
[ -s dist/assets/media/night-hero.jpg ] || curl -fsSL -o dist/assets/media/night-hero.jpg "https://cdn.creativeclaw.co/u/48eaa2c1/images/cfc7f60f-f6bb-40ba-a57e-6f8d27d4d388.jpg"
ls -la dist/assets/media
