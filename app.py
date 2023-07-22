# Import the necessary libraries
import base64
import os
import subprocess
import streamlit as st


# Define the function to create the home page
def home():
    st.set_page_config(page_title="Athletes AI", page_icon=":weight_lifter:", layout="wide")
    st.title("Athletes AI")
    st.markdown("## Welcome to Athletes AI!")
    st.markdown("Please use the navigation bar on the left to select an option.")



# Define the function to create the Diet Plan page
import streamlit as st
import subprocess


def diet_plan():
    st.title("Diet Plan")

    gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"])
    age = st.number_input("What is your age?", value=0, step=1, format="%d")
    height = st.number_input("What is your height?", value=0, step=1, format="%d")
    weight = st.number_input("What is your current weight?", value=0.0, step=0.1, format="%f")
    activity_level = st.selectbox("How active are you on an average day?", ["Light", "Moderate", "Heavy"])
    eating_preference = st.selectbox("What's your eating preference?",
                                     ["Vegetarian", "Non-Vegetarian", "Vegan", "Ovo-Vegetarian"])
    medical_history = st.multiselect("What's your medical history?",
                                     ["Bloating", "Constipation", "Diabetes", "High Cholesterol", "Hypothyroidism",
                                      "PCOS", "PCOD", "None"])

    # Calculating the BMR and Calorie Requirement based on User Inputs
    if gender == "Male":
        bmr = 88.4 + (13.4 * weight) + (4.8 * height) - (5.68 * age)
    else:
        bmr = 447.6 + (9.25 * weight) + (3.1 * height) - (4.68 * age)

    if activity_level == "Light":
        calorie_requirement = bmr * 1.375
    elif activity_level == "Moderate":
        calorie_requirement = bmr * 1.55
    else:
        calorie_requirement = bmr * 1.725

    # Calculate the number of steps required based on user input
    steps_per_day = 10000 if activity_level == "Moderate" else 15000

    # Food Recommendations
    breakfast = "Oats with milk, nuts, and fruits"
    lunch = "Brown rice, dal, vegetables, and a salad"
    snack = "Boiled eggs, fruit, and nuts"
    dinner = "Grilled chicken/fish/tofu, quinoa, vegetables, and a salad"

    if eating_preference == "Vegetarian":
        lunch = "Brown rice, dal, vegetables, and a salad with paneer/tofu"
        dinner = "Paneer/tofu, quinoa, vegetables, and a salad"

    if eating_preference == "Vegan":
        breakfast = "Oats with soy milk, nuts, and fruits"
        lunch = "Brown rice, lentils, vegetables, and a salad"
        snack = "Roasted chickpeas, fruit, and nuts"
        dinner = "Tofu, quinoa, vegetables, and a salad"

    # Displaying Recommendations
    st.write(f"You need to consume {calorie_requirement} calories each day to achieve your goals.")
    st.write(f"You should aim to take {steps_per_day} steps per day.")
    st.write("Here are some recommended meals for you:")
    st.write("Breakfast: " + breakfast)
    st.write("Lunch: " + lunch)
    st.write("Snack: " + snack)
    st.write("Dinner: " + dinner)


def workout_plan():
    st.title("Workout Plan")


        # # function to calculate workout based on user input
        # def calculate_workout(gender, height, weight, activity_level, exercise_frequency, training_level,
        #                       eating_preference,
        #                       medical_history, fitness_goal, target_weight):
        #     # add your code here to calculate the workout based on the user's input
        #     # you can use conditional statements, loops and calculations to determine the workout plan for the user
        #     # this will be specific to your expertise in the field of fitness and exercise
        #
        #     # example output
        #     pushups = 20
        #     squats = 30
        #     lunges = 15
        #     planks = 45
        #     return pushups, squats, lunges, planks
        #
        # # main function to run the workout planner
        # def main():
        #     st.title("Workout Planner")
        #
        #     # collect user input
        #     gender = st.selectbox("What is your gender?", ["Male", "Female", "Other"])
        #     height = st.number_input("What is your height? (in cm)")
        #     weight = st.number_input("What is your current weight? (in kg)")
        #     activity_level = st.selectbox("How active are you on an average day?", ["Light", "Moderate", "Heavy"])
        #     exercise_frequency = st.selectbox("How often do you exercise?",
        #                                       ["Strenuous", "Moderate", "Light", "Very light"])
        #     training_level = st.selectbox("How do you define your level of training?",
        #                                   ["Beginner", "Intermediate", "Advanced"])
        #     eating_preference = st.selectbox("What's your eating preference?",
        #                                      ["Vegetarian", "Non-vegetarian", "Vegan", "Ovo-vegetarian"])
        #     medical_history = st.multiselect("What's your medical history?", [
        #         "Bloating", "Constipation", "Diabetes", "High cholesterol", "Hypothyroidism", "PCOS", "PCOD", "None"])
        #     fitness_goal = st.selectbox("What's your current fitness goal?", ["Gain weight", "Keep fit", "Lose weight"])
        #     target_weight = st.number_input("What's your target body weight? (in kg)")
        #
        #     # calculate workout based on user input
        #     pushups, squats, lunges, planks = calculate_workout(gender, height, weight, activity_level,
        #                                                         exercise_frequency,
        #                                                         training_level, eating_preference, medical_history,
        #                                                         fitness_goal, target_weight)
        #
        #     # display workout plan to the user
        #     st.subheader("Today's Workout Plan:")
        #     st.write("Pushups:", pushups)
        #     st.write("Squats:", squats)
        #     st.write("Lunges:", lunges)
        #     st.write("Planks:", planks)
        #
        # if __name__ == "__main__":
        #     main()


# Define the function to create the Let's Workout page
def lets_workout():
    # st.title("Let's Workout")

    def pull_up(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def push_up(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def squat(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def sit_up(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def walk(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def pull_up_Demo(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def push_up_Demo(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def walk_Demo(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def main():

        menu = ["-", "pull-up", "push-up", "squat", "sit-up", "walk", "pull-up-Demo", "push-up-Demo", "walk-Demo"]
        choice = st.sidebar.selectbox("Select an option", menu)

        if choice == "-":
            st.title("Let's Goo")

        elif choice == "pull-up":
            command = ['python', 'main.py', '-t', 'pull-up']
            pull_up(command)
            stdout, stderr = pull_up(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "push-up":
            command = ['python', 'main.py', '-t', 'push-up']
            push_up(command)
            stdout, stderr = push_up(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "squat":
            command = ['python', 'main.py', '-t', 'pull-up']
            squat(command)
            stdout, stderr = squat(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "sit-up":
            command = ['python', 'main.py', '-t', 'sit-up']
            sit_up(command)
            stdout, stderr = sit_up(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "walk":
            command = ['python', 'main.py', '-t', 'walk']
            walk(command)
            stdout, stderr = walk(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "pull-up-Demo":
            command = ['python', 'main.py', '-t', 'pull-up', '-vs', 'videos/pull-up.mp4']
            pull_up_Demo(command)
            stdout, stderr = pull_up_Demo(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "push-up-Demo":
            command = ['python', 'main.py', '-t', 'pull-up', '-vs', 'videos/push-up.mp4']
            push_up_Demo(command)
            stdout, stderr = push_up_Demo(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

        elif choice == "walk-Demo":
            command = ['python', 'main.py', '-t', 'pull-up', '-vs', 'videos/walk.mp4']
            walk_Demo(command)
            stdout, stderr = walk_Demo(command)

            # Display the output
            if stderr:
                st.error(stderr)
            else:
                st.code(stdout)

    if __name__ == "__main__":
        main()


# Define the function to create the Performance Prediction page
def performance_prediction():
    st.title("Performance Analysis")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        width: 1550px;
        height: 900px;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Create the menubar
menu = [ "Diet Plan", "Workout Plan", "Let's Workout", "Performance Prediction"]
choice = st.sidebar.selectbox("Fitness Goals", menu)
# if choice == "None":
#     add_bg_from_local('./images/fp.png')
if choice == "Diet Plan":
    diet_plan()
elif choice == "Workout Plan":
    workout_plan()
elif choice == "Let's Workout":
    lets_workout()
elif choice == "Performance Prediction":
    performance_prediction()