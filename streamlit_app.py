import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Hello this is first streamlit app')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)



# streamlit.text(fruityvice_response.json())

# fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
# streamlit.write('The user entered ', fruit_choice)


# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)



# write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)




# def get_fruityvice_data(this_fruit_choice):
#   fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
#   fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#   return fruityvice_normalized
  
# streamlit.header("Fruityvice Fruit Advice!")  
# try:
#   fruit_choice= streamlit.text_input('What fruit would you like information about?')
#   if not fruit_choice:
#     streamlit.error("please select fruit to get information")
#   else:
#     # fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#     # fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#     # streamlit.dataframe(fruityvice_normalized)
#     back_from_function=get_fruityvice_data(fruit_choice)
#     streamlit.dataframe(back_from_function)
# except URLError as e:
#   streamlit.error()

streamlit.text('The fruit load list contains:')
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list (fruit_name) values(%s)",(new_fruit,))
    return "thanks for adding "+new_fruit

add_my_fruit=streamlit.text_input('what fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)


                            
streamlit.stop()

# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my_cur.fetchone()
# streamlit.text("Fruit load list contains")
# streamlit.text(my_data_row)

#streamlit.text(my_data_row)
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)
#streamlit.text("Hello from Snowflake:")


  
streamlit.write('Thankyou for adding',add_fruit)

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values('from streamlit')") 
