# Visual rules: the surface, with the numbers

## Why the surface matters this much

People form an impression in 50 ms and decide trust in under 3 s, almost entirely on visual
design, and a bad first screen loses 20 to 30% of new users before they see a feature. People
with no design training feel the problems subconsciously: clutter, weak hierarchy, uneven
spacing, cheap imagery, copy that does not say what they get. Five things fix most of it: clean
hierarchy, generous spacing, professional imagery that supports the headline, balanced
typography, outcome-focused copy. [v1f9iYZ2GhQ, AnL49w4yIOw]

Interface design is not decoration. Colour, contrast and hierarchy either guide people to the
goal or distract them from it. Every visual choice answers one question: does this help the
user see what they need to see when they need to see it? [AnL49w4yIOw]

## Typography

- One font. Two at most, a display face for headings and one for body. [PGQnGEH7c-E, wgMgje60Ovw]
- Count every family that renders as text, including a system stack used for body copy. A
  handwriting or decorative face used only inside an image-like asset (a mock handwritten page,
  a sticker) is a third family: allowed when the asset needs it, but say so, and never let it leak
  into UI text.
- Four sizes, two weights. Six sizes and four weights cannot make a clean UI. Whatever you have,
  cut it by two. [86PGRyQjdzQ]
- Borrow a scale: inspect a well-designed site's computed styles (family, size, weight,
  letter-spacing, line-height) and use them as your text styles. Name styles by role (heading,
  body-lg), not by value. [PGQnGEH7c-E, wgMgje60Ovw]
- Text measure no wider than 600 px; reading suffers past that. [PGQnGEH7c-E]
- Display type: line-height about 110% (down to 95% when lines stack), letter-spacing about
  -0.03 em. [wgMgje60Ovw]
- Text at 18 px and below keeps its size on every breakpoint, so small stays smaller than
  medium without becoming unreadable. [wgMgje60Ovw]
- Monospace for large numbers whose width changes, and reuse an existing heading size for
  decimals so the number never collides with its neighbours. [86PGRyQjdzQ]

## Copy on the surface

- Say more with less. Do not repeat a word the heading already says ("Rewards" above means the
  button does not need "rewards" in it). Fewer words lower cognitive load without losing
  clarity, and across a whole app the difference is large. [86PGRyQjdzQ]
- Clear beats clever. If the button says "earn tokens" and the action claims voting rewards, the
  copy failed. [86PGRyQjdzQ]
- Sell the outcome, not the spec: "1,000 songs in your pocket", not 1 GB. "Close tickets three
  times faster without switching tabs", not "real-time notifications with Slack and Jira
  integrations". [TIfiy1fodDs]
- Nobody reads; they scan for a reason to care or a reason to leave. For every section ask:
  will a fast scroller catch what it is, why it helps, and what to do next? If not, the fix is
  usually structure, not more words. Not too little copy (objections unanswered), not too much
  (analysis paralysis): the amount your buyer needs and nothing else. [TIfiy1fodDs]

## Spacing and structure

- The 8-point grid (he personally works on 4): every number divisible by 8 or 4. 24, not 25;
  12, not 11. Developers then know a 31 is a mistake for 32. [86PGRyQjdzQ, GDjxXRLHEg4]
- Space by relationship. Elements that belong together sit at the base gap; the next group sits
  at a multiple, usually 2x. Heading to body 24, body to buttons 48. Smaller text, smaller base
  (16 inside, 32 to the next). [PGQnGEH7c-E]
- 80 to 96 px between a text block and its image. At least 160 px vertical padding on a section.
  32 px padding inside cards and small wrappers; bigger text needs bigger spacing. "More
  breathing room is the safest route." [PGQnGEH7c-E]
- Padding scales with the device: desktop 56 to 64, tablet 32 to 40, mobile 12 to 24. Buttons
  and radii shrink too (height 88 to 72 to 64, radius 20 to 16 to 12). [wgMgje60Ovw, PYskozIWh-E]
- A content container of 960 to 1200 px max width; 12 columns on desktop, 8 on tablet, 4 on
  mobile; divide content into equal chunks so 2x2s and 3x3s line up anywhere on the page.
  [PGQnGEH7c-E, GDjxXRLHEg4]
- Group related things and space deliberately between elements, inside elements, everywhere.
  Random spacing is the clearest beginner tell. [86PGRyQjdzQ]
- The hero is one screen tall: min-height 100vh with content fit, so nothing clips on a short,
  wide screen and the next section does not peek on a tall one. [wgMgje60Ovw, m2NXQjKPUrg]

## Break the grid on purpose

Humans like patterns and like it when a pattern breaks. Once the grid exists, break it in a few
chosen places: a logo ticker that runs off both edges, a carousel that starts in the grid and
bleeds right, a final call to action with centred text in open space after left-aligned
sections. The page should flow like a wave: predictable, then a surprise, then predictable.
[PGQnGEH7c-E]

## Colour

- 60 / 30 / 10: 60% a neutral (white or light grey, or the dark base), 30% a complementary
  (black or white), 10% the brand colour. A UI that is 60% brand colour is "straight up
  stressful"; everything screams, so nothing gets attention. [86PGRyQjdzQ]
- Or three colours: a base for backgrounds, a primary for calls to action and tiny details, a
  neutral for text. The only hard rule is contrast between base and primary. [PGQnGEH7c-E]
- Shades and tints of one colour, not many colours. A scale like 100 / 75 / 50 / 25 / 10 / 5 / 3%
  of the dark colour gives the UI layers. Name tokens by role and tint (dark-75), never "black",
  so the colour can change later. [wgMgje60Ovw, 86PGRyQjdzQ]
- Text hierarchy by opacity: around 80% for the largest, 60 to 70% for small; keep every size
  readable. Headings at dark-100, body at 75, the smallest at 50. [PGQnGEH7c-E, wgMgje60Ovw]
- The primary at 5% opacity for secondary buttons and cards you want to lift without stealing
  the show. [PGQnGEH7c-E]
- Save the brand colour for what must pop and the things you want to carry meaning (the live
  indicator, the reward icon). Do not put red on a button when red means error elsewhere.
  Juniors go too far the other way and barely use it, which reads as dull; it is a balance.
  [86PGRyQjdzQ]
- Strong, high contrast on elements that drive revenue; reduce contrast on everything else to
  make room for them. [AnL49w4yIOw]
- Flat colours over gradients. A subtle glow (a blurred shape at low opacity behind an image)
  rather than a heavy one. [86PGRyQjdzQ, PGQnGEH7c-E]

## Visuals and assets

- The easiest way to make a hero look amazing is a great visual. With stock video, community
  illustrations, 3D libraries and image models there is no excuse for a bad asset. Pick the
  niche, the style, the colours, and generate on a white background so the asset blends in.
  [PGQnGEH7c-E, m2NXQjKPUrg]
- Colour-match assets and palette: eyedrop the primary from the hero image, or make the image
  fit the system's colours. [cocnZubvfFE]
- A blurred copy of the image behind the content gives an aurora backdrop that ties colours
  together; blur costs rendering performance, so use it sparingly. [cocnZubvfFE, V-xm5c_XRWU]
- Simple visuals that communicate beat fancy ones that confuse. A grey bar chart with one red
  dot tells the user where to look; 45 layers of shadow tells them the designer was busy.
  [86PGRyQjdzQ]

## Details, the last 19%

Details are where websites become a mess, because people add everything to give a design life.
The rule is simple and minimal, with a few consistent treatments:

- Buttons: a 1 px white inner shadow at the top edge plus a soft, faded drop shadow, so the
  button is not flat and lifeless. Secondary buttons: a primary-colour border at 5% opacity and
  the same shadow. Copy the exact style onto cards. [PGQnGEH7c-E]
- Consistent radii (Apple's squircles are the reference), consistent spacing, consistent
  proportions. Misaligned radii, too many shades of one colour and unintentional emphasis
  compound and break the world-class feel, and they make the developer's life miserable.
  "Consistency creates trust." [doiaMtD80p8, wmTkiF23GRQ]
- Add emphasis only where it matters, and reuse one visual motif to connect related parts of
  the UI (the same pulsing dot marks the live period in the chart and the live action in the
  panel). Achieve more with less. [86PGRyQjdzQ]
- Avoid the AI tells: Inter for everything, purple-to-blue gradients, glossy abstract art.
  [pqWPKgfBDiw] The full list is below.
- QA every screen against a checklist before moving on: alignment, radii, shades, emphasis,
  microcopy, opacities. The comments pile up and that is the point. [wmTkiF23GRQ]

## Landing page anatomy

- One call to action. In a study of 18,000 pages, one CTA converted at 13.5%, two at 11.9%,
  three at 10.5%. Fewer options, more decisions (the 24-versus-6 jam study: 3% vs 30% bought).
  [TIfiy1fodDs]
- The exception: visitors arrive at different readiness, so a primary CTA for high intent
  ("Try free") and a softer secondary for context ("Watch the demo") is fine on complex
  products. Add escape valves (chat widget, support link, save for later) for people not ready
  to convert at all. [TIfiy1fodDs]
- Each section: a headline naming a pain or outcome; a subhead adding a new angle; a product
  visual with context or contrast; proof points (logos, numbers, testimonials); a clear CTA.
  [TIfiy1fodDs]
- A proof point is only proof if it survives a check. A sample question must be the real
  question with its real paper, year and marks; a number must be the product's own; a named
  person must exist and have agreed. When none is available, show the product doing the work
  (a real marked page) and leave the number out; an invented or wrong proof point tells the
  sceptical visitor exactly what they feared.
- Show the product doing the thing: Sketch's hero is a live prototype you can move; Jitter's
  value proposition ("motion design made simple") is followed by UI flying into the frame.
  Explain in text and show in motion. [evhZQg2NHfo]
- Hero recipe when you have one great image: mega heading (centred, or left with the asset
  right), the same base spacing from heading to body to CTA, a radial darkening behind text for
  contrast, the CTA coloured from the image. Vary alignment and size per section (centre mega,
  left large, right large, 4-up grid) and the same four tricks produce every section. [cocnZubvfFE]
- Check mobile on the published site, not the canvas. Heavy effects that look great on a new
  phone may crawl on an old one; the best sites scale type and crop GIFs for mobile instead of
  shrinking them. [evhZQg2NHfo, wgMgje60Ovw]

## Design systems

- Design freely first. When an element repeats (a heading size, an icon size, a button), make it
  a style or component. Atomic design: atoms (icon, text style, colour), molecules (icon with
  label), organisms (a card), templates (a card list section). [_uva2dQPlV8]
- Primitives (raw colours, sizes) and then semantic tokens that alias them (background, body
  primary). Keep themes, sizes and languages in separate collections so they switch
  independently; link every colour before swapping themes. [XnI-WbMCDyw]
- Be context-aware. A solo designer's or small team's system exists to save time and stay
  consistent, not to match Ant Design. "Don't build an Excel sheet of buttons until you need it."
  [_uva2dQPlV8]
- Style guide before pages: colour styles, text styles, link states, components with variants
  per device, an image library. One change then propagates everywhere. [PYskozIWh-E, wgMgje60Ovw]
- Make the nav, buttons and repeated items components with per-device variants; set a max width;
  pin elements to edges so they scale; check scaling up as well as down. [wgMgje60Ovw, rEjd7QRxtDY]

## The tells, with their fixes

A generated screen fails in the same few ways. Each line pairs the tell with what replaces it;
the list says what to avoid, and the direction decides the replacement, so it never becomes a
house style of its own. (Format after Damir Sokolovsky's unslop, CC BY 4.0; the items here are
from Tim Gabe's videos and this skill's own runs.)

- Purple-to-blue or violet-to-pink gradients on backgrounds, cards or buttons → one neutral
  surface, the brand colour only where it means something
- Gradient-filled text in headings or numbers → solid text colour
- Coloured glows, glass cards with coloured shadows, blurred colour blobs behind content → remove;
  depth from a soft neutral shadow or a hairline, not from light effects
- Everything highlighted, five accents on one screen → one accent, used once or twice
- Inter (or any default nobody chose) for everything → a type choice that fits the character
- Six sizes and four weights → four sizes, two weights; hierarchy from size and colour, not weight
- Uppercase labels with wide tracking (`PAID THIS MONTH`) → sentence case
- Negative letter-spacing on small text → zero or slightly open; tight tracking only on display type
- Emoji as icons, in labels or in pills; the ✨ for anything AI → one line icon set, or nothing
- Spacing values off the grid (11, 13, 31) → the nearest step of 4 or 8
- Rows of one list at different heights or gaps → one height, one gap
- Five equal metric cards in a row → one number that leads, the rest smaller or different in kind
- A chart because dashboards have charts; rainbow bars in one series → one chart that answers a
  question, one accent for the thing that matters
- Greeting headlines (`Welcome back, Priya! 👋`) → the answer or the context (the period, the
  page, the one sentence that says how things stand)
- Exclamation marks, hype words (supercharge, seamless, unlock, magical, revolutionize),
  "AI-powered" on everything → plain outcome copy
- Claims that cannot be checked (`Loved by 10,000+ teams`, a wrong question number) → the
  product's own verified fact, or nothing
- Three calls to action in a hero → one, and at most one softer secondary
- Buttons and links that go nowhere (`href="#"`) → a real destination, or remove the control
- Only the happy path designed → empty, loading, error, offline and limit-reached states written
- Motion that loops for no reason (pulse, ping, shimmer, floating, parallax on everything),
  `transition-all`, cards that scale on hover → motion that explains something, one easing

## App-layout tokens, as starting values

When a project has no system, these are sane defaults for dashboards and app screens (from
Tim Gabe's grid rules plus common practice; the direction can move them):

- Spacing scale 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128. Inside a control 4 to 12,
  between related rows 2 to 8, between groups 12 to 24, between sections 32 to 64 (landing
  pages 80 to 160).
- Sidebar 240 to 280 wide; content fluid, page padding 24 to 32, capped around 1440 to 1600.
  Top bar 56 to 64. Navigation rows 32 to 36 tall with 2 to 4 between them; a section label sits
  closer to its own items than to the section above (24 above, 8 below).
- Radii nest: inner radius = outer radius minus the padding between them, never below 4.
  Controls 8 to 10, cards 12 to 16, panels 14 to 20. Not everything is a pill.
- Hairlines are the text colour at 6 to 10% opacity. On dark themes depth comes from surface
  steps, not shadows.
- Numbers in tabular figures and one format across the screen (`$48,210` next to `$124,860.40`
  is two formats).
