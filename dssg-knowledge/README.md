# ML: Machine Learning and Practical Validity

## Motivation
By definition this work involves abstracting or disguising the human element by turning a social problem into an optimization problem. It is important to think carefully about how we do that, implicit and explicit assumptions, and common pitfalls.

## Concepts: Mapping a social science problem to ML problem - defining an objective function, ethical questions, potential for misuse, evaluation and validation (just because you’re modeling something well doesn’t mean it’s what you think you’re modeling, or that the application will be effective). Social implications (and potential biases) should be worked out; contextualizing project from a data-driven, practical perspective. ref future ML talks

# ML: Predictive Modeling

## Motivation
People coming from social science or stats background are usually familiar with modeling for interpretation so it is a leap for them to go to throwing as many models and features as possible at a problem.

## Concepts 
Prediction vs. interpretation: what this means for feature generation and model evaluation - you include all information even if it might not be useful, collinearity is not as concerning, feature selection/regularization 

# ML: Model Evaluation 

## Motivation
You build a lot of models. You have to choose between them. How?

## Concepts
Constructing a training/test split, AUC/precision/recall, deciding on a metric based on the context of the problem (ranked list/precision at top K), generalizability (EPA test set bias)


# ML Temporal Cross Validation

## Motivation
Most projects will aim to predict some outcome before it happens, need to build models that don’t leak information so you estimate performance as accurately as possible 

## Concepts
How to choose granularity/observation level (predicting in the next day/week/year), how to set up training and test sets (both conceptually and technically), difference between training window (observations) and aggregation windows (features), how to not cross contaminate, how does model update when more data is added





