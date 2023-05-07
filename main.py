# This is a program for beautiful interface

import streamlit as st
import pickle

# Load the trained model
pickle_in = open('Water_Quality_Prediction_System.pkl', 'rb')
model = pickle.load(pickle_in)


# define the functions to pass an inputs and make prediction
def prediction(aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper,
               bacteria, viruses, lead, nitrates, nitrites, perchlorate, radium, silver, uranium):


# Making a Prediction with new new water sample
    prediction = model.predict(
        [[aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper,
               bacteria, viruses, lead, nitrates, nitrites, perchlorate, radium,silver, uranium]])
    if prediction == 0:
        pred = 'Safe'
    else:
        pred = 'Unsafe'
    return pred


# let's create a function to define the web page
def main():
    # front end elements of the web page
    html_temp = """ 
        <div style ="background-color:blue;padding:15px"> 
        <h1 style ="color:black;text-align:center;">Automated Water Quality Prediction System</h1> 
        </div> 
        """
    st.title('Automated Water Quality Prediction System', )
    st.image("""water-testing.jpg""")


# Enter all the parameters of water
    st.header('Enter the characteristics of the water:')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        aluminium = st.number_input('aluminium:', min_value=0.0, max_value=5.05, value=0.5)
        ammonia = st.number_input('ammonia:', min_value=0.0, max_value=30.0, value=0.5)
        arsenic = st.number_input('arsenic:', min_value=0.0, max_value=1.05, value=0.5)
        lead = st.number_input('lead:', min_value=0.0, max_value=0.8, value=0.5)
        nitrates = st.number_input('nitrates:', min_value=0.0, max_value=20.0, value=0.5)

    with col2:
        barium = st.number_input('barium:', min_value=0.0, max_value=5.0, value=0.5)
        cadmium = st.number_input('cadmium:', min_value=0.0, max_value=0.9, value=0.5)
        chloramine = st.number_input('chloramine:', min_value=0.0, max_value=9.0, value=0.5)
        nitrites = st.number_input('nitrites:', min_value=0.0, max_value=3.0, value=0.5)
        perchlorate = st.number_input('perchlorate:', min_value=0.1, max_value=60.0, value=0.5)

    with col3:
        chromium = st.number_input('chromium:', min_value=0.0, max_value=1.0, value=0.5)
        copper = st.number_input('copper:', min_value=0.0, max_value=2.0, value=0.5)
        bacteria = st.number_input('bacteria:', min_value=0.0, max_value=1.0, value=0.5)
        radium = st.number_input('radium:', min_value=0.0, max_value=8.0, value=0.5)
        silver = st.number_input('silver:', min_value=0.0, max_value=0.5, value=0.5)

    with col4:
        viruses = st.number_input('viruses:', min_value=0.0, max_value=1.0, value=0.5)
        uranium = st.number_input('uranium:', min_value=0.0, max_value=1.0, value=0.5)

    result = " "
    if st.button("Predict Quality of water"):
        result = prediction(aluminium, ammonia, arsenic, barium, cadmium, chloramine, chromium, copper,
               bacteria, viruses, lead, nitrates, nitrites, perchlorate, radium, silver, uranium)
        st.success("Status of new water sample is: {}".format(result))


if __name__=='__main__':
    main()
