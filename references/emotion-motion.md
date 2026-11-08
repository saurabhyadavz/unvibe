# Emotion and motion: where the feeling goes

## Why emotion is the differentiator now

Decent UX, decent UI and decent branding are table stakes; components are free and a model will
hand you a good flow in minutes. What none of that gives is connection, personality, a
thought-through experience, and that is what people pick a product for when ten tools do the
same job. In person, emotion happens through tone and body language; in software it exists only
if someone designs it. Most apps today treat users like robots who want efficiency, and users
complete tasks without attaching to anything, so they churn on the next Black Friday deal.
[YA3QpYIKqNI, AnL49w4yIOw, v1f9iYZ2GhQ]

Evidence: Duolingo's 2022 character animation system (facial reactions, lip sync, idle motion)
is credited by its own team as a major reason people stay; daily actives went from 14 million to
34 million in two years. Phantom made crypto feel less scary with an animated ghost and playful
wallet-creation moments and became a top utility app. Revolut's polish tracked its move
upmarket: tactile charts that glow under your finger, cards that flip and catch light. In
fintech "trust literally affects how much users spend", so polish is revenue. [Du2lkZ_cux8]

## Personality lives in the core surface, not the edges

A friendly empty state, confetti on first save and a mascot on the loader are decoration bolted
on while the core surface is still a chart or a list like every competitor's. Carrot Weather
used the same data as Apple's free app and charged for it, because the character's reaction to
the forecast *was* the forecast: you knew what the weather felt like before you read a number.
Sometimes the way you deliver the data is the product. Day One journaling sells against two free
Apple apps by what surrounds the text: weather, place, photos, a timeline, search; the Moleskine
against the IKEA notebook. "Craft is the work users won't see but will feel." [MAvKHToGiVY]

## Physics, not easing

- Springs over bezier curves. Bezier "can feel lifeless"; springs behave like objects with
  weight. Three knobs: stiffness (how many bounces), mass (how heavy and how high the bounce),
  damping (how quickly it settles). Aggressive is stiff, light, low damping; smooth is softer,
  heavier, more damped. Tune until it feels right. [bdR3p6PvYQQ]
- Apple's rubber band at the end of a scroll, haptic clicks on a trackpad that never moves, the
  shutter sound: the digital world behaving like the physical one so nothing has to be learned
  and every action is confirmed. Routine tasks become reassuring. [doiaMtD80p8]
- Transitions carry the user from place to place instead of switching screens on them; the
  brain builds a map. Blur, translucency and parallax keep a strict system from feeling boring.
  [doiaMtD80p8]
- Big behaviour changes happen gradually: the home-button line took years to train billions of
  people to swipe without a tutorial. Guide with cues, not instructions. [doiaMtD80p8]
- Movement during waits reassures: Perplexity's loader and voice dots react in real time, so the
  loop closes and waiting feels like something is happening. Treat in-between moments as
  intentional, not empty. [D9SXaj6qQIQ]

Values from his tutorials, as defaults: an element enters with opacity 0 to 1, 16 to 25 px up, a
slight rotate or scale, on a spring with more damping and some mass, siblings staggered 0.1 s
apart. Loops are slow and mirrored (a 65 s rotation, a 2 s wobble). Hover at 0.5 opacity, pressed
at 0.25. Trigger scroll animations when the section reaches the top or middle of the viewport so
they are not spent before they are seen. Blur is pretty and expensive. Fewer layers render
faster. [various tutorials; see sources.md]

## Motion hygiene

Before adding any motion, remove the motion that means nothing: pulses and pings on things that
are not live, shimmer on headings, breathing glows, floating elements, parallax on everything,
`transition-all`, cards that scale on hover. Keep what explains: a hover is a quick surface
change, a press a tiny scale down, a menu fades and rises a few pixels from where it opened, a
changed number tweens. One easing and a few durations across the screen; at most one entrance on
load, a short fade and rise with a small stagger, never every card flying in from a different
side. Animate transform and opacity, not width, height or position, so it stays smooth on weak
phones. Then spend the saved attention on the two moments below.

## Where to spend emotion: the peak and the end

People remember an experience by its most intense moment and by how it ends, not by the average
(Kahneman's peak-end rule). Disney knows the 90-minute queue sucks and designs the fireworks and
the exit music; 70% come back. Apple's finish line is a box lid that takes two to four seconds to
lift. [11h4H3TAGkM, uoLpH_20qKw]

The procedure:

1. Map the whole journey (sticky notes or a board), every step from sign-up to the end of the
   core task. Mark where the user slows down, where stress peaks, where it is quiet. Keep it as
   a living document. [11h4H3TAGkM]
2. Pick one spot for the peak: after a core task completes, at a milestone, at the point of most
   effort. Put the "holy dang" moment there: a badge, a sparkle, an animation, surprise copy.
   Just one. [11h4H3TAGkM]
3. Design the ending. Most apps just fall off. Close with a check, a summary card, "you showed up
   today, that's huge", a nudge for tomorrow. It need not be fancy; it must be intentional.
   [11h4H3TAGkM]
4. Vacuum the negative moments: waits, errors, long forms. Uplifting microcopy, help before it is
   asked for, delays used as moments instead of dead space. Negative moments are as memorable as
   positive ones. [11h4H3TAGkM]
5. Test variations: timing, emoji versus icon, animation versus static. Watch where people drop
   and where they linger. [11h4H3TAGkM]

Choose moments by business goal, not for the animation's sake. Freecash got a tiered diamond
system because it needed power users returning for years; an AI note-taker got its logo woven
into the daily-use surface; a trust-sensitive crypto audience got emotion front-loaded in
onboarding. You do not need Duolingo's motion budget; you need the right two or three moments.
[wmTkiF23GRQ, AnL49w4yIOw]

Airbnb puts micro-animations and value tags at the moment you find the listing, then a
trademark 3D animation on booking. Uber ends every ride with a vibration, a rating and a tip
prompt because the peak (arriving) already happened and the ending just needs closure. Ahead
builds your personal brief in front of you, then nudges you to come back tomorrow. [11h4H3TAGkM]

## Gift, not receipt

Dopamine is the anticipation chemical; it fires on uncertainty about something good, not on the
thing itself. Hand someone the result flat ("Congratulations" in a modal) and you bypass it.
Every app has moments where it hands the user something: a match, a report, a score, a recap.
Deliver those in three stages:

1. **Anticipation.** A beat where something is about to happen and the user does not yet know
   what. Even a brief build-up changes the response. A pack you are about to open; a recap that
   arrives wrapped and asks to be pulled open.
2. **Reveal.** With weight: visual, haptic, sometimes audio. One item at a time, because the
   same information delivered sequentially is many events instead of one.
3. **Celebration and afterglow.** Confetti, a glow, and then a moment to sit with it: a share
   prompt, a badge, a stat to screenshot. The afterglow is where the result becomes identity.

Robinhood's confetti was powerful enough that regulators banned it; Spotify Wrapped is a
year-long anticipation, sequential slides and a share prompt, and most imitators ship a report
and miss the ceremony; Tinder turned a database event into a full-screen explosion. Undertone's
recap arrives in a sleeve the user peels open, with confetti and a haptic, framed as the first
entry in their mental health record, and the ask to book the next session sits inside that
peak. Take the most transactional moment in your product and ask what it would look like with
weight. [uoLpH_20qKw, YA3QpYIKqNI]

Variable rewards are the honest version of this engine: anticipation towards what is next,
rather than fear of losing a streak. See `retention.md`. [LXX_qOA5D8E]

## Make feedback human

- On repeated actions (check-ins, logging, confirmations) add micro-interactions with instant
  emotional feedback: a bounce, a glow, a sparkle. Celebrate small wins; success states should
  feel intentional, not huge. [Du2lkZ_cux8]
- If there is a mascot, let it react; emotions are contagious. Progress animations give a sense
  of building something over time. [Du2lkZ_cux8]
- In intimidating categories (finance, crypto, health, insurance), polish is trust and every
  micro-interaction is a trust signal; friendly, warm details make heavy topics lighter. Build
  for people, not pros. [Du2lkZ_cux8]
- Design the UI like a movie, not a set of stills: the way screens connect is where the
  experience lives, and it is the mistake even senior designers make. [86PGRyQjdzQ]
- Treat the brief's two edges as rules: Undertone's was "nothing clinical, nothing cute,
  because this is therapy", and the wrapped recap could still feel serious. Tailored beats
  generic delight every time. [YA3QpYIKqNI]

## Ask after the win

Users are most receptive right after a meaningful win, so the timing of an ask matters more
than the ask. Map the biggest wins in each flow, amplify them, and place the rating request, the
upgrade and the share prompt there. Paywalls, tutorials and forced flows shown at moments of
confusion are the common mistake. Netflix's "97% match" and "because you watched" rows are
screenshot moments because they sound human; find the one moment of strongest emotion in your
product and amplify it until people want to share it. [v1f9iYZ2GhQ, hIm3d3JAsPw]
