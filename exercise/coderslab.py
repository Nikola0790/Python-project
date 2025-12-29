def coderslab_welcome():
    print('Welcome !!!')

# EXERCISE FOOD

from typing import List, Tuple


class Ingredient:
    def __init__(
        self,
        name: str,
        protein_per_100g: int | float,
        carbs_per_100g: int | float,
        fats_per_100g: int | float,
    ):
        self.name = name
        self.protein = protein_per_100g
        self.carbs = carbs_per_100g
        self.fats = fats_per_100g

    def values_for_amount(self, grams: int | float) -> tuple[float, float, float, float]:
        factor = grams / 100
        protein = self.protein * factor
        carbs = self.carbs * factor
        fats = self.fats * factor
        kcal = protein * 4 + carbs * 4 + fats * 9.4
        return protein, carbs, fats, kcal


class Meal:
    def __init__(self, name: str):
        self.name = name
        self.ingredients: List[Tuple[Ingredient, float]] = []

    def add_ingredient(self, ingredient: Ingredient, grams: int | float) -> None:
        self.ingredients.append((ingredient, grams))

    def summary(self) -> tuple[str, float, float, float, float]:
        lines = [f"Meal: {self.name}"]
        total_p = total_c = total_f = total_kcal = 0.0

        for ingredient, grams in self.ingredients:
            p, c, f, kcal = ingredient.values_for_amount(grams)
            total_p += p
            total_c += c
            total_f += f
            total_kcal += kcal

            lines.append(
                f"- {grams}g {ingredient.name} "
                f"({p:.2f}g protein, {c:.2f}g carbohydrates, "
                f"{f:.2f}g fats, {kcal:.1f} kcal)"
            )

        lines.append(
            f"Total: {total_p:.2f}g protein, {total_c:.2f}g carbohydrates, "
            f"{total_f:.2f}g fats, {total_kcal:.1f} kcal"
        )

        return "\n".join(lines), total_p, total_c, total_f, total_kcal


class DailyPlan:
    def __init__(self, name: str):
        self.name = name
        self.meals: List[Meal] = []

    def add_meal(self, meal: Meal) -> None:
        self.meals.append(meal)

    def print_summary(self) -> None:
        print(self.name)
        print()

        total_p = total_c = total_f = total_kcal = 0.0

        for meal in self.meals:
            text, p, c, f, kcal = meal.summary()
            print(text)
            print()

            total_p += p
            total_c += c
            total_f += f
            total_kcal += kcal

        print(
            f"TOTAL: {total_p:.2f}g protein, {total_c:.2f}g carbohydrates, "
            f"{total_f:.2f}g fats, {total_kcal:.0f} kcal"
        )

egg = Ingredient("Egg", 13, 1.1, 11)
tomato = Ingredient("Tomato", 0.9, 3.9, 0.2)
bread = Ingredient("Bread", 9, 49, 3.2)

scrambled_eggs = Meal("Scrambled Eggs")
scrambled_eggs.add_ingredient(egg, 200)
scrambled_eggs.add_ingredient(tomato, 50)

sandwich = Meal("Sandwich")
sandwich.add_ingredient(bread, 25)
sandwich.add_ingredient(tomato, 50)

plan = DailyPlan("Minimal")
plan.add_meal(scrambled_eggs)
plan.add_meal(sandwich)

plan.print_summary()


#EXERCISE STUDENT

import csv
class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                if class_name is None or class_name == row[2]:
                    students.append(
                        cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                    )
        print(students)
        return students


Student.from_file('students.csv')  # ALL students
Student.from_file('students.csv', '2C')  # Only those in 2C class

