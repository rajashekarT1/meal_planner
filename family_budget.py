import streamlit as st


class FamilyBudget:
    def __init__(self):
        self.members = {}
        self.expenses = []

    def add_member(self, name, budget):
        self.members[name] = {"budget": budget, "expenses": 0}

    def add_expense(self, member_name, amount):
        if member_name in self.members:
            self.members[member_name]["expenses"] += amount
            self.expenses.append((member_name, amount))

    def show_balances(self):
        balances = {}
        for member, data in self.members.items():
            remaining_budget = data["budget"] - data["expenses"]
            balances[member] = remaining_budget
        return balances


def run_family_budget():
    budget_tracker = FamilyBudget()

    st.title("Family Budgeting & Expense Tracker")

    with st.form(key='member_form'):
        member_name = st.text_input("Family Member Name")
        budget_amount = st.number_input("Budget Amount", min_value=0)
        add_member_button = st.form_submit_button(label="Add Member")

        if add_member_button:
            if member_name and budget_amount > 0:
                budget_tracker.add_member(member_name, budget_amount)
                st.success(f"Member {member_name} added with a budget of {budget_amount}.")
            else:
                st.error("Please fill in all the details.")

    with st.form(key='expense_form'):
        expense_name = st.selectbox("Select Member for Expense", list(budget_tracker.members.keys()))
        expense_amount = st.number_input("Expense Amount", min_value=0)
        add_expense_button = st.form_submit_button(label="Add Expense")

        if add_expense_button:
            if expense_name and expense_amount > 0:
                budget_tracker.add_expense(expense_name, expense_amount)
                st.success(f"Expense of {expense_amount} added for {expense_name}.")
            else:
                st.error("Please fill in all the details.")

    st.subheader("Family Budget Balances")
    balances = budget_tracker.show_balances()
    if balances:
        for member, balance in balances.items():
            st.write(f"{member}: Remaining Budget: {balance}")
    else:
        st.write("No members added yet.")

if __name__ == "__main__":
    run_family_budget()
