import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Mom New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text ('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text ('🥗 kale,Spinach and Racket Smoothie')
streamlit.text ('🐔 Hard-Boiled  Free-range Egg')
streamlit.text ('🥑🍞 Avocado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
streamlit.error('Please select  a fruit to get information')
else:
#streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice")
fruityvoice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error() 
                      
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

# write your own comment -what does the next line do? 
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
#streamlit.dataframe(fruityvice_normalized)

           #allow end user to add a fruitto the list
           def insert_row_snowflake(new_fruit):
           with my_cnx.curson() as my_cur:
                      my_cur.execute("insert into fruit_load_list values('"+????+"')")
                      return "Thanks for adding " + new_fruit

            # add a button to load the fruit
                      if stramlit.button('Get The fruit list'):
                      my_cnx=snowflake.connector.connect(**
