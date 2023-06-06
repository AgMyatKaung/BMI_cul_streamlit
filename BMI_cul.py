import streamlit as st

# title 
st.title('Welcome to BMI Calculator')

# take weight input in kgs
weight = st.number_input("Enter your weight ( in kgs)")
height = st.number_input("Enter your height (in cms)")
try:
    bmi = weight / ((height / 100)**2)
except:
    st.text("Enter some value of height")

# check if button is pressed or not
if(st.button('Calculate BMI')):
    #print bmi index
    st.text("You BMI Index is {}.".format(bmi))

    # give interpreatation of bmi
    if(bmi < 16):
        st.error("You are Extremely Underweight ..... Try to eat more ")
    elif(bmi >=16 and bmi < 18.5):
        st.warning("You are Underweight .... Eat more , go to Gym and train your body  ")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy  .... Great job  .. Keep that ")
    elif(bmi >= 25 and bmi < 30):
        st.warning("You OverWeight  .... take some exercise for you good health")
    elif(bmi >= 30):
        st.error("You Extremely OverWeight !!!! ... It's important to engage in regular exercise and make it a priority. ")