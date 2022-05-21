import streamlit as st
import random


solutions = ('helicopter',
             'generator',
             'television',)
guide = ('-a flying object',
         '-produces electricity',
         '-transmits audio-visual content')
congrats = ('You are correct!',
            'Nice! You got it!',
            'You are smart!',
            'Good Job!')
questions = ('ehlretpocii',
             'grotarene',
             'tnoeisivel')

        
st.sidebar.write("## Anagram Game")

choice = st.sidebar.radio("Do you wanna play?", options = ['Yes','No'])
if choice == 'Yes':
            valid = False
            length = len(solutions) - 1
            length1 = len(congrats) - 1
            selection = st.selectbox("Choose an Anagram to decode:", questions)
            with st.form(key = 'my_form'):
                answer = st.text_input("Your Answer: ")
                if st.form_submit_button('Submit'):
                    if selection == questions[0] and  solutions[0] == answer:
                        valid = True

                    elif selection == questions[1] and solutions[1] == answer:
                        valid = True
                        
                    elif selection == questions[2] and solutions[2] == answer:
                        valid = True
                        
                    if valid:
                        st.success(congrats[random.randint(0,length1)])
                    else:
                        st.error("You're not correct! Try again")



                
                    
            
elif choice == 'No':
            st.sidebar. success('Goodbye !')
            

