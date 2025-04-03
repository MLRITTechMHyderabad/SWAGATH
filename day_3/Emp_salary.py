employee = [
    {"name": "SWAGATH", "salary": 50000, "rating": 5},
    {"name": "Goutham", "salary": 40000, "rating": 5},
    {"name": "ASHA", "salary": 35000, "rating": 4},
    {"name": "pravalika", "salary": 35000, "rating":4 }
]

print(employee)

adding_salary = lambda emp: {
    "name": emp["name"],
    "salary": round(emp["salary"] * (1.10 if emp["rating"] in [4,5] else 1.05 if emp["rating"] == 3 else 0.97), 2),
    "rating": emp["rating"]
}

updated_salary = list(map(adding_salary, employee))

print("\n",updated_salary)

