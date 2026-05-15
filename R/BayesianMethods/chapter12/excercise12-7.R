# Load packages
library(bayesrules)
library(rstanarm)
library(bayesplot)
library(tidyverse)
library(tidybayes)
library(broom.mixed)

data(bald_eagles)

# A poisson regression model would be better since the variance
# is not constant and increases with the mean of the data.
# The data is not looking like its a linear relation either.

eagle_model_2 <- stan_glm(
  count ~ year + hours,
  data = bald_eagles, family = poisson,
  prior_intercept = normal(0, 2.5),
  prior = normal(0, 2.5, autoscale = TRUE),
  prior_aux = exponential(1, autoscale = TRUE),
  chains = 4, iter = 5000*2, seed = 84735)

prior_summary(eagle_model_2)

# Model: Y_i ~ Poisson(lambda_i)
# 
# Where:
#   log(lambda_i) = beta_0 + beta_1 * year_i + beta_2 * hours_iy
#
# Priors (on log scale, since link = log):
#   beta_0 ~ Normal(0, 2.5)
#   beta_1 ~ Normal(0, 2.5)
#   beta_2 ~ Normal(0, 2.5

pp_check(eagle_model_2, alpha = 1)

# This model seems to capture the trends better than the normal model did.
# Looking at the pp-plot, we see that the model is in line with the data.