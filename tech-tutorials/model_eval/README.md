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
    * overlapping label windows (caveat: dependent 'samples')
    * Exercise: Implement temporal split generator, label generator, feature getter, join on toy data set
      with pre-built features
- Day 2
 3. details on temporal cross-validation (sliding windows, sub-sampling of 
    training splits, (...?...) )
 4. model evaluation in practice (Cincinnati?); trade-offs; notebooks.
    Exercise.
- Day 3
 5. Bias Formulations
 6. Bias Practical (?)
