Biodiversity in National Parks: Species Observations and Conservation Analysis

A. Introduction

This project investigates biodiversity data, focusing on species observations and their conservation statuses in national parks. Leveraging Python and its libraries like Pandas, Matplotlib, Seaborn, and SciPy, the analysis aims to derive insights into species distribution, observation frequency, and conservation needs across various parks.

B. Data Description

The dataset encompasses two key files:

observations.csv: Contains records of species observations in national parks, featuring the park name, species observed, and the count of observations.
species_info.csv: Provides details on each species, including its scientific name, category (e.g., Mammal, Bird), and conservation status.
Key Data Attributes:

Park Name: Identifier of the national park.
Scientific Name: The scientific designation of each species.
Common Names: Commonly used names for the species.
Observations: Count of individual species observations in the parks.
Conservation Status: Status indicating the level of endangerment (e.g., Endangered, No Concern).
The dataset presents a comprehensive view of various species, capturing a wide range of conservation statuses and observational data across different national parks.

C. Methodology

Data Cleaning
Checked for duplicates and missing values to ensure the integrity and quality of the data.
Filled missing values in 'conservation_status' with 'No Concern' for standardization.
Analytical Approach
Merged datasets for a holistic analysis.
Grouped data by relevant attributes (conservation status, park name, species category) for detailed examination.
Statistical Testing
Chi-Squared Test: Assessed the distribution uniformity of endangered species across parks.
ANOVA: Evaluated differences in observations among species categories.
Visualization
Utilized a variety of plots (bar, box, pie charts) to visualize the data, aiding in understanding species distribution, conservation status, and observation frequency.


Certainly! Below is the drafted README section D. Analysis, focusing on "Analysis by Park" based on the provided code snippets.

D. Analysis

###Analysis by Park###

The biodiversity within national parks is vast and varied. To delve into this richness, our analysis first focuses on observation counts across different parks, identifying which parks have higher instances of species observations, and thereby suggesting areas of high biodiversity and visitor interest.

![Observation Counts By Park](./Visualizations/Observation_Counts_By_Park.png)

Observation Counts by Park: We aggregated the total number of species observations for each park to determine which parks are most frequented by different species. The horizontal bar chart created from this data visually emphasizes the disparities between the parks, highlighting which parks may offer more robust habitats for wildlife or perhaps better opportunities for observation by visitors.

Most Observed Species in Each Park: By grouping the data by park and species, and summing the observations, we pinpointed the most observed species in each park. A bar chart was then used to illustrate these species, offering insights into which species might be emblematic or particularly abundant in each park. This analysis not only draws attention to these species but may also raise questions about their habitat conditions and the factors contributing to their high observation rates.

Observations per Park for Different Species Categories: A boxplot visualization was employed to display how observations are distributed among different species categories across the parks. This comparison provided a multi-faceted view of the parks' biodiversity, shedding light on the presence and visibility of various species categories such as mammals, birds, reptiles, etc., within each park.

Analysis of Endangered Species Observations in Each Park: Focusing on conservation, we analyzed the observations of endangered species, differentiating them by conservation status. The resulting bar chart serves as a stark visual reminder of the conservation challenges and efforts within these parks, indicating which parks report more frequent observations of species that are of concern, threatened, or endangered.

Statistical Analysis - Chi-Squared Test: To understand the distribution of endangered species across parks and whether certain parks are more favorable to the survival of these species, we performed a Chi-Squared test. This statistical test measured the deviation of observed frequencies of endangered species from what would be expected if the species were distributed uniformly across the parks. The test results, including the Chi-Squared statistic and the p-value, provided a quantitative measure of these distributions, potentially reflecting different levels of conservation efforts across the parks.
