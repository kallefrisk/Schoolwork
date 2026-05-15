# Load packages
library(bayesrules)
library(rstanarm)
library(bayesplot)
library(tidyverse)
library(tidybayes)
library(broom.mixed)

data(bald_eagles)
eagles <- bald_eagles

head(eagles)

eagles$count %>%
  hist(main = "Eagle Sightings",
       xlab = "count",
       breaks = seq(min(eagles$count) - 0.5,
                    max(eagles$count) + 0.5,
                    by = 1))

# It looks like we have a very skewed dataset looking at the amount of no-sightings
# and the smaller number of many sightings.

eagles %>%
  ggplot(aes(x = year, y = count)) +
  geom_col()

# Here we see a trend in the data of looking like an exponential function as well
# as the variance of the data seemingly increasing with the year

eagles %>%
  mutate(hours_bin = cut(hours,
                         breaks = c(130, 150, 170, 190, 210, 230, 250),
                         include.lowest = TRUE)) %>%
  ggplot(aes(x = year, y = count, fill = hours_bin)) +
  geom_col(alpha = 0.7)

# Here it looks like the hours spent observing have increased over the years.

