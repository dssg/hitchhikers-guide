# Model Evaluation and Bias in Data Science Projects

We have 6 lessons - two sessions a day over three days. One session a day (or 
the latter half of the second session in a given day) should be hands-on. We 
can give homework, which could simply be the 'leftovers' of a given day's 
hands-on session.

- Day 1
 1. * introduction & brief outline of workshop
    * examples of DSaPP projects
    * explanation of common data structure (temporal data, entities, ...)
    * examples of common features (spatiotemporal aggregations, prior behavior, 'static' features like demographics)
    * examples of common outcome definitions ('binarizations')
    * What do we mean by 'successful' predictions? Examples of deployments; explain resource constraints.
    * accuracy, precision, ROC
    * top-k precision, recall-precision curves
    * list stability
    * Detour into caveats: We are _not_ working causally. We are _not_ (most of the time) modeling inspection densities.
      We are _not_ (most of the time) providing statistical inference, optimality guarantees, or anything like that. 
      Delineate 'science' vs 'engineering' approach (here, we are sharing conceptual and technical tools, not 
      scientific, or even empirical, knowledge). Encourage questions & suggestions throughout workshop.
     * introduce toy/example dataset and have students connect to SQL DB (*maybe in next session?*)
 2. * simple temporal cross-validation ('as-of' date, label window, feature window, metrics)
    * train, test, evaluation sets (TODO: ensure universal terminology)
    * caveats on temporal cross-validation: incorrect dates, overwritten or backfilled 
      data (example: student dropouts), data updating frequencies (e.g. end-of-year reports), 
      non-stationary derivatives in the data, changes in policy, changes in systems, bias in the 
      labelling process (e.g. biased judges)
    * Exercise: Implement temporal split generator, label generator, feature getter, label-feature
      join, some evaluation metrics, on toy data set with pre-built features
- Day 2
 3. * difference between incident and label dates, and how that influence label generation; 
      caveat on correlates of the incident that are predictive of the label
    * leakage, and examples of hard-to-find leakage
    * prediction horizons (e.g. in education)
    * prediction frequencies (depending on deployment)
    * overlapping label windows (caveat: dependent 'samples')
    * overlapping feature windows (generally no problem)
    * label rank breaking (unknown `k` vs additional randomization)
    * 'status list' of entities - finding labels for `null` entities in a given label window
    * imputation - finding features for `null` entities in a given feature window; counts/mean/median
      caveat on leakage
    * dummification, and the problems of knowing the set of all levels upfront
    * "train however you like, test however you deploy"
    * sub-sampling of training and/or testing data (?)
    * making train and/or test sets more reprensetative (?)
    * modeling/weighting by `P(I)` / inverse probability weighting (?)
    * evaluating predictions in field trials / problems of randomized trials on ranked
      lists (?)
 4. * novelty vs accuracy (Cincinnati?)
    * stability across temporal splits
    * Exercise: Implement label generator with incident-vs-decision date, in-split imputation, 
      global dummification, plots for temporal stability
- Day 3
 5. * characterizing models via entities, not via labels (back ref: list overlap)
    * cross-tabs on categorical features or discretized continuous features between high-risk/low-risk predictions
    * scatter plots on continuous features
    * simple significance tests (chi-square, KS-test); caveat: multiple testing, dependency between features
    * protected class definitions
    * not sufficient: removing protected features
    * population parity
    * disparate impact
    * test equality
    * extension from equal FNR/FPR to independence of score and class; removing dependency on thresholds
    * (is there an equivalent formulation for equal precision?)
    * caveat about curse of dimensionality - marginal bias is 'easy', but interactions of bias are very many 
      (e.g. difficulties of testing not only for discrimination against age, or race, or gender, but also for 
      discrimination against (age x race x gender) )
    * science thriller: ProPublica's COMPASS coverage, initial response articles, follow-up articles
 6. Exercise: calculating cross-tabs on toy data set; calculating condtioned cross-tabs and scatter plots for 
    disparate impact and test equality; applying chi-square test
