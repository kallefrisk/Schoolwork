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

# Use a somewhat informative prior
penguin_model_1 <- stan_glm(
  body_mass_g ~ flipper_length_mm + species,
  data = penguins_bayes, family = gaussian,
  prior_intercept = normal(3000, 250^2),
  prior = normal(c(20, 0, 500), c(10, 20, 100), autoscale = TRUE),
  prior_aux = exponential(1, autoscale = TRUE),
  chains = 4, iter = 5000*2, seed = 84735)

mcmc_trace(penguin_model_1, size = 0.1)
mcmc_dens_overlay(penguin_model_1)
mcmc_acf(penguin_model_1)
pp_check(penguin_model_1, alpha = 1)
# The MCMC-simulations all have good acceptance rates and look stable.
# We see that the regression converges nicely in all chains
# and that our model captures the features nicely.

tidy(penguin_model_1, effects = c("fixed", "aux"),
     conf.int = TRUE, conf.level = 0.95)

penguins_bayes %>%
  add_epred_draws(penguin_model_1, ndraws = 50) %>%
  ggplot(aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_line(aes(y = .epred, group = paste(species, .draw)), alpha = 0.7) +
  geom_point(data = penguins_bayes, size = 1)

as.data.frame(penguin_model_1) %>%
  mutate(
    Adelie = `(Intercept)`,
    Chinstrap = `(Intercept)` + speciesChinstrap,
    Gentoo = `(Intercept)` + speciesGentoo) %>%
  mcmc_areas(pars = c("Adelie", "Chinstrap", "Gentoo")) + 
  xlab("Intercept")

# Here it is important to know that the different parameters have different interpretations
# The Intercept is as it says, the intercept of the line with the y-axis
# The flipper_length_mm parameter suggests that the penguins weight increases with ~40g/mm flipper
# The speciesChinstrap parameter says that the Chinstrap is on average 207g lighter
# The speciesGentoo parameter says that the Gentoo is on average 265g heavier

body_mass_prediction <- posterior_predict(
  penguin_model_1,
  newdata = data.frame(flipper_length_mm = c(197, 197, 197),
                       species = c('Gentoo', 'Chinstrap', 'Adelie')))

mcmc_areas(body_mass_prediction) +
  ggplot2::scale_y_discrete(labels = c("Gentoo", "Chinstrap", "Adelie")) +
  xlab("body_mass_g")
