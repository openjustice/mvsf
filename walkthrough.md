---
layout:     post
title:      Walkthrough
date:       2016-06-05
summary:    Walkthrough of how to create such a visualization
---

Are you interested in one of the datasets on the [OpenJustice CA portal][OJ], but you want visualize it differently from their default? This is a walkthrough of how two hackers at the [National Day of Civic Hacking][NDoCH] identified a deficiency [TKTK awkward wording] in one of the OpenJustice visualizations, and adapted a visualization of some other dataset to the OpenJustice data.

[OJ]: http://openjustice.doj.ca.gov/
[NDoCH]: https://www.eventbrite.com/e/national-day-of-civic-hacking-tickets-25188025061

This is the OpenJustice visualization that <a href="https://github.com/saikirandulla" class="github-username">@saikirandulla</a> and <a href="https://github.com/aprilw" class="github-username">@aprilw</a> were looking at:

![msdemeanor vs felony arrests by county](images/existing_chart.png)

It plots [the rates of misdemeanor vs felony arrests by county](http://openjustice.doj.ca.gov/agencies/charts), providing a notion of the spread. They wondered, how has that changed over time? Well, you can filter by year:

![msdemeanor vs felony arrests by county with years filter](images/existing_chart_years.png)

Okay...that provides the information we want, yet completely obscures the information we want. How can we see how these ratios have trended over time?

The interactive animation "The Wealth & Health of Nations" suggests one possibility: displaying on year at a time, and animating the time parameter:

[![The Wealth & Health of Nations](images/wealth_and_health_of_nations.png)](https://bost.ocks.org/mike/nations/)

## TO BE CONTINUED

This will eventually be a walkthrough of the Misdemeanors vs Felonies visualization:

![screenshot](images/screenshot.png)

It was generated from Markdown, so that's cool!
