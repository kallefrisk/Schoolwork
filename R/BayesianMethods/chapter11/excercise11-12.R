# Load some packages
library(bayesrules)
library(rstanarm)
library(bayesplot)
library(tidyverse)
library(broom.mixed)
library(tidybayes)

data("penguins_bayes")
penguins_bayes <- penguins_bayes %>%
  drop_na(c(flipper_length_mm, bill_length_mm, bill_depth_mm, body_mass_g, species))

predictors <- c("flipper_length_mm", "bill_length_mm", "bill_depth_mm")

for (predictor in predictors) {
  p <- ggplot(penguins_bayes, aes(x = .data[[predictor]], y = body_mass_g, color = species)) + 
    geom_point(size = 1, alpha = 1) +
    labs(
      title = paste("Body Mass vs", str_replace_all(predictor, "_", " ")),
      x = str_replace_all(predictor, "_", " "),
      y = "Body Mass (g)",
      color = "Species"
    ) +
    theme_minimal() +
    theme(legend.position = "bottom")
  
  print(p)  # Need to explicitly print in a loop
}

# Use a somewhat informative prior without interaction terms
penguin_model_3 <- stan_glm(
  body_mass_g ~ flipper_length_mm + bill_length_mm + bill_depth_mm,
  data = penguins_bayes, family = gaussian,
  prior_intercept = normal(3000, 250),
  prior = normal(c(20, 100, 200), c(10, 20, 50), autoscale = TRUE),
  prior_aux = exponential(1, autoscale = TRUE),
  chains = 4, iter = 5000*2, seed = 84735)

posterior_interval(penguin_model_3, 0.95)

# Looking at the intervals it is clear to see that flipper_length_mm has a significant positive association
# While both bill parameters have a somewhat positive association
# We also see that sigma varies greatly, indicating a weak association for these parameters.