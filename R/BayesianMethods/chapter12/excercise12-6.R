# Load packages
library(bayesrules)
library(rstanarm)
library(bayesplot)
library(tidyverse)
library(tidybayes)
library(broom.mixed)

data(bald_eagles)

eagle_model_1 <- stan_glm(
  count ~ year + hours,
  data = bald_eagles, family = gaussian,
  prior_intercept = normal(0, 2.5),
  prior = normal(0, 2.5, autoscale = TRUE),
  prior_aux = exponential(1, autoscale = TRUE),
  chains = 4, iter = 5000*2, seed = 84735)

prior_summary(eagle_model_1)

# Model: Y_i ~ Normal(mu_i, sigma)
# 
# Where:
#   mu_i = beta_0 + beta_1 * year_i + beta_2 * hours_i
#
# Priors:
#   beta_0 ~ Normal(0, 2.5)
#   beta_1 ~ Normal(0, 2.5)
#   beta_2 ~ Normal(0, 2.5)
#   sigma ~ Exponential(1)

pp_check(eagle_model_1, alpha = 1)

# The model is doing good but could be better.
# First of all, a normal model is not going to do good in this scenario
# since the data is discontinuous and the mean doesn't look to be linear.
# The variance is not constant either.