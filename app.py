import streamlit as st
st.markdown(
    
    <style>
    body {
        background-image: url('https://www.istockphoto.com/photo/2024-on-the-calculator-screen-new-year-2024-on-the-calculator-display-with-copy-space-gm1781688768-546899513?utm_source=pixabay&utm_medium=affiliate&utm_campaign=SRP_image_sponsored&utm_content=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fcalculator%2F&utm_term=calculator');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    ,
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
