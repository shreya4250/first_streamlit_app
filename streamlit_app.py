import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.title('My Mom New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text ('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text ('🥗 kale,Spinach and Racket Smoothie')
streamlit.text ('🐔 Hard-Boiled  Free-range Egg')
streamlit.text ('🥑🍞 Avocado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
