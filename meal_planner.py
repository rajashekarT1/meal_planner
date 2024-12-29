import streamlit as st

class MealPlanner:
    def __init__(self):
        self.meals = {}
        self.shopping_list = set()

    def add_meal(self, day, meal, ingredients):
        self.meals[day] = {"meal": meal, "ingredients": ingredients}
        self.update_shopping_list(ingredients)

    def update_shopping_list(self, ingredients):
        self.shopping_list.update(ingredients)

    def generate_shopping_list(self):
        return list(self.shopping_list)

    def display_meals(self):
        return self.meals

def meal():
    st.title("Meal Planner with Shopping List")

    meal_planner = MealPlanner()

    with st.form(key='meal_form'):
        day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        meal = st.text_input("Meal Name")
        ingredients_input = st.text_area("Ingredients")
        ingredients = ingredients_input.split(",") if ingredients_input else []
        submit_button = st.form_submit_button(label="Add Meal")

        if submit_button:
            if day and meal and ingredients:
                meal_planner.add_meal(day, meal, [i.strip() for i in ingredients])
                st.success(f"Meal added for {day}: {meal}")
            else:
                st.error("Please fill in all the details.")

    st.subheader("Meal Plan")
    meals = meal_planner.display_meals()
    if meals:
        for day, meal_info in meals.items():
            st.write(f"{day}: {meal_info['meal']}")
            st.write(f"Ingredients: {', '.join(meal_info['ingredients'])}")
    else:
        st.write("No meals added yet.")

    st.subheader("Shopping List")
    shopping_list = meal_planner.generate_shopping_list()
    if shopping_list:
        st.write(", ".join(shopping_list))
    else:
        st.write("No ingredients to buy yet.")
if __name__ == "__main__":
    meal()