import streamlit as st
import pickle
import numpy as np



dataset = pickle.load(open("lap_dataset1.pkl", "rb"))
pipe = pickle.load(open("lap_pipe1.pkl", "rb"))


#title
st.title("LAPTOP PRICE PREDICTOR")

#brand
company = st.selectbox ("Brand" , dataset["Company"].unique())


#type of laptop
type = st.selectbox ("Type" , dataset["TypeName"].unique())


#RAM
ram = st.selectbox( "RAM (GB)" , [2,4,6,8,12,16,24,32,64])

#weight
weight = st.number_input("Weight")


#touchscreen
touchscreen = st.selectbox("Touchscreen" , ["Yes" , "No"])


#IPS
ips = st.selectbox("IPS" , ["Yes" , "No"])

#screen size
screen_size = st.number_input("Screen size")


#resolution
resolution = st.selectbox("Screen Resolution" , ["1920x1080","1366x768",
                                                 "1600x900","3840x2160",
                                                 "3200x1800","2880x1800",
                                                 "2560x1600","2560x1440",
                                                 "2304x1440"])

#cpu brand
cpu = st.selectbox("CPU Brand" , dataset["CPU brand"].unique())

#hdd
hdd = st.selectbox("HDD (GB)" , [0,128,256,512,1024,2848])

#ssd
ssd = st.selectbox("SSB (GB)" , [0,8,128,256,512,1024])


#gpu
gpu = st.selectbox("GPU" , dataset["Gpu Brand"].unique())


#os
os = st.selectbox("OS" , dataset["OS"].unique())

if st.button("Predict Price"):
    #query


    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0


    if ips == "Yes":
        ips = 1
    else:
        ips = 0


    x_res = int(resolution.split("x")[0])
    y_res = int(resolution.split("x")[1])

    ppi = ( (x_res**2) + (y_res**2) )**0.5 / screen_size

    query = np.array([company, type,touchscreen,ips,ppi,ram,weight,cpu,hdd,ssd,gpu,os ])

    query = query.reshape (1,12)


    st.title( "Rs " + str(int(np.exp(pipe.predict(query)[0])))  + " /-")