import streamlit as st

class EnergyTracker:
    def __init__(self):
        self.appliances = {}
    def add_appliance(self,name,power_consumption,hours_per_day):
        self.appliances[name] = {"power_consumption":power_consumption,"hours_per_day":hours_per_day}

    def calculate_energy_usage(self):
        total_usage = 0
        appliance_details = {}

        for appliance,data in self.appliances.items():
            usage = data["power_consumption"]*data["hours_per_day"]
            appliance_details[appliance] = usage
            total_usage +=usage
        return appliance_details,total_usage
    
def run_energy_tracker():
    st.title("Energy Usage Tracker")

    energy_tracker = EnergyTracker()
    st.header("Add Appliance")

    with st.form(key="appliance_form"):
        appliance_name= st.text_input("Appliance Name")
        power_consumption = st.number_input("Power Consumption(km)",min_value=1)
        hours_per_day = st.number_input("Hours per day",min_value=0)
        submit_button = st.form_submit_button(label="Add Appliance")

        if submit_button:
            if appliance_name and power_consumption and hours_per_day>=0:
                energy_tracker.add_appliance(appliance_name,power_consumption,hours_per_day)
                st.success(f"Appliance{appliance_name} added")
            else:
                st.error("Please fill all details")

    st.subheader("Energy Usage Details")
    appliance_details,total_usage = energy_tracker.calculate_energy_usage()

    if appliance_details:
        for appliance,usage in appliance_details.items():
            st.write(f"{appliance}:{usage} km")
        st.write(f"Total Energy Usage:{total_usage} km")
    else:
        st.write("No appliances added yet")


if __name__ == "__main__":
    run_energy_tracker()