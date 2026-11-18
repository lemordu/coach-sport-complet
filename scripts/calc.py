#!/usr/bin/env python3
"""BMR (Mifflin-St Jeor), TDEE, calories cibles et macros."""
import argparse, json

ACTIVITY = {"sedentary": 1.2, "lightly_active": 1.375, "moderately_active": 1.55, "very_active": 1.725}
GOAL = {"weight_loss": -500, "muscle_gain": 300, "maintenance": 0}

def compute(weight, height, age, gender, activity, goal):
    bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender == "male" else -161)
    tdee = bmr * ACTIVITY[activity]
    target = tdee + GOAL[goal]
    floor = max(bmr, 1500 if gender == "male" else 1200)
    capped = goal == "weight_loss" and target < floor
    if capped:
        target = floor
    protein = 2 * weight
    fat = 0.25 * target / 9
    carbs = max(0, (target - protein * 4 - fat * 9) / 4)
    return {"bmr": round(bmr), "tdee": round(tdee), "target_kcal": round(target), "capped": capped,
            "protein_g": round(protein), "fat_g": round(fat), "carbs_g": round(carbs)}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--weight", type=float, required=True)
    p.add_argument("--height", type=float, required=True)
    p.add_argument("--age", type=int, required=True)
    p.add_argument("--gender", choices=["male", "female"], required=True)
    p.add_argument("--activity", choices=ACTIVITY, required=True)
    p.add_argument("--goal", choices=GOAL, required=True)
    a = p.parse_args()
    print(json.dumps(compute(a.weight, a.height, a.age, a.gender, a.activity, a.goal), indent=2))
