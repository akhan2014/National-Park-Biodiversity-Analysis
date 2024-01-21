# Biodiversity In National Parks Analysis Script
# This script performs an exploratory data analysis on biodiversity data
# focusing on species observations and their conservation statuses.


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, chi2_contingency


# Load the datasets
# The 'observations.csv' contains observation records of species,
# while 'species_info.csv' includes species classification and conservation status.
observations_df = pd.read_csv('observations.csv')
species_df = pd.read_csv('species_info.csv')


# Merge DataFrames on 'scientific_name':
# This combines the observations with species details for a comprehensive dataset.
# 'left' join ensures all records from 'observations_df' are included in the merged dataset.

df = pd.merge(observations_df, species_df, on='scientific_name', how='left')

# Display basic information and first few rows of the dataset
# Helpful to understand the dataset structure and types of data stored.
print(df.info())
print(df.head())


# Data Cleaning Section
# ----------------------

# Identify duplicates and missing values:
# .duplicated().sum() returns the count of duplicate rows.
# .isnull().sum() provides a count of missing values in each column.
print('Number of Duplicated Rows:', df.duplicated().sum())
print('Missing Value Count:', df.isnull().sum())


# Delete duplicated rows from the combined dataframe to prevent skewed analysis
df = df.drop_duplicates()


# Handle missing values in 'conservation_status':
# Missing values are filled with 'No Concern', assuming absence of data means no conservation concern.
# This standardizes the data for consistent analysis.

df['conservation_status'] = df['conservation_status'].fillna('No Concern')


# Data Analysis and Visualization Section
# ----------------------


# Rechecking the cleaned data set structure:
# After data cleaning, it's good practice to recheck the structure of the data.
print(df.info())


# Display statistical summary of the dataset:
# .describe() provides a statistical summary of numerical columns, useful for initial data understanding.
print(df.describe())


# Analysis of Endangered Species Observations in Each Park:
# This visualization helps identify which parks have the most observations of endangered species.
# 'endangered_species' is a filtered DataFrame containing only records where species are not of 'No Concern'.
endangered_species = df[df['conservation_status'] != 'No Concern']

# Using seaborn's barplot to compare observations across different parks, categorized by conservation status.
plt.figure(figsize=(12, 6))
sns.barplot(data=endangered_species, x='park_name', y='observations', hue='conservation_status')
plt.title('Endangered Species Observations in Each Park')
plt.xlabel('Park Name')
plt.ylabel('Observations')
plt.legend(title='Conservation Status')
plt.tight_layout()
plt.show()


# Observations per Park for Different Species Categories:
# This visualization reveals how observations are distributed across parks and species categories.

# A boxplot is used for its ability to show distributions with respect to categories.
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='park_name', y='observations', hue='category', palette='Set2')
plt.title('Observations per Park for Different Species Categories')
plt.xlabel('Park Name')
plt.ylabel('Observations')
plt.legend(title='Category')
plt.tight_layout()
plt.show()


# Most Observed Species in Each Park:
# Identifying and visualizing the most observed species in each park.

# 'groupby' is used to group data by 'park_name' and 'scientific_name', then 'sum' the observations.
# 'idxmax' is used to find the index of the max observation for each park.
top_species_per_park = df.groupby(['park_name', 'scientific_name'])['observations'].sum().reset_index()
top_species_per_park = top_species_per_park.loc[top_species_per_park.groupby('park_name')['observations'].idxmax()]

# Bar plot visualization for the most observed species in each park.
plt.figure(figsize=(12, 6))
sns.barplot(x='park_name', y='observations', data=top_species_per_park, hue='scientific_name')
plt.title('Most Observed Species in Each Park')
plt.xlabel('Park Name')
plt.ylabel('Observations')
plt.xticks(rotation=45)
plt.legend(title='Scientific Name', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# Observation Counts by Park:
# Comparing total observations across different parks to identify which park has the most observations.

# 'groupby' is used to group data by 'park_name', and 'sum' is used to aggregate observations.
observation_counts_by_park = observations_df.groupby('park_name')['observations'].sum()

plt.figure(figsize=(10, 6))
observation_counts_by_park.plot(kind='barh')
plt.title('Observation Counts by Park')
plt.xlabel('Total Observations')
plt.ylabel('Park Name')
plt.show()


# Creating a contingency table of the counts of each endangered species in each park
# This table forms the basis for the Chi-Squared test.
contingency_table = pd.crosstab(endangered_species_parks['park_name'], endangered_species_parks['scientific_name'])

# Performing the Chi-Squared test
# This test helps us understand if the distribution of endangered species across parks is uniform or shows significant differences.
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Printing the results of the Chi-Squared test
print("\nChi-Squared Test Results for Endangered Species Distribution Across Parks:")
print("Chi-Squared Statistic:", chi2, "P-Value:", p)

# Interpreting the results:
# - The Chi-Squared statistic measures how much the observed frequencies deviate from the expected frequencies.
# - The p-value tells us whether the deviations are statistically significant.
# If the p-value is low (commonly <0.05), we can conclude that the distribution of endangered species across parks is not random.
# This could indicate that certain parks are more favorable to the survival of these species, or it could reflect different levels of conservation efforts across the parks.


# Species distribution across different categories
# This bar plot shows how many species fall into each category (e.g., Mammal, Bird, etc.).
# It provides an overview of the biodiversity in the dataset.

category_counts = species_df['category'].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title('Distribution of Species Across Categories')
plt.xlabel('Category')
plt.ylabel('Number of Species')
plt.xticks(rotation=45)
plt.show()


# Distribution of observations by species category
# This boxplot visualizes the spread and distribution of observations for each species category.
# It's useful for identifying categories with more frequent observations, which might indicate higher abundance or easier detectability.

plt.figure(figsize=(12, 8))
sns.boxplot(x='category', y='observations', data=df)
plt.title('Distribution of Observations by Species Category')
plt.xlabel('Species Category')
plt.ylabel('Number of Observations')
plt.xticks(rotation=45)
plt.show()

# ANOVA test for differences in observations among categories
# This statistical test checks if there are significant differences in the mean number of observations across different species categories.
# A low p-value would indicate that at least one category has a significantly different number of observations.

# Grouping the data by 'category' and calculating the mean number of observations for each category.
category_observations = df.groupby('category')['observations'].mean()

# Conducting the ANOVA test.
# The f_oneway function from scipy.stats is used for the ANOVA test.
# It compares the means of observations for each category to determine if they are statistically significantly different.
f_stat, p_value = f_oneway(*[df[df['category'] == category]['observations'] for category in category_observations.index])

# Printing the ANOVA test results.
print("ANOVA Test Results for Differences in Observations Among Categories:")
print("F-Statistic:", f_stat, "P-Value:", p_value)

# Interpreting the ANOVA test results:
# - The F-Statistic measures the ratio of variance between the groups (categories) to the variance within the groups.
# - A higher F-Statistic value indicates a greater difference between the group means.
# - The p-value assesses the probability of observing the data, assuming the null hypothesis is true (no difference in group means).
# - A low p-value (commonly <0.05) suggests that we can reject the null hypothesis, meaning there are statistically significant differences in the observations among different categories.
# - In this case, with a p-value of 0.01079, we conclude that there is a significant difference in the mean number of observations among different species categories. This may warrant further investigation into why certain categories have more or fewer observations.


# Species count by conservation status
# This bar chart shows the number of species associated with each conservation status.
# It helps in understanding the distribution of conservation needs among species.

species_count_by_status = species_df['conservation_status'].value_counts()

plt.figure(figsize=(10, 6))
species_count_by_status.plot(kind='bar')
plt.title('Species Count by Conservation Status')
plt.xlabel('Conservation Status')
plt.ylabel('Number of Species')
plt.xticks(rotation=45)
plt.show()


# Proportions of species in each conservation status
# This pie chart visually represents the proportions of different conservation statuses in the dataset.
# It provides a clear view of how many species are in each status category relative to the total.

conservation_df = species_df[species_df['conservation_status'].notna()]
status_proportions = conservation_df['conservation_status'].value_counts(normalize=True)

plt.figure(figsize=(8, 8))
status_proportions.plot(
    kind='pie', 
    autopct='%1.1f%%', 
    startangle=90,
    colors=['blue', 'orange', 'green', 'red'],
    explode=(0.1, 0.1, 0.1, 0.1),
    shadow=True
)
plt.title('Proportions of Conservation Statuses')
plt.ylabel('')
plt.show()

# Top 10 most observed species overall
# This bar plot ranks the top 10 species based on total observations across all parks.
# It helps identify which species are most frequently observed, potentially indicating abundance or wide distribution.

top_species = df.groupby('common_names')['observations'].sum().nlargest(10)

plt.figure(figsize=(10, 6))
top_species.plot(kind='barh')
plt.title('Top 10 Most Observed Species Overall')
plt.xlabel('Total Observations')
plt.ylabel('Common Name')
plt.show()

# Filtering for 'Endangered' species
endangered_species = species_df[species_df['conservation_status'] == 'Endangered']

# Merging with the observations data
endangered_species_observations = pd.merge(endangered_species, observations_df, on='scientific_name')

# Summing observations for each endangered species
summed_observations = endangered_species_observations.groupby('scientific_name')['observations'].sum().reset_index()

# Sorting and selecting the top 10 most observed endangered species
top_10_endangered = summed_observations.sort_values('observations', ascending=False).head(10)

# Visualization: Simplified Bar plot for the top 10 most observed endangered species
plt.figure(figsize=(10, 6))
sns.barplot(x='observations', y='scientific_name', data=top_10_endangered)
plt.title('Top 10 Most Observed Endangered Species')
plt.xlabel('Total Observations')
plt.ylabel('Scientific Name')
plt.tight_layout()
plt.show()


# 5 rarest endangered species
# This plot shows the five endangered species with the least number of observations.
# These species could be at higher risk and might need more focused conservation efforts.

rarest_endangered = summed_observations.sort_values('observations', ascending=True).head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x='observations', y='scientific_name', data=rarest_endangered)
plt.title('5 Rarest Endangered Species Across Parks')
plt.xlabel('Total Observations')
plt.ylabel('Scientific Name')
plt.tight_layout()
plt.show()


# Findings and Interpretations:
# -----------------------------
# 1. Certain parks are more significant in terms of observations of endangered species, suggesting targeted conservation efforts.
# 2. The diversity and distribution of species across categories and conservation statuses provide insights into biodiversity and conservation needs.
# 3. The ANOVA test results indicate if different species categories have significantly different observation counts, guiding further ecological studies.
# 4. The analysis of the most and least observed species, especially endangered ones, highlights areas of concern and potential conservation priorities.

