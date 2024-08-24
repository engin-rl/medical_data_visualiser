# Medical Data Visualizer

In this project, I visualized and made calculations from medical examination data using matplotlib, seaborn, and pandas.

_The dataset values were collected during medical examinations._

# Data description

The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices.

I used the dataset to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.


|Feature           | Variable Type         | Variable                  | Value Type                                           |
|:-----------------|:----------------------|:--------------------------|:-----------------------------------------------------|
| **Age**          | Objective Feature     | age                       | int (days)                                           |
| **Height**       | Objective Feature     | height                    | int (cm)                                             |
| **Weight**       | Objective Feature     | weight                    | float (kg)                                           |
| **Gender**       | Objective Feature     | gender                    | categorical code                                     |
| **Systolic blood pressure** | Examination Feature  | ap_hi                     | int                                                  |
| **Diastolic blood pressure** | Examination Feature  | ap_lo                     | int                                                  |
| **Cholesterol**  | Examination Feature   | cholesterol               | 1: normal, 2: above normal, 3: well above normal     |
| **Glucose**      | Examination Feature   | gluc                      | 1: normal, 2: above normal, 3: well above normal     |
| **Smoking**      | Subjective Feature    | smoke                     | binary                                               |
| **Alcohol intake** | Subjective Feature    | alco                      | binary                                               |
| **Physical activity** | Subjective Feature    | active                    | binary                                               |
| **Presence or absence of cardiovascular disease** | Target Variable | cardio | binary                                               |


# Data Preview

| cardio |   variable   | value | total |
|:------:|:------------:|:-----:|:-----:|
|   0    |    active    |   0   |  6378 |
|   0    |    active    |   1   | 28643 |
|   0    |     alco     |   0   | 33080 |
|   0    |     alco     |   1   |  1941 |
|   0    | cholesterol  |   0   | 29330 |
|   0    | cholesterol  |   1   |  5691 |
|   0    |     gluc     |   1   |  4127 |
|   0    | overweight   |   0   | 15915 |
|   0    | overweight   |   1   | 19106 |
|   0    |    smoke     |   0   | 31781 |
|   0    |    smoke     |   1   |  3240 |
|   1    |    active    |   0   |  7361 |
|   1    |    active    |   1   | 27618 |
|   1    |     alco     |   0   | 33156 |
|   1    |     alco     |   1   |  1823 |
|   1    | cholesterol  |   0   | 23055 |
|   1    | cholesterol  |   1   | 11924 |
|   1    |     gluc     |   0   | 28585 |
|   1    |     gluc     |   1   |  6394 |
|   1    | overweight   |   0   | 10539 |
|   1    | overweight   |   1   | 24440 |
|   1    |    smoke     |   0   | 32050 |
|   1    |    smoke     |   1   |  2929 |


![Figure_1](https://github.com/user-attachments/assets/1a0081f7-8df9-43b2-853c-7d2f666afc78)

![Figure_2](https://github.com/user-attachments/assets/dc7de831-f084-48b8-bedb-951b6bb8c886)

