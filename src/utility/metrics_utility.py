TOTAL_POPULATION = {
    'name': 'total_population',
    'params': {
        'drilldowns': 'State',
        'measure': 'Population'
    }
}

# Value
AVERAGE_WAGE = {
    'name': 'average_wage',
    'params': {
        'drilldowns': 'State',
        'measure': 'Average Wage'
    }
}

# Negation
POVERTY_POPULATION = {
    'name': 'poverty_population',
    'params': {
        'drilldowns': 'State',
        'measure': 'Poverty Population'
    }
}

# % of Population
EMPLOYED_POPULATION = {
    'name': 'employed_population',
    'params': {
        'drilldowns': 'State',
        'measure': 'Total Population',
        'Workforce Status': 'True'
    }
}

UNEMPLOYED_POPULATION = {
    'name': 'unemployed_population',
    'params': {
        'drilldowns': 'State',
        'measure': 'Total Population',
        'Workforce Status': 'False'
    }
}

# Negation
AGE_WORKING_PEOPLE = {
    'name': 'seniors_working_population',
    'params': {
        'drilldowns': 'State,Age',
        'measure': 'Total Population',
        'Workforce Status': 'True'
    }
}

# Negation
PATIENT_TO_PRIMARY_CARE_RATIO = {
    'name': 'parent_to_primary_card_ratio',
    'params': {
        'drilldowns': 'State',
        'measure': 'Patient to Primary Care Physician Ratio'
    }
}

# Negation
PATIENT_TO_DENTIST_RATIO = {
    'name': 'patient_to_dentist_ratio',
    'params': {
        'drilldowns': 'State',
        'measure': 'Patient to Dentist Ratio'
    }
}

# Negation
PATIENT_TO_MENTAL_HEALTH_PROVIDER_RATIO = {
    'name': 'patient_to_mental_health_provider_ratio',
    'params': {
        'drilldowns': 'State',
        'measure': 'Patient to Mental Health Provider Ratio'
    }
}

# Negation
OTHER_PRIMARY_CARE_PROVIDERS = {
    'name': 'other_primary_care_providers',
    'params': {
        'drilldowns': 'State',
        'measure': 'Other Primary Care Providers'
    }
}

# Negation
PREMATURE_DEATHS = {
    'name': 'premature_deaths',
    'params': {
        'drilldowns': 'State',
        'measure': 'Premature Death'
    }
}

# Negation
CHILD_MORTALITY = {
    'name': 'child_mortality',
    'params': {
        'drilldowns': 'State',
        'measure': 'Child Mortality'
    }
}

# Negation
POOR_OR_FAIR_HEALTH = {
    'name': 'poor_or_fair_health',
    'params': {
        'drilldowns': 'State',
        'measure': 'Poor Or Fair Health'
    }
}

# Negation
DIABETES_PREVALENCE = {
    'name': 'diabetes_prevalence',
    'params': {
        'drilldowns': 'State',
        'measure': 'Diabetes Prevalence'
    }
}

# Negation
ADULT_OBESITY = {
    'name': 'adult_obesity',
    'params': {
        'drilldowns': 'State',
        'measure': 'Adult Obesity'
    }
}

# Negation
PHYSICAL_INACTIVITY = {
    'name': 'physical_inactivity',
    'params': {
        'drilldowns': 'State',
        'measure': 'Physical Inactivity'
    }
}

# Negation
LIMITED_ACCESS_TO_HEALTHY_FOODS = {
    'name': 'limited_access_to_healthy_foods',
    'params': {
        'drilldowns': 'State',
        'measure': 'Limited Access To Healthy Foods'
    }
}

CONSIDERED_METRICS = [{'config': AVERAGE_WAGE, 'weight': 3},
                      {'config': POVERTY_POPULATION, 'weight': 4},
                      {'config': EMPLOYED_POPULATION, 'weight': 4},
                      {'config': CHILD_MORTALITY, 'weight': 2},
                      {'config': PATIENT_TO_PRIMARY_CARE_RATIO, 'weight': 1},
                      {'config': OTHER_PRIMARY_CARE_PROVIDERS, 'weight': 1},
                      {'config': PATIENT_TO_DENTIST_RATIO, 'weight': 1},
                      {'config': PATIENT_TO_MENTAL_HEALTH_PROVIDER_RATIO, 'weight': 1},
                      {'config': POOR_OR_FAIR_HEALTH, 'weight': 2},
                      {'config': PREMATURE_DEATHS, 'weight': 3},
                      {'config': ADULT_OBESITY, 'weight': 4},
                      {'config': LIMITED_ACCESS_TO_HEALTHY_FOODS, 'weight': 2},
                      {'config': PHYSICAL_INACTIVITY, 'weight': 2},
                      {'config': DIABETES_PREVALENCE, 'weight': 3}]

POPULATION_METRICS = [POVERTY_POPULATION, EMPLOYED_POPULATION]

NEGATION_METRICS = [PREMATURE_DEATHS, DIABETES_PREVALENCE, POOR_OR_FAIR_HEALTH, CHILD_MORTALITY, ADULT_OBESITY,
                    PHYSICAL_INACTIVITY, LIMITED_ACCESS_TO_HEALTHY_FOODS, OTHER_PRIMARY_CARE_PROVIDERS,
                    PATIENT_TO_MENTAL_HEALTH_PROVIDER_RATIO, PATIENT_TO_DENTIST_RATIO, PATIENT_TO_PRIMARY_CARE_RATIO,
                    POVERTY_POPULATION]
