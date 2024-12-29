import streamlit as st

class WeatherOutfitPlanner:
    def __init__(self):
        self.weather_conditions ={
            "sunny":"T-shirt and shorts",
            "rainy":"Raincoat and boots",
            "cold":"jacket and scarf"
        }
    def suggest_outfit(self,weather):
        return self.weather_conditions.get(weather.lower(),"check the weather forecast")
def app():
    st.title("Weather-Based outfit Planner")

    outfit_planner = WeatherOutfitPlanner()

    with st.form(key='outfit_form'):
        weather_today = st.selectbox("Enter Weather Condition",["Sunny","Rainy","Cold"])
        submit_button = st.form_submit_button(label="Get Suggested Outfit")

        if submit_button:
            if weather_today:
                suggested_outfit = outfit_planner.suggest_outfit(weather_today)
                st.success(f"Suggested Outfit for {weather_today}:{suggested_outfit}")
            else:
                st.error("Please fill details")
if __name__ == "__main__":
    app()
