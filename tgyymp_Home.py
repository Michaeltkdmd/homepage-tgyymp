import streamlit as st
from annotated_text import annotated_text
import numpy as numpy
import json
import requests
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth 
import datetime
import re
from deta import Deta

st.set_page_config(
    page_title ="TGYYMP app",
    page_icon = "hg"
)
st.title("TGYYMP")

#Removal of logo
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
#Streamlit Authenticator


#First function

#####
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

col1, col2 , col3 = st.columns(3)
col1.metric("Average Daily Vistors", "74" , "28%")
col2.metric("Active Users", "1,103" , "23%")
col3.metric("User Satisfaction", "1.5x" , "4%")

#Welcome_Url = "https://lottie.host/34e0e9b0-0690-49f9-a9ee-c9bc8348e6e1/ZxR1ZHHAZS.json"
# lottie_welcome = load_lottieurl(Welcome_Url)
# st_lottie(lottie_welcome,speed=2, reverse=False, loop=True, quality="medium", height=250, width=250,
# key=None )

Heart_Url = "https://lottie.host/7903bfb8-305c-44f9-9b43-2ba0de1897a6/UeNFDFWrkB.json"
lottie_Heart = load_lottieurl(Heart_Url)
#st_lottie(lottie_Heart, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    #key=None)

Symbol_Url = "https://lottie.host/09b8d866-34a4-4f9c-98cf-889920678ddd/w96EI5835r.json"
lottie_Symbol = load_lottieurl(Symbol_Url)

lottie_url_hello = "https://lottie.host/728462af-3e70-44b9-ac15-26da4edb9d78/zB5U2gBCXU.json"
lottie_hello = load_lottieurl(lottie_url_hello)

Camera_Url = "https://lottie.host/6c4f7a87-e6e9-483e-8510-ff62be45bf00/wAPBeI8IaE.json"
lottie_Camera = load_lottieurl(Camera_Url)

Tracker_Url = "https://lottie.host/8f47544e-b5c4-4d65-8d36-6c3d3c5688b9/nqDM9Gviwd.json"
lottie_Tracker = load_lottieurl(Tracker_Url)

##Check Us out on Youtube.
st.title("The tailored fitness logbook experience") 
st_lottie(lottie_Symbol, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None) 
st.subheader("At TGYYMP we are committed to delivering optimal user experience, so you’ll be encouraged to improve your existing training, weight loss and recovery while you develop new techniques and reach your desired goals.")
st.title("Proprietary visuals and content")
st_lottie(lottie_Camera, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None)
st.subheader("Upload content or take a snapshot of your sessions or current training program, exclusively for you to complement your growth. The body achieves what the mind believes!")
st.title("Meal planning")
st_lottie(lottie_hello, speed=2, reverse=False, loop=True, quality="high", height=150, width=150,
    key=None)
st.subheader("Find your ultimate meal prep plan using TGYYMP functionality and discover many alternatives for satisfying your needs and your goals. Manage your meals daily and weekly, stay on trend and plan ahead!")
st.title("A fitness logbook on demand")
st_lottie(lottie_Heart, speed=2, reverse=False, loop=True, quality="medium", height=150, width=150,
    key=None)
st.subheader("TGYYMP cross-section and cognitive performance should aid you too your ideal body composition.")
st.title("Track performance and statistics")
st_lottie(lottie_Tracker, speed=2, reverse=False, loop=True, quality="medium", height=100, width=100,
    key=None)
st.subheader("Documentation of performance is imperative for future growth. Stay in touch with your adequate weight composition and share your achievements on other social platforms #TGYYMP. Plus, you can edit your SMART goals performance in the ‘Gallery’ page.")
annotated_text("SOME PEOPLE ", ("WANT", "#8ef"),"IT TO HAPPEN" )
annotated_text("SOME PEOPLE ", ("WISH", "#8ef") , "IT WOULD HAPPEN.")
annotated_text("OTHERS" , ("MAKE", "#8ef") ,"IT HAPPEN.") 
DETA_KEY = "a01kqvdgtag_QfV2f8qK1HS7uBATcgV8uezx4hdgkGcV"

deta = Deta(DETA_KEY)

db = deta.Base("StreamlitAuth1")
#Signup/Login
def insert_user(email, username, password):

    """
    Inserts Users into the DB
    :param email:
    :param username:
    :param password:
    :return User Upon successful Creation:

    """
    date_joined = str(datetime.datetime.now())

    return db.put({"key": email, "username":username, "password": password, "date_joined": date_joined})

insert_user("test@outlook.com", "test1", "123456")

def fetch_users():
    """
    Fetch Users
    :return Dictionary of Users:
    """
    users = db.fetch()
    return users.items

def get_user_emails():
    """
    Fetch User Emails
    :return List of user emails:
    """
    users = db.fetch()
    emails = []
    for user in users.items:
        emails.append(user["key"])
    return emails

def get_usernames():
    """
    Fetch Usernames
    :return List of user usernames:
    """
    users = db.fetch()
    usernames = []
    for user in users.items:
        usernames.append(user["key"])
    return usernames

def validate_email(email):
    """
    Check Email Validity
    :param email:
    :return True if email is valid else False:
    """
    pattern = "^[a-zA-z0-9-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(pattern, email):
        return True
    return False

def validate_username(username):
    """
    Checks Validity of userName
    :param username:
    :return True if username is valid else False:
    """

    pattern = "^[a-zA-Z0-9]*$"
    if re.match(pattern, username):
        return True
    return False
st.title(":green[Premium] Users")
st.subheader(":green[Sign up] to have access to more TGYYMP info on:")
st.subheader("Adequate body composition, weight loss, weight gain and nutrition goals.")
def sign_up():
    with st.form(key="signup", clear_on_submit=True):
        st.subheader(":green[Sign up]")
        email = st.text_input(":blue[Email]", placeholder="Enter Your Email")
        username = st.text_input(":blue[Username]", placeholder="Enter Your Username")
        password1 = st.text_input(":blue[Password]", placeholder="Enter Your Password" , type="password")
        password2 = st.text_input(":blue[Confirm Password]", placeholder="Confirm Your password" , type="password")
        st.form_submit_button("Sign up")

        if email:
            if validate_email(email):
                if email not in get_user_emails():
                    if validate_username(username):
                        if username not in get_usernames():
                            if len(username) >=2:
                                if len(password1) >= 6:
                                    if password1 == password2:
                                        hashed_password = stauth.Hasher([password2]).generate()
                                        insert_user(email, username, hashed_password[0])
                                        st.success("Account created successfully!")
                                    else:
                                        st.warning("Password Do Not Match")
                                             
                                else:
                                    st.warning("Password is too short")
                                    
                            else:
                                st.warning("Username is too short")
                                
                        else:
                           st.warning("Username Already Exists")    

                    else:
                        ("Invaild username")
                else:
                    ("Email Already exists!")
            else:
                st.warning("Invalid Email")

                                      
sign_up()
#Login