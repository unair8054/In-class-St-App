import streamlit as st
from PIL import Image

st.snow ()
st.title("Utkarsh Nair")
st.subheader ("It is, what it is")

Col1,Col2 = st.columns ([3,1])

with Col1:
    st.subheader ("About Me")
    st.text ("I wish knew that answer")

#sidebar w/Download 

st.sidebar.caption('In case you chill and discuss about Formula 1?')
st.sidebar.write('pqrs@xyz.com')

#rb means converting psf file to raw binary format

pdf_file = open ('Final Project Guideline Document.pdf','rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='Final Project Guideline Document.pdf',mime='pdf')
image = Image.open("Room .jpeg")
st.image (image, width = 250)

#Projects - to be added. 

#st.subheader("Projects")
#titanic_data = pd.read_csv('titanic.csv')
#interval = alt.selection_interval()
#bar_chart = alt.Chart(titanic_data).mark_bar().encode(
 #   x = 'sum(Survived):Q',
  #  y = 'Pclass:N',
   # color = 'Pclass:N',
#).properties(
 #   width = 300
#)
#scatter_plot = alt.Chart(titanic_data).mark_point().encode(
 #   x = 'Age:Q',
  #  y = 'Fare:Q',
   # color = alt.condition(interval, 'Sex', alt.value('lightgray')),
#).properties(
 #   width = 500,
  #  height = 400
#).add_selection(
 #   interval
#).interactive()
# Define a selection to filter the scatter plot based on the selected passenger 
#selection = alt.selection_single(fields=['Pclass'], empty = 'none')
#bar_chart = bar_chart.add_selection(selection)
#scatter_plot = scatter_plot.transform_filter(selection)
#put any jupiter chart in streamlit just add st.altair_chart()
#st.altair_chart(bar_chart | scatter_plot)


# Skills Section - IN the form of Bar Chart 

#skill_data = pd.DataFrame(
 #   {
  #      "Skills Level" : [90,60,60,40],
   #     "Skills": ["Python", "Tableau", "mySQl", "RStudio"]
    #}
#)

#skill_data = skill_data.set_index ("Skills")
#with st.container():
 #   st.subheader ("Skills")
  #  st.bar_chart(skill_data)
#with    st.expander("See More Skills"):
 #   st.write("I have lots of more sjills too such as ....")

#Add a map
#Create a datafram with latitude and longitude 

tab_skills,tab_exp,tab_pro,tab_con,tab_pic = st.tabs(['Skills', 'Experience', 'Projects', 'Contact Me', "Take a Picture"])



picture = st.camera_input("Take a picture with me")
if picture:
    st.image(picture)
