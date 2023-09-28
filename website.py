# import module
import streamlit as st

# Title
st.title("Hi!")

st.subheader("Welcome to the ideas generator!")

if st.checkbox("The blog."):
    st.write("A lot of people in the world are suffring from creative block. So, we dicided to interveiw our friend chunny who had creative block, to see his experience.")
    st.write('After the interveiw, chunny told us creative block really sucks."It really sucks." Says chunny. "Its like you cant think of anything. Your brain is basicaly dead."')
    st.write('Luckely for chunny, we made this website to help him. "Its great!" he says "I can think again!"')
topic = None
topic = st.selectbox("Please select one topic to generate ideas on:",
    ['Painting', 'Music' , 'Sculptures', 'Nonfiction', 'Fiction', 'Videos'])

if(st.button("Submit")):
    st.subheader("Here's some ideas:")
    if(topic == "Painting"):
        st.write("Nature")
        st.write("Self portrate")
        st.write("Man made things")
    elif(topic == "Music"):
        st.write("Classical")
        st.write("Fast and hard")
        st.write("Slow and calming")
    elif(topic == "Sculptures"):
        st.write("Nature")
        st.write("Humans")
        st.write("Objects")
    elif(topic == "Nonfiction"):
        st.write("Living things")
        st.write("How machines work")
        st.write("The history of ___")
    elif(topic == "Fiction"):
        st.write("Survival")
        st.write("Adventure")
        st.write("Sorry")
    else:
        st.write("Video games")
        st.write("Busting myths")
        st.write("Try not too laugh")
    st.write("For more ideas, please search", topic, "on google.")
    st.subheader("Don't worry if your topic isn't perfect. Just try your best.")
st.header("How to come up with your own ideas:")
st.write("Step one: Think about what your latest peices are. What do you like?")
st.write("Step two: Write the things down.")
st.write("Step three: Make a picture related to the word.")