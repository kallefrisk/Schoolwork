# Load some packages
library(bayesrules)
library(rstanarm)
library(bayesplot)
library(tidyverse)
library(broom.mixed)
library(tidybayes)

data("penguins_bayes")
penguins_bayes <- penguins_bayes %>%
  drop_na(c(flipper_length_mm, body_mass_g, species))

ggplot(penguins_bayes, aes(x = flipper_length_mm, y = body_mass_g, color = species)) + 
  geom_point(size = 1)

# Use a somewhat informative prior with interaction terms
penguin_model_2 <- stan_glm(
  body_mass_g ~ flipper_length_mm + species + flipper_length_mm:species,
  data = penguins_bayes, family = gaussian,
  prior_intercept = normal(3000, 250),
  prior = normal(c(20, 0, 500, 0, 0), c(10, 20, 100, 50, 50), autoscale = TRUE),
  prior_aux = exponential(1, autoscale = TRUE),
  chains = 4, iter = 5000*2, seed = 84735)

mcmc_trace(penguin_model_2, size = 0.1)
mcmc_dens_overlay(penguin_model_2)
mcmc_acf(penguin_model_2)
pp_check(penguin_model_2, alpha = 1)
# The MCMC-simulations all have good acceptance rates and look stable.
# We see that the regression converges nicely in all chains
# and that our model captures the features nicely.

tidy(penguin_model_2, effects = c("fixed", "aux"),
     conf.int = TRUE, conf.level = 0.95)

penguins_bayes %>%
  add_epred_draws(penguin_model_2, ndraws = 50) %>%
  ggplot(aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_line(aes(y = .epred, group = paste(species, .draw)), alpha = 0.7) +
  geom_point(data = penguins_bayes, size = 1)

# Here I learn that the Gentoo species have a steeper slope compared to the others.
