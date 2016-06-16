# Misdemeanors vs. Felonies Visualization

## Summary

County felony and misdemeanor arrest rates are shown relative to California's average rates, both for the total population and disaggregated by race/ethnicity. Counties with higher-than-average misdemeanor rates tend to also have higher-than-average felony rates. The misdemeanor arrest rate for Blacks is 2.5 times higher than the state average and the felony arrest is 3.5 times higher. Hispanics are just slightly above the average rate for both. Whites are just below average and Asians/Pacific Islanders are notably lower. Arrest rates for Blacks across counties has a larger range of deviation from the state average compared to the distribution for other races/ethnicities.

## Setup

1. Clone the repo
2. Start up a server, e.g. `python3 -m http.server`
3. Open up the page in the browser, e.g. `http://0.0.0.0:8000/`


## Next Steps

1. Add race dimension to the visualization
  - Currently, the visualization only shows "All Combined" for race
  - New csv in data folder (new_data.csv) includes a race field
    1. This may require a change to the scripts/data_converter.py file to get the race into  the json file the visualization reads from. Unless there is another trick!
  - Possible ideas:
    1. Color by race: (Downside here is it gets rid of coloring by county)
    ![Race breakdown](http://i.imgur.com/YwRBfWe.png)
    2. Include race filters:
    ![Race Filter](http://i.imgur.com/UVQoQQk.gif)
1. Add county filter to visualization
  - Similar to race filter, but for counties
  - Map of California counties filter (may be too small to be useful)
1. Improve tooltip
  - Tooltip only includes county name
  - Make a tooltip which includes felony, misdemeanor, total arrests, arrests per 100K, population: (example)
  ![Tooltip](http://i.imgur.com/UEAKwmB.png)

These improvements are geared to make our new d3 visualization encompass all the functionality of our old highcharts visualizations as seen at the [open justice website](http://openjustice.doj.ca.gov/agencies/charts). These have year, county and race filters.

