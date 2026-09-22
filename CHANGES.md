# Review Pass: Changes Log

Conservative, review-only pass over the published book. Scope per chapter: (1) genuine
grammar/typo fixes, (2) small local wording fixes for writing-style consistency, (3) minor
tone nudges toward a Molnar-style register. No restructuring, no content/argument/example
changes, no touching code chunks, citations, or `notebooks_student/`. Chapter 1 gets grammar
fixes only, at the most obviously-safe bar, since it's already been read by students.

Each chapter section lists changes made, then a separate list of passages flagged but left
untouched, with the reason.

## Sitewide: image sizing (CSS)

`styles.css` existed but was never actually linked from `_quarto.yml` (its own comment said
so), so it had zero effect on the published site.

- **Added** a general rule so images scale to their container instead of overflowing or
  staying fixed at native pixel width on narrow screens:
  ```css
  img {
    max-width: 100%;
    height: auto;
  }
  ```
  Reason: image sizing / responsive layout, requested separately from the chapter-by-chapter
  pass.
- **Fixed**: added `css: styles.css` under `format: html:` in `_quarto.yml` so the stylesheet
  (and this new rule) is actually applied. Without this the CSS file was dead code.
  Reason: the requested image-sizing fix would otherwise have no effect at all.
- Checked all `![...](...)` images across `chapters/*.qmd` for explicit width overrides
  (e.g. `{width=...}`): none found, so no per-image fixes were needed, consistent with the
  instruction to prefer a general rule.

## Chapter 1: Introduction

Extra-cautious pass, per instructions: grammar/typo fixes only, no style or tone changes,
even where a similar issue was fixed elsewhere in the book.

### Changes made

1. "OpenAI's result was graded by former IMO medalists, DeepMind's performance was
   independently verified by official IMO coordinators." → replaced the comma with a
   semicolon, and moved the `[^imo-2025]` footnote marker from the start of the next
   sentence to the end of this one (it was attached to the wrong sentence).
   Reason: comma splice + misplaced footnote reference (grammar).
2. "A long list of near-synonyms for this field **have** been used" → "**has** been used".
   Reason: subject-verb agreement (singular "list").
3. "...deep learning, and in the old days knowledge discovery, pattern recognition." → added
   a comma after "days". Reason: punctuation/list clarity.
4. "a past  price cut drove a spike in  demand" / "would  affect future sales" → collapsed
   double spaces to single spaces. Reason: typo.
5. "...frequently identical only the setup differs" → "...frequently identical; only the
   setup differs." Reason: run-on sentence (missing punctuation).
6. "This goal is **rather** causal analysis rather than pure prediction" → removed the first,
   redundant "rather". Reason: grammar/redundancy made the sentence hard to parse.
7. "We see this as **a** one of the core Vs" → removed the stray "a". Reason: typo.
8. `...decision I'm about to make?".` → `...decision I'm about to make?"` (dropped the
   redundant period after the closing quote). Reason: punctuation.
9. "not just in usual tech companies" → "not just in **the** usual tech companies". Reason:
   missing article.
10. "hypothetical damage pattern on  a returning aircraft" → single space. Reason: typo.
11. "...total volume at the country level,  which is exactly why..." → single space. Reason:
    typo.
12. "Both snapshots are taken at loan origination  matched against whether..." → "...taken at
    loan origination **and** matched against whether..." (also fixed the double space).
    Reason: missing conjunction made this an incomplete/broken clause.
13. "delinquency history,credit limit changes" → added the missing space after the comma.
    Reason: typo.
14. "...tooling landscape is enormous. Ranging from off-the-shelf..." → joined into one
    sentence: "...is enormous, ranging from off-the-shelf...". Reason: "Ranging from..." was
    a sentence fragment (dangling participle), not a complete sentence.
15. "**Data Understanding**: manipulating, and making sense of raw datasets." and
    "**Data Preparation**: cleaning, and transforming data..." → removed the comma before
    "and" in both two-item lists ("manipulating and making sense...", "cleaning and
    transforming..."). Reason: comma doesn't belong before "and" joining only two items.
16. "Whereas these models can respond **without** supplying the prompt without any training
    data, under the hood they're still built on a predictive learning task" → "Whereas these
    models can respond **by** supplying the prompt without any training data, under the hood
    they're still built on a predictive learning task". Reason: broken sentence, flagged in
    the previous pass and corrected per author confirmation (the point being that the user
    only has to supply a prompt, not training data, to get a response).
17. "However, you might **now** assume that the realm of analytics is limited to..." →
    removed "now". Reason: flagged in the previous pass as an unclear leftover word; author
    confirmed it should go.
18. "**Data Exploration**: visualizing data to find patterns and relationships and quality
    issues." → "...find patterns, relationships, and quality issues." (proper 3-item list).
    Reason: flagged as ambiguous list structure; author confirmed the 3-item reading.
19. "...due to tenure vs product count, **since** the two are so intertwined" → changed the
    second "since" to "because" ("...due to tenure vs product count, **because** the two are
    so intertwined"). Reason: flagged repeated "since...since" in one sentence; author agreed
    it read strangely.
20. "...it helps to fix some vocabulary about a data set **that** you'll see used more or less
    interchangeably..." → "...it helps to fix some vocabulary about a data set, **terms**
    you'll see used more or less interchangeably...". Reason: flagged ambiguous relative
    clause (unclear whether "that" modified "vocabulary" or "data set"); rewording with
    "terms" ties it unambiguously to the vocabulary, not the data set.
21. "A 'messy' table ... versus a 'tidy' table ... **contain** the same information" →
    "...**contains** the same information". Reason: flagged as a subject-verb agreement
    question; author confirmed "contains".

### Flagged, not changed

- "The omnipresence of and reliance on analytics has increased..." — grammatically valid but
  clunky (one preposition each for "omnipresence" and "reliance" sharing one object). Not
  changed because it isn't a genuine error, and Chapter 1 is grammar-fixes-only in this pass
  (no style nudges).
- "...only later exploit prescriptive analytics..." — this sentence walks through the
  maturity hierarchy but only names descriptive, predictive, and prescriptive, skipping
  diagnostic (which is one of the four types defined just above). Possibly intentional
  (diagnostic often sits close to descriptive in maturity models), but flagging since it reads
  like an omission. Left as is: fixing it would mean adding content, not wording.

## Chapter 2: Python for Data Analytics

Normal scope for this pass (grammar, small style-consistency wording, minor tone nudges).
This chapter is almost entirely short reference-style prose next to code cells; the code
itself was left untouched throughout, per instructions.

### Changes made

1. "customers and **newpapers** subscriptions data" → "customers and **newspaper**
   subscriptions data". Reason: typo.
2. "...errors come down to arrays not having the shape." → "...not having the shape **you
   expect**." Reason: the sentence was missing its object; "the shape" alone doesn't parse as
   a complete thought.
3. "...crucial before moving **into to** realm of data understanding..." → "...before moving
   **into the** realm of data understanding...". Reason: typo (duplicated/wrong preposition,
   missing article).
4. "`pandas` can read most common tabular formats, like CSV and Excel including files with no
   header row..." → added a comma after "Excel": "...like CSV and Excel, including files with
   no header row...". Reason: without the comma, "Excel including files with no header row"
   misleadingly reads as if it's describing Excel specifically rather than tabular formats in
   general.
5. "...and then applies **a** specific aggregation function**s** to each group." → removed
   "a": "...applies specific aggregation functions to each group." Reason: article/number
   mismatch ("a" with a plural noun).
6. "This a fast way to implement a transformation..." → "This **is** a fast way to implement a
   transformation...". Reason: missing verb.
7. Nested-dictionary example: `"city": "brussels"` → `"city": "Brussels"`. Reason: flagged as
   inconsistent with "Ghent" (capitalized) elsewhere in the same example; author confirmed the
   fix despite being inside a code chunk.
8. Code comment `#in VSCode it better to use: %pip install package_name` →
   `# in VSCode it's better to use: %pip install package_name`. Reason: flagged typo/missing
   space in a code comment; author confirmed the fix.

### Flagged, not changed

(none remaining for this chapter)

## Chapter 3: Data Understanding

### Changes made

1. "And if the data **can** be trusted, the model itself can't be trusted either: garbage in,
   garbage out." → "And if the data **can't** be trusted..." Reason: this was a clear
   negation typo, the sentence directly contradicted its own "garbage in, garbage out" point
   as written.
2. "For **exampl**, a churn model..." → "For **example**, a churn model...". Reason: typo.
3. "...post-COVID world, where **there** behavior changed drastically." → "...where **their**
   behavior changed drastically." Reason: there/their typo.
4. "**Focussing** on only the active customers is also a **nice** example of survivorship bias
   as seen in **Chatper** 1." → "**Focusing** on only the active customers is also a **clear**
   example of survivorship bias as seen in **Chapter** 1." Reason: "Chatper" was a typo;
   "Focussing" (British spelling) → "Focusing" for consistency with the rest of the book's
   American spelling; "nice" → "clear" as a minor tone nudge (a touch more neutral/precise).
5. "NPC's date columns  (when a subscription..." → collapsed the double space. Reason: typo.
6. "...will happily compute its mean **which** is a number with no meaning whatsoever." →
   added a comma before "which". Reason: non-restrictive clause needs a comma.
7. "Another option is **web scraping** which involves..." → added a comma before "which" for
   the same reason as #6.
8. "...isn't the same as making data anonymous **and** you have to think about..." → added a
   comma before "and". Reason: joins two independent clauses (compound sentence).
9. "...this way **which** is a clear violation of transparency." → added a comma before
   "which". Same reason as #6/#7.
10. "Of course **if was never the intended** that the complaints would be used for this
    purpose." → "Of course, **it was never intended** that the complaints would be used for
    this purpose." Reason: "if"/"it" typo and a stray extra "the" made the clause
    ungrammatical.
11. "This allowed **identifying him to** his own social circle as someone whose family
    property..." → "This allowed **his own social circle to identify him** as someone whose
    family property...". Reason: "allowed identifying X to Y" is not a grammatical English
    construction; swapped subject/object so the sentence parses, without changing what it
    says.
12. "**On** some cases, someone stayed flagged..." → "**In** some cases, someone stayed
    flagged...". Reason: wrong preposition.

### Flagged, not changed

- None. Every issue found in this chapter had a safe, unambiguous fix.

## Chapter 4: Data Exploration

### Changes made

1. "`.describe()` can't tell these apart. A scatter plot can **immediatly visualizes** the
   differences." → "...can **immediately visualize** the differences." Reason: typo
   ("immediatly") plus subject-verb agreement after "can" (needs the base form "visualize").
2. "For **examlpe**, treemaps, Sankey diagrams..." → "For **example**, treemaps..." Reason:
   typo.
3. "Once your goal shifts from *exploring* to *explaining* the chart itself is only half the
   job" → added a comma after *explaining*. Reason: the introductory clause needs to be set
   off from the main clause.
4. "...lines, text, bars, points) ." → "...lines, text, bars, points)." Reason: stray space
   before the period.
5. "...to visualize any **ordere** series...a simple **example.Plotting** `TotalPrice`'s..." →
   "...any **ordered** series...a simple **example. Plotting** `TotalPrice`'s...". Reason:
   typo ("ordere") and a missing space after the period.
6. "...drop any *later* variable...This means that you keep the first occurrence and
   **removing** the rest." → "...and **remove** the rest." Reason: parallel structure (both
   verbs after "you keep...and" should be the same form).
7. "It often happens when you have a situation where the true value is not available at the
   time of observation." → "It often happens when the true value is not available at the time
   of observation." Reason: tone/concision, trimmed the redundant "you have a situation
   where".
8. "a tenancy agreement **that'still** ongoing" → "a tenancy agreement **that's still**
   ongoing". Reason: typo (garbled contraction).
9. "You just don't know the actual end date in the future **and** you will consider..." →
   added a comma before "and". Reason: joins two independent clauses.
10. "...this flags well over 10% of all training rows **which** is far too many..." → added a
    comma before "which". Reason: non-restrictive clause needs a comma.
11. "...as a potential outlier.  On some variables here," → collapsed the double space.
    Reason: typo.

12. "One is a clean linear relationship, one is a clear curve with a straight line fits poorly
    due to an outlier, one is a vertical line of points plus one outlier." → "One is a clean
    linear relationship, one is a clear curve, another has a straight line that fits poorly
    due to a single outlier, and one is a vertical line of points plus one outlier." Reason:
    flagged as broken/merged, only describing 3 of Anscombe's 4 datasets; author confirmed
    this reconstruction.
13. "Even though, as we saw in the introduction, a purely predictive model can often tolerate
    it from a pure predictive perspective, it can still cause issues in interpretation and
    make the model less robust." → "Even though, as we saw in the introduction, a purely
    predictive model can often tolerate it without losing accuracy, it can still undermine
    any post-hoc explanation of that model (e.g., unstable feature importances) and make the
    model less robust." Reason: flagged as confusing/self-contradictory (a purely predictive
    model "having issues in interpretation" didn't fit Chapter 1's own predictive-vs-causal
    framing); author clarified the point is about post-hoc explanation methods applied to an
    otherwise black-box predictive model, which the rewrite now makes explicit.

### Flagged, not changed

(none remaining for this chapter)

## Chapter 5: Data Preparation

### Changes made

1. "A straight line can't capture this rise-then-plateau-then-fall pattern. What it actually
   does is **creating** a misleading representation..." → "...What it actually does is
   **create** a misleading representation..." Reason: "does is X-ing" is not a standard
   construction; needs the base verb form ("does is create").
2. "...depending on the needs of different **columnsn**..." → "...different **columns**...".
   Reason: typo.
3. "A one-hot column only ever takes the values 0 and 1 **and** standardizing it doesn't make
   it more useful." → added a comma before "and". Reason: joins two independent clauses.
4. "**Target (mean) encoding**, **which** goes a step further and replaces each category with
   the actual mean of the target..." → removed "which": "**Target (mean) encoding** goes a
   step further and replaces...". Reason: with "which" attached, this was a sentence
   fragment (no main verb); the two encoding methods described just above it ("Manual
   ordinal encoding uses...", "Automated ordinal encoding orders...") are both complete
   sentences, so this also restores the parallel structure.
5. The three "which to use" bullets at the end of the Ordinal Encoding section were
   rewritten for both a grammar fix and style consistency:
   - "**Manual encoding** when you have a clear, defensible business hierarchy, it stays
     interpretable, but isn't necessarily optimal for prediction." → "**Manual encoding**:
     use when you have a clear, defensible business hierarchy. It stays interpretable, but
     isn't necessarily optimal for prediction."
   - "**Automated (feature-engine) encoding** when you'd rather let the data reveal the
     order, useful for finding surprising patterns..." → "**Automated (feature-engine)
     encoding**: use when you'd rather let the data reveal the order. Useful for finding
     surprising patterns..."
   - "**Target encoding** when predictive power matters most it creates the strongest
     statistical relationship..." → "**Target encoding**: use when predictive power matters
     most. It creates the strongest statistical relationship...". This one also had a
     genuine run-on (no punctuation at all between "matters most" and "it creates"), not
     just a style issue.
   Reason: the third bullet was a real grammar error (run-on); all three were also
   inconsistent with the "**Term**: description" pattern used for equivalent bulleted
   definitions everywhere else in the book (e.g., Chapter 4's "Structurally missing:
   ...", "Non-applicable: ...").
6. "They're not competitors and they try to solve the same problem, namely turning a
   categorical variable into numbers, but they sit at opposite ends of the cardinality
   spectrum." → "They try to solve the same problem, namely turning a categorical variable
   into numbers, but they're not really competitors, since they sit at opposite ends of the
   cardinality spectrum." Reason: flagged backwards logic ("and...but" connected the clauses
   the wrong way round); author confirmed the reordering.
7. "Their actual aggressiveness level is an inverted U-shape curve, quantified with a
   quadratic term in a plain linear regression too." → "The effect of aggressiveness level
   is an inverted U-shape curve, quantified with a quadratic term in a plain linear
   regression too." Reason: flagged as not quite parsing ("a level" isn't "a curve"); author
   confirmed the fix.

### Flagged, not changed

(none remaining for this chapter)

## Chapter 6: Model Evaluation

### Changes made

1. "The previous two chapters turned **a raw tables** into a clean, model-ready basetable." →
   "...turned **a raw table** into..." Reason: article/number mismatch.
2. "...every performance number you report afterwards is **fiction** and unreliable." →
   "...is **fictional** and unreliable." Reason: parallel structure ("fictional and
   unreliable" are both adjectives; "fiction and unreliable" mixed a noun with an adjective).
3. "As soon as you compare several models or fine-tune hyperparameter **set[newline]tings**,
   a plain train/test split isn't enough." → "...hyperparameter **settings**...". Reason:
   the word "settings" was corrupted, split across a line break into "set" and "tings" (a
   genuine text-corruption bug, not a line-wrap artifact).
4. "The final test set in the outer loop is already present  with the existing 20% holdout"
   → collapsed the double space. Reason: typo.
5. "Cross-validation can play either role, or both at once, which gives potential setups:" →
   "...which gives **three** potential setups:" Reason: the list right after has exactly
   three bullets; "potential setups" alone was missing its count.
6. "Hence, **fully nested cross-validation** is the fully nested setup and it removes the
   last dependence..." → "Hence, **fully nested cross-validation** removes the last
   dependence...". Reason: removed a circular, self-referential clause ("X is the X setup").
7. "Performance that looks too good-to-be-true, **is** also often not true." → removed the
   comma before "is". Reason: the comma incorrectly separated the subject from its verb.
8. "...know exactly which point in time separates 'known' from 'future' before touching the
   data and stick to this **is** in your preprocessing and splitting." → removed the stray
   "is". Reason: broke the sentence ("stick to this is in" doesn't parse).
9. "Increasing complexity beyond this (more variables, **comples transformations trees**)
   makes things worse..." → "...(more variables, **complex transformations, trees**)...".
   Reason: typo ("comples" → "complex") and a missing comma to make this a proper 3-item
   list.
10. "let's **consdider** a synthetic time series example" → "let's **consider**...". Reason:
    typo.
11. "**Threshold-independent metrics**, ROC and AUC, precision-recall curves, **lift**, look
    instead at..." → "...precision-recall curves, **and lift**, look instead...". Reason:
    missing "and" before the final list item (the parallel sentence two lines above,
    describing threshold-dependent metrics, does include "and the rest").
12. "...searches for the threshold that maximises a chosen metric, using internal
    cross-validation **.**" → removed the stray space before the period. Reason: typo.
13. "On strongly imbalanced data, ROC/AUC can be misleading too... **Since** the false
    positive rate has a huge true-negative denominator, **so** it stays low..." → removed
    "Since": "The false positive rate has a huge true-negative denominator, so it stays
    low...". Reason: "Since X, so Y" uses two conjunctions for one link between clauses;
    only one is needed.
14. "Note that a random classifier's  AP equals..." → collapsed the double space. Reason:
    typo.
15. "The AUCs are **clsoe** to each other..." → "...are **close** to each other...". Reason:
    typo.

16. "Neslin et al. (2006) showed that a retention campaign's expected profit is a direct,
    increasing function of lift..." → "@neslin2006defection show that a retention campaign's
    expected profit is a direct, increasing function of lift...". Reason: flagged as a
    plain-text citation with no matching bib entry; author supplied the full reference
    (Neslin, Gupta, Kamakura, Lu, & Mason, 2006, *Journal of Marketing Research* 43(2),
    204-211), added as `neslin2006defection` in `references.bib`, and the in-text citation
    switched to the book's `[@key]` format (tense changed from "showed" to "show" to match
    the book's convention for citations used as a sentence subject).

### Flagged, not changed

(none remaining for this chapter)

## Chapter 7: Modeling

This chapter had picked up some edits since it was originally written, including one
text-corruption bug matching the same pattern found and fixed in Chapter 6.

### Changes made

1. "...helping to prevent overfitting and **app[newline]roximate** the true test error." →
   "...**approximate** the true test error." Reason: the word "approximate" was corrupted,
   split across a line break into "app" and "roximate" (same bug pattern as Chapter 6's
   "settings").
2. "**Notice, that** this cross-validated selection doesn't fully match..." → "**Notice
   that** this cross-validated selection doesn't fully match...". Reason: stray comma
   between "Notice" and "that".
3. "This is **why** logistic regression is actually fitting a straight line to." → "This is
   **what** logistic regression is actually fitting a straight line to." Reason: "why...to"
   leaves "to" with nothing to attach to; "what" is the relative pronoun the sentence needs
   (this was flagged as broken during an earlier pass in this same conversation, and had
   since been reverted back to "why"; reapplying the fix now as part of this formal review).
4. "This is the most common default... **This is** impractical for very large $K$..." →
   "...**It becomes** impractical for very large $K$...". Reason: minor tone/flow nudge to
   avoid two consecutive sentences both starting with "This is".
5. "Learning to build them well is a natural next step once the fundamentals covered in this
   book. However, ..." → "...once the fundamentals covered in this book **are second
   nature**. However, ...". Reason: the sentence was missing its verb ("once the
   fundamentals... [are what?]"), left dangling, most likely from an edit that trimmed the
   original ending; restored it.

6. "Lasso tends to work well when only a handful of predictors actually matter and high
   variance between the predictors (a small 'true' model hiding among many candidates), while
   Ridge tends to work well when most predictors carry a similar, modest amount of signal
   (low variance between the predictors)." → "Lasso tends to work well when there is high
   variance in the true effect sizes: a small number of predictors have large coefficients
   while the rest are close to zero (a small 'true' model hiding among many candidates).
   Ridge tends to work well when the effect sizes have low variance instead, i.e. most
   predictors carry a similar, modest amount of signal." Reason: flagged as grammatically
   unparallel and ambiguous about what "variance" referred to; author confirmed it means
   variance in the true effect sizes/coefficients (Lasso: high variance, a few large
   coefficients among many near-zero ones; Ridge: low variance, most coefficients similarly
   modest), now made explicit.
7. "The coefficients can also easily be interpreted in terms of log-odds and odds ratios,
   which are more interpretable than the raw regression coefficients." → "Its coefficients
   can also easily be converted into odds ratios, which are considerably more interpretable
   than the raw log-odds coefficients themselves." Reason: flagged as circular (log-odds
   coefficients are the raw coefficients, so grouping them with odds ratios as both "more
   interpretable" didn't quite make sense); author confirmed the odds ratio specifically is
   the interpretable one of the two.

### Flagged, not changed

(none remaining for this chapter)




## Appendix: Installation Guide

### Changes made

None. A careful read-through, plus the same mechanical checks used for every other chapter
(double spaces, missing space after a period, em-dashes), found nothing to fix. This appendix
is short and purely instructional, and it already reads cleanly and consistently with the rest
of the book.

### Flagged, not changed

(none)
