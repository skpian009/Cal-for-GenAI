import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-image: url('https://img.freepik.com/free-vector/calculator-concept-illustration_114360-1194.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Streamlit app title
st.title("Simple Calculator")

st.markdown("<p style='color:blue; font-size:20px;'>Created by Zubair</p>", unsafe_allow_html=True)

# Dropdown menu for selecting operation
operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Input fields for the two numbers
num1 = st.number_input("Enter first number:", step=1e-2, format="%.2f")
num2 = st.number_input("Enter second number:", step=1e-2, format="%.2f")

# Function for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Button to calculate
if st.button("Calculate"):
    # Based on the selected operation, perform calculation
    if operation == "Add":
        result = add(num1, num2)
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.success(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.success(f"Result: {num1} / {num2} = {result}")
