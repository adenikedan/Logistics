# import module
import streamlit as st
import datetime

from PIL import Image

#Import Image from pillow to open images
from PIL import Image
img = Image.open("LogisticsImage.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=600)

# Add Title

st.title("Welcome to Nikesworld Logistics")

# markdown
st.markdown('### We are here to serve you better')
 
# text
st.text("Kindly provide your details:")


#pickup
Pickup_date = st.date_input("Please select Pickup date", min_value=datetime.date(1921, 1, 1),
                            max_value=datetime.date(2030, 12, 31))
    
  
 #Form
with st.form(key='form1', clear_on_submit=True):
    Address =  st.text_area("Enter the pickup Address :")
    Address2 = st.text_area("Enter the delivery address")
    firstname= st.text_input("Enter your First Name:")
    Lastname=  st.text_input("Enter your Last Name:")
    Emailaddress = st.text_input("Enter your Email Address:")
    Mobileno= st.text_input("Enter your Mobile number")
   
   
                                                     
#RadioButton
# Select male if clicked else Female
    gender = st.radio("Select Gender: ",("Male", " Female"))
    
        
#Radio
    Referral= st.radio("How did you hear about our services:",('Friends', 'Family','Social Media','Word of Mouth','Others')) 
    
#Selectbox indicating goods to be delivered to the recipient
    goods= st.selectbox("Please select the type of goods:", ['perishable goods', 'clothings','inflamatory goods' ,'Others'])
    

    
# To display customer details when submit button is cliked.        
    submit_button = st.form_submit_button("submit")
    st.write("Pickup Address is :" + " " + Address)
    st.write("Delivery Address is :" + " " + Address2)
    st.write("FirstName :" +" "+ firstname)
    st.write("LastName :" +" "+ Lastname)
    st.write("Email Address :" +" "+ Emailaddress)
    st.write("MObile no:" +" "+str(Mobileno))
    st.write("Gender :" +" "+ gender)
    st.write("Referral:" +" "+ Referral)
    st.write("Goods to be delivered :", goods)
    
    
        
#This will indicate location price based on the location indicated by customer.  
location = st.radio('Your form has been submitted:Please select your delivery location to obtain your fee ',('Mainland', 'Island', 'Outside                      Lagos'))

    
# compare location value
if(location == 'Mainland'):
    amount = st.text('Your delivery amount is: N1500')
elif(location == 'Island'):
    amount = st.text('Your delivery amount is: N2000')
else:
    amount = st.text('Your delivery amount is :N3000') 
    
# To upload receipt in jpg', 'png','JPEG','pdf','docx' formats 
image = st.file_uploader(" Kindly make payment and upload receipt", type=['jpg', 'png','JPEG','pdf','docx'])

st.write( "Thank you for choosing us")


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)