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
