import pandas as pd

# Assuming you have a DataFrame called 'df' with 'ship_mode', 'sales', and 'profit' columns
df['surcharge'] = df['ship_mode'].map({
    "Same Day": 0.2,
    "First Class": 0.1,
    "Standard Class": 0.05
}).fillna(0)

df['total_cost'] = (df['sales'] - df['profit']) * (1 + df['surcharge'])


SELECT *,
    CASE
        WHEN ship_mode = 'Same Day' THEN 0.2
        WHEN ship_mode = 'First Class' THEN 0.1
        WHEN ship_mode = 'Standard Class' THEN 0.05
        ELSE 0
    END AS surcharge,
    (sales - profit) * (1 + 
        CASE
            WHEN ship_mode = 'Same Day' THEN 0.2
            WHEN ship_mode = 'First Class' THEN 0.1
            WHEN ship_mode = 'Standard Class' THEN 0.05
            ELSE 0
        END) AS total_cost
FROM your_table;