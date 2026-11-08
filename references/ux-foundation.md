# Experience foundation: the flow and every state

## The core loop, before any visual

Clarify and map the core experience before touching design software. A strategy document, then
screen maps of every part of the flow and its features, then wireframes and prototypes to find
the most efficient path. Being strict about this order is what stops a beautiful interface from
sitting on a flow that takes half an hour to order a pizza. [AnL49w4yIOw]

## The three things a user must always know

Walk the core flow and make sure at every step the user knows what just happened, can take it
back, and knows what to do next. In a 2026 study of five AI building tools, about a quarter of
the design reasoning the tools gave never reached the interface, and the parts skipped were
exactly these: showing what the system is doing, undo, recovering from an error. Researchers
called the gap "design theater". The brain keeps score of every "did that work?" and judges the
product by the effort. [8EAYZe6y3I8]

## Design every state as carefully as the success screen

Open the product and break it on purpose: turn off the network mid-flow, fail a payment, empty
every list. Then design those states with the care of the happy path. Reasons:

- The service recovery paradox: a failure handled well leaves people as happy as no failure, or
  happier. Chrome's offline T-Rex game was played 270 million times a month. [8EAYZe6y3I8]
- One bad experience is enough for about a third of people to leave. [8EAYZe6y3I8]
- For a money app the status screens *are* the product, because people pay with Apple Pay and
  only open the app to check what happened. SoulCard got 15 designed status screens (processing,
  on hold, declined, two of eight confirmations) and successful deposits rose 71%. [0GMQRCnOQmo]
- An unexplained wait feels longer than an explained one. "Pending" becomes "Your transfer is on
  hold while we complete routine checks", with a support button right there. [0GMQRCnOQmo]
- A declined payment that just says nothing is where users are "left alone". Tell them what to
  check and give them the human in one tap. [8EAYZe6y3I8]
- Undertone's mic test told users their 20-second recording "doesn't count" and gave them
  nothing; a founder estimated 10% of downloads never came back. "I was expecting anything
  instead of nothing." A dead end at the first touch of the core feature sets the trust for
  everything after. [YA3QpYIKqNI, 8EAYZe6y3I8]

## Screen 80 sits next to screen 1

People use the product as one thing for months, while teams review it one screen at a time.
Undertone had two separate "you've used all your sessions" screens with no count and no date.
One pattern replaced both: a "2 of 2 sessions used" badge, a sentence, the exact refresh date.
Small on its own; at scale it is the difference between one product and 80 screens that
disagree. Use the product for an hour as a real user and write down every spot where it stops
feeling like the same product. AI makes this worse because a new screen costs a minute.
[8EAYZe6y3I8]

People also cannot tell you how much inconsistency slows them. Moving a nav bar from left to
right more than doubled time on page and slowed the next pages too, and users said it had not
slowed them much. Trust the audit, not the survey. [8EAYZe6y3I8]

## Remove the exit ramps, then stop

- Map every step from sign-up to first success and look for the pause, the confusion, the
  extra tap. Netflix found 15% of viewers fast-forwarding intros, built Skip Intro, and by 2022
  it was pressed 136 million times a day; skippers binge longer. Micro-frictions compound into
  experience debt. Find your one to three biggest and remove them: smart defaults, one-click
  common actions, sample data instead of empty dashboards. [hIm3d3JAsPw]
- Map every decision point in the core flow. Each is a place to say "never mind". Netflix on a
  phone has at least six before content plays; ReelShort has none (open, it plays, swipe for
  next). Remove the taps, screens and "are you sure?" prompts that do not protect the user from
  a real mistake. [7dCZrtH15zc]
- Apple's three-tap rule: the most important things sit within about three actions. Remove
  everything, then add back strategically; reveal complexity only when needed; hide secondary
  actions; optimise the common case. [doiaMtD80p8]
- One clear focus per screen (Hick's law): Apple Fitness opens to "Let's go", not 30 workouts.
  Big, close targets for the primary action (Fitts' law): Waze's buttons are large and under
  the thumb because the driver has one hand and no attention. Design for distraction. [D9SXaj6qQIQ]

But the goal is the friction sweet spot, not zero friction. Strip too much and users are no
longer guided to the value. A story-style carousel on the welcome screen carries the value
proposition without extra onboarding screens; expandable tooltips hide secondary data without
hiding it. Find the balance for this product rather than applying "shorter" blindly.
[v1f9iYZ2GhQ]

## Onboarding

The default rule: as short as possible, and better, surface tangible value as fast as possible.
Granola onboards in two screens (sign in, allow microphone) and the value lands in the next
meeting you were going to have anyway. Tinder: log in, photos pulled automatically, start
swiping, under a minute; its sessions ran 11 minutes against competitors' 3. Apps lose about 77%
of users in three days, and onboarding is the lever. [Aa89MC8jX2c, 4yKtlOWClhA, 55hDj88zKa8]

The exception: a long onboarding is right when it buys something the user needs in order to
stick. Either a personalised first experience that would feel generic without the data (Cal AI's
20-plus questions; Noom's 113 screens), or a filter for buyers, because people who finish a long
quiz have shown deep pain and willingness to pay. Effort before the payoff also makes the payoff
feel earned (the Aronson and Mills effect), which is why quiz-style onboarding is everywhere.
[Aa89MC8jX2c, nQKWYmrixCU]

Patterns that work inside onboarding:

- Let them taste the product before asking for anything: a real breathing session, a first
  puzzle with hints, a sample recap. Value in the first 60 seconds. [55hDj88zKa8]
- Move the scary first use into the flow people already finish. Undertone's mic test moved into
  onboarding, where completion was high, and ended with a real recap instead of a wall.
  [YA3QpYIKqNI]
- Three steps feel finishable; twelve do not. Show progress (step 2 of 5) when the count is
  small; hide the count when it is long, because "12 steps" before any value is a reason to
  leave. [55hDj88zKa8]
- Personalise early (voice, speed, preferences) so the product feels theirs. [55hDj88zKa8]
- Give people something that feels like theirs before you ask for money. SoulCard's first step
  was picking your card; endowment does the rest. [0GMQRCnOQmo]
- Do not read a high completion rate as a good onboarding. It may be measuring how badly people
  needed the app that week. Look at what happens after. [YA3QpYIKqNI]

## Trust in high-stakes products (money, health, law)

Every screen answers one of three worries, in this order as the relationship deepens:

1. **Is this company real?** The hero animation ends on plain promises ("Card issued in
   seconds. No annual fees. Refund anytime.") so the questions are answered before they are
   asked. The product is shown in normal life (hotels, taxis, groceries). The look must read as
   a company that will exist next year, not a fresh startup. [0GMQRCnOQmo]
2. **What if something goes wrong?** Fees shown before paying, not at the end; a hidden fee
   found later feels like a trick and nobody makes a second deposit with an app that tricked
   them. A clear warning beats a maybe ("Use the wrong network and your money may be lost").
   Progress on every transfer (2 of 8). Explained waits. [0GMQRCnOQmo]
3. **Am I still in control?** One-tap freeze, limits, PIN, hide balance; most people never use
   them, but knowing the button exists is what makes them feel safe (the 1972 noise-button
   study). A human reachable in one message on the channel they already use. The features that
   keep people are sometimes the ones they never touch. [0GMQRCnOQmo]

Certainty converts: Uber's single estimated price beat a price range by double digits in rides
per user. Where transparency builds trust, be specific. [puldme__Ckk]

## Data screens and dashboards

Most products have at least one screen where the user reads numbers, and most stop at showing
the data the way every competitor shows it: a chart, a row of figures, a list, a table. The
personality gets bolted onto the edges (a mascot on the loader, confetti on first save) while
the core surface stays a report. [MAvKHToGiVY]

- Decide what the user should feel or do about the data, and lead with that: one headline
  number or sentence at display size, the rest quieter. Carrot Weather used Apple's forecast
  data and charged for it because the character's reaction to the weather *was* the forecast.
  [MAvKHToGiVY]
- Put the stake or comparison next to the metric: against the target, last week, or people like
  them. Metrics designed as a mirror make the user think about where they stand; metrics
  designed as a report make them close the tab. [yBpv5rZoBjA, BxhsCu9hNpY]
- One primary action per screen (Hick's law) and contrast spent only on what drives the
  outcome; seven equal cards means nothing leads. [D9SXaj6qQIQ, AnL49w4yIOw]
- The states a dashboard lives in most are not the full one: the first week with no data, a
  partial sync, a stale number, a failed load. Design them; the empty dashboard is the one a new
  user sees. [8EAYZe6y3I8]
- Information-heavy screens (investment dashboards, operations views) should stay visible and
  scannable; automation belongs on the mechanical parts, summarising trends, flagging anomalies
  and recommending the next action, not on hiding the numbers behind an assistant. [zRUoPIwCxfw]
