---
name: unvibe
description: Product-design recipe for apps and web apps that have to feel premium and keep users, distilled from Tim Gabe (ex-Spotify designer, agency for YC and app founders) across all 81 of his videos. Two modes. AUDIT: score an existing screen, flow, onboarding, landing page or paywall against the recipe and list the fixes in impact order. BUILD: design a new screen, flow, onboarding, paywall, landing hero or retention feature by the recipe, direction first, every state designed, his exact type/spacing/colour numbers, emotion only at the peak and the end, structure before price. Use it whenever someone wants a product or page to look premium, trustworthy, "not vibe-coded", less generic or less like AI slop; asks why users don't convert, don't come back, or bounce in onboarding; designs or reviews a paywall, pricing screen, trial, onboarding, empty/error/loading state, dashboard, landing hero or retention mechanic (streaks, badges, leaderboards, notifications); or asks what makes apps like Duolingo, Strava, Spotify, Netflix, Airbnb or Apple feel the way they do. Fires even when the word "design" is absent, e.g. "our free users never upgrade", "the home screen feels off", "make this feel like a real company".
---

# Premium product design

The whole recipe in one sentence: decide the one idea and what "premium" means to this buyer
first, make sure the user always knows what happened and what to do next in every state, apply a
small set of exact numbers to the surface, spend emotion only at the peak and the end, and build
the mechanics that bring people back and make them pay. Everything below serves that sentence.

Why this order matters: a clean screen is the floor now. Any model produces one in a minute, so a
clean screen says nothing about care. What buyers read as "premium" is evidence that someone
thought about them: the error they hit, the wait they sat through, the one decision only this
company would have made. Those are the places this skill spends its attention.

The recipe lives in six reference files. Read only the ones the task touches:

| File | Read it when |
|---|---|
| `references/direction.md` | starting anything new, or a screen "feels generic" and nobody can say why |
| `references/ux-foundation.md` | flows, onboarding, states, trust in money/health products, friction |
| `references/visual-rules.md` | type, spacing, grid, colour, assets, buttons, landing-page anatomy, design systems |
| `references/emotion-motion.md` | animation, micro-interactions, celebrations, where to put delight |
| `references/retention.md` | streaks, badges, leaderboards, notifications, habits, identity, "they don't come back" |
| `references/paywalls.md` | pricing screens, trials, upgrades, credits, "they don't convert" |

`references/sources.md` maps every rule to the video it came from, for when a claim needs checking.

Most tasks need two files, not six: `direction.md` plus the one that matches the artefact. A
landing page or hero: `visual-rules.md`. An app screen or dashboard audit: `ux-foundation.md`,
then `visual-rules.md` for the surface findings. Onboarding or a flow: `ux-foundation.md`. A
paywall or pricing screen: `paywalls.md`. A streak, badge, notification or "they don't come
back": `retention.md`. Open `emotion-motion.md` only when the task is about animation, a
celebration moment or how a result is delivered. Reading everything costs minutes and tokens and
does not change the findings.

## Which mode

- The user has something (a file, a screenshot, a URL, a description of a screen or flow) and
  wants to know what is wrong or what to fix: **Audit**.
- The user wants something made (a screen, a flow, a paywall, a hero, a mechanic): **Build**.
- A redesign is both: audit first, then build from the audit's top findings.

Whether to keep the existing look depends on the audit's point-of-view score. At 3 or above the
product has a direction: keep its theme, tokens and components, apply the numbers as a yardstick,
and fix what is wrong. At 1 or 2 the look *is* the problem (it is the average of every app, so
it says nothing about who made it): choose a direction, write the brief, and change the surface
visibly. Polishing a generic screen produces a tidier generic screen, which the owner will
rightly call no change. This skill decides what and why. For pixel-level polish of components
(radii, icon transitions, hit areas) a dedicated UI-polish skill, if one is installed, is the
better tool afterwards.

## Audit mode

Read `references/direction.md` and whichever other files the artefact touches, then look at the
artefact as a new customer would, not as its author.

Get something you can actually look at. Code alone hides what people see: run the app or open
the file and screenshot it. Given only a live URL, save the page and work on the copy. Given
only a screenshot, rebuild it as one static HTML file first and treat that as the original.
Then measure before you judge: `python3 scripts/measure_html.py page.html` counts font sizes,
weights, colours, gradients, dead links, off-grid spacing values, state mentions and more, so
the surface findings are numbers ("13 sizes, 6 weights, 27 dead links") instead of adjectives.
Run it on the before and the after and the table is your evidence.

Work through the five layers in order,
because a finding in an earlier layer usually explains several in later ones (no point of view
produces random colour use; an undesigned state produces a dead end).

1. **Direction.** Can you say in one sentence what this product believes and who it is for?
   Does every element on the screen serve that? What would a competitor's version look like,
   and is this one distinguishable?
2. **Foundation.** Walk the flow the screen belongs to. At each step: does the user know what
   just happened, can they undo it, do they know what to do next? List the states the screen can
   be in (empty, loading, partial, error, offline, limit reached, success) and mark which are
   designed. Count the decision points before value. Follow every button and link: an action
   that leads nowhere (a hash anchor, a loop back to the top, a disabled control) is a dead end
   the user meets at the exact moment they decided to act.
3. **Surface.** Count fonts, sizes, weights. Measure spacing against the grid and the 2x
   relationship rule. Count colours and check where the brand colour is spent. Find the primary
   action and ask whether it is the only thing that pops. Read the copy as a scanner: what is
   it, why does it help, what do I do next.
4. **Feel.** Where is the peak of this flow and is it marked? How does it end? Is any result
   delivered as a receipt that could be a gift? Are the waits and errors wrapped in care?
5. **Mechanics.** If the screen is part of a loop: what brings the user back on its own, what
   do they lose by leaving, what does the product know about them that it shows back? If it
   sells: is the structure right before the price is argued about?

Score point of view, consistency and execution from 1 to 5 each (the scorecard in
`references/direction.md`), then write the report. Order findings by impact on trust and
conversion, not by the order you noticed them, and give each one a reason the user can repeat to
a colleague. Prefer five findings that change behaviour over twenty that pad the list.

### Audit report format

```
# <Screen or flow> audit

Scorecard: point of view N/5 · consistency N/5 · execution N/5
One line on what this product seems to believe, and whether the screen shows it.

## Fix first
1. **<finding>** — what is wrong, in the user's terms.
   Why it matters: <the recipe's reason, one or two sentences>.
   Fix: <the concrete change, with numbers where the recipe has them>.
2. ...

## Also worth doing
- <smaller findings, same shape, one line each>

## States not yet designed
<list, or "all present">

## What is already right
<two or three things to keep, so the fixes don't flatten them>
```

## Build mode

Never start with the screen. Start with a direction brief, because the models' failure mode is
to produce the average of every app ever made, and the brief is the only thing that prevents it.
Write the brief down (in the response, or in a short file beside the design) before drawing or
coding anything:

```
Direction brief
- Buyer: who, and what "premium" and "trustworthy" mean to them (calm and warm? sharp and fast?)
- Character: two or three concrete words. Clean, modern, sleek, minimal and premium are banned
  here, because they describe every template and so decide nothing
- World: the place or material the product belongs to (paper and ink, instruments and night
  shifts, maps and window light). It sets the tint of the neutrals, the accent and any visual
- The one idea: the single feeling or promise every screen will honour
- The hidden assumption we bet against: what the category assumes about users, and our opposite
- The one user we over-deliver for, and what we therefore leave out
- The peak moment and the ending of this flow
- One decision in this design only this company would make
```

Then proceed through the layers, reading the matching reference as you go:

1. **Foundation first.** Map the flow as steps, mark every decision point, cut the ones that
   add nothing, and list every state each screen can be in. Design the dead ends and failures
   before the happy path looks pretty; they are cheaper to get right now and they are where
   trust is won.
2. **Surface by the numbers.** Apply `references/visual-rules.md` as passes in a fixed order,
   each finished across the whole screen before the next: spacing, colour, icons, copy, type,
   layout, details, visuals, motion. Spacing first because everything reads differently once the
   rhythm is right; copy before type and layout because the length of the headline decides its
   size and where it sits; visuals and motion last because they should fit a screen that already
   works without them. The targets: one font (two at most), four sizes and two weights, the
   8-point grid, relationship spacing at 2x, 60/30/10 colour with the brand colour reserved for
   what must pop, outcome copy, one primary action. Keep the chrome quiet and put the richness
   into one or two moments of content; slop spreads colour over the chrome, craft spends it
   once. Then break the grid once on purpose so the page has a rhythm.
3. **Emotion at the peak and the end.** From the brief, build the one magical moment and the
   designed ending. Deliver results as gifts (anticipation, reveal, afterglow), not receipts.
   Wrap the waits. Leave everything else quiet.
4. **Mechanics where they belong.** If the thing you are building is part of a return loop or
   a purchase, apply `references/retention.md` or `references/paywalls.md`: a routine cue and
   forgiveness, a clock, stakes on screen, identity the user can show, structure before price.
5. **Self-audit.** Run the audit layers over your own output before handing it over, and say
   what you left undesigned and why.

Deliver the brief, the design (code, spec or copy, whichever the user asked for), and the
self-audit. Where the design is code, every state in the state list must exist in the code, not
just the default. Where it is a spec, write the exact on-screen copy; "a reassuring message
here" is the vagueness this recipe exists to remove.

**Checkable facts are real or marked, never invented.** A sample question with a paper, year
and mark; a statistic; a named person; a price; a count of users. The recipe asks for proof
points because a sceptical visitor will check them, so a wrong one costs more than none. Use a
fact you have verified, or label it a placeholder (`{real question from the owner's bank}`) and
say so in the hand-over. The same goes for numbers quoted from the recipe itself: cite them as
the recipe's figures, not as this product's results.

### Improving something that already exists

"Make this better" is an audit followed by a build, and the owner judges it by eye. So:

- Score it first and say the scores out loud. If point of view is 1 or 2, the job is a new
  direction and the result should look different at a glance. If it is 3 or above, say that the
  look is right and name where the remaining gains are (usually states, dead ends, the ending,
  the peak), so nobody expects a different page.
- Even when the look stays, make at least one change the eye catches: the peak moment made
  visible, the one deliberate grid break, the decision only this company would make shown on
  the surface, the ending designed. Structural fixes are real but invisible in a screenshot; the
  owner should be able to see that work happened.
- Hand over a before/after list: each change, what it fixes, and the recipe reason, plus the
  measured table from `scripts/measure_html.py` run on both files. The owner compares
  screenshots; the list and the numbers are how the invisible changes get credit.
- When the audit finds almost nothing wrong, say so plainly and offer two or three refinements
  with exact values, applied only if the owner agrees. Never change a good screen to make it
  different; a changed screen is not an improved one.
- Render to check your work at most three times. More than that is polishing the check, not the
  screen, and it is where the hours and tokens go.

## Dashboards and data screens

Most products have a screen where the user reads numbers, and most stop at showing the data: a
grid of equal boxes, every number the same size, a chart because dashboards have charts. The
recipe's rules for these screens:

- The data is rarely the product; what the user should feel or do about it is. Lead with the
  one number or sentence that answers "how am I doing and what now", at display size, and make
  everything else quieter. Carrot Weather sold the same forecast as Apple by making the
  character's reaction the headline. [MAvKHToGiVY]
- Put the stake or the comparison on screen, not just the metric: against last week, against
  the target, against people like them. A metric alone is a report; a metric against something is
  a reason to act. [MAvKHToGiVY, yBpv5rZoBjA]
- One primary action per screen, the only element that pops; strong contrast on what drives
  the outcome, low contrast on everything else. A dashboard with seven equal cards has no
  primary action. [AnL49w4yIOw, D9SXaj6qQIQ]
- Design the states a dashboard actually lives in: no data yet (the first week), partial data,
  loading, stale, error. A new user's dashboard is empty; that screen decides whether they come
  back. [8EAYZe6y3I8]
- Information-heavy screens should stay visible and scannable rather than hidden behind an
  assistant, but the mechanical parts (summarising trends, flagging anomalies, recommending the
  next action) are where automation belongs. [zRUoPIwCxfw]
- Four type sizes, two weights, the grid, one brand colour spent on the one thing that matters.
  Numbers in a monospace or tabular face so columns align. [86PGRyQjdzQ]

## The numbers, for quick reference

The full rules and their reasons are in `references/visual-rules.md`. These are the ones that
come up in nearly every audit:

| Element | Rule |
|---|---|
| Fonts | one; two at most rendered as text (display + body). A handwriting or decorative face inside a mock scan or illustration is a third and needs a reason; system stacks count |
| Type | four sizes, two weights; cut whatever you have by two |
| Measure | text no wider than 600 px |
| Grid | 8-point (4 acceptable); every number divisible by 8 or 4 |
| Spacing | related items at the base gap, the next group at 2x (24 inside, 48 between) |
| Sections | 160 px vertical padding; 32 px inside cards; 80 to 96 px between text and image |
| Container | 960 to 1200 px max width; 12 / 8 / 4 columns |
| Colour | 60 / 30 / 10, or three colours: base, primary for actions, neutral for text |
| Text hierarchy | by opacity: about 80% large, 60 to 70% small |
| Secondary surfaces | primary at 5% opacity for secondary buttons and highlighted cards |
| Landing page | one call to action; a softer secondary only for mixed intent |
| Onboarding | value inside 60 seconds unless length buys personalisation or filters buyers |
| First impression | judged in 50 ms, trust decided in 3 s; a bad first screen loses 20 to 30% |

## The eight questions to ask of anything

When unsure what to say about a design, these questions always produce the finding:

1. What does this product believe, and does this screen show it?
2. Does the user know what just happened, how to undo it, and what to do next?
3. What happens when it fails, is empty, or is slow?
4. What is the one action here, and is it the only thing that pops?
5. Would a scanner catch what it is, why it helps, and what to do next?
6. Where is the peak, and how does it end?
7. What changes on its own that brings the user back, and what do they lose by leaving?
8. What decision here could only this company have made?
9. The template check: if you swapped this product's name for a competitor's, would the screen
   still fit? If yes, the direction has not reached the copy, the visual or the details.

## Credits

Every design idea in the references is Tim Gabe's, from his YouTube channel (@TimGabe); the
video id in brackets after each rule says which one. The audit's shape borrows from Damir
Sokolovsky's unslop (CC BY 4.0, x.com/heydamir) and Matt Shumer's unslop (MIT,
github.com/mshumer/unslop); the ideas and wording here are our own beyond that.
