import streamlit as st

def feet_inch_to_cm(feet, inches):
    total_inches = feet * 12 + inches
    cm = total_inches * 2.54
    return cm

def lb_to_kg(pounds):
    kg = pounds * 0.45359237
    return kg

# Streamlit app
st.header("Welcome to BMI Calculator "\
         "And Unit Converter")

st.subheader("BMI Calculator")

# take weight input in kgs
weight = st.number_input("Enter your weight (in kgs)")
height = st.number_input("Enter your height (in cms)")
try:
    bmi = weight / ((height / 100)**2)
except:
    st.text("")

# check if button is pressed or not
if st.button('Calculate BMI'):
    # print bmi index
    st.text("Your BMI Index is {}.".format(bmi))

    # give interpretation of bmi
    if bmi < 16:
        st.error("You are Extremely Underweight ..... Try to eat more")
    elif 16 <= bmi < 18.5:
        st.warning("You are Underweight .... Eat more, go to the Gym and train your body")
    elif 18.5 <= bmi < 25:
        st.success("You are Healthy  .... Great job  .. Keep it up")
    elif 25 <= bmi < 30:
        st.warning("You are Overweight  .... Take some exercise for your good health")
    elif bmi >= 30:
        st.error("You are Extremely Overweight !!!! ... It's important to engage in regular exercise and make it a priority.")

# Toggle button to show/hide the unit converter section
show_unit_converter = st.checkbox("Show Unit Converter ( From Feet,inch to cm & lb to kg )")

if show_unit_converter:
    st.subheader("Unit Converter")
    
    with st.form("unit_conversion_form"):
        # Feet and Inches to Centimeters
        feet = st.number_input("Feet")
        inches = st.number_input("Inches")
        
        # Pounds to Kilograms
        pounds = st.number_input("Pounds")
        
        convert_button = st.form_submit_button("Convert")
        
        if convert_button:
            cm = feet_inch_to_cm(feet, inches)
            kg = lb_to_kg(pounds)
            st.write(f"{feet} feet and {inches} inches = {cm} centimeters")
            st.write(f"{pounds} pounds = {kg} kilograms")
