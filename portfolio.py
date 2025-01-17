import streamlit as st
st.set_page_config(page_title="Abhinav Singh's Portfolio", layout="wide")
st.title("Abhinav Singh's Portfolio")
st.markdown("""
    <style>
        .intro {
            font-size: 20px;
            color: #4B0082;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .strip {
            height: 5px;
            background-color: #FF6347; 
            margin: 20px 0;
        }
        .section-header {
            color: #6A5ACD;
            border-bottom: 2px solid #FF6347; 
            padding-bottom: 5px;
        }
    </style>
    <div class="intro">
        Hello! I'm Abhinav Singh, a Full Stack Development student at UPES, Dehradun, India. 
        I have a passion for technology and software development, and I'm always eager to learn new skills.
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Education")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.subheader("UPES, Dehradun, India")
st.write("**Bachelors of Technology in CSE – Full Stack Development** (August 2023 - Present)")
st.write("C GPA: 7.8 / 10.0")
st.subheader("Jyoti Niketan School, Azamgarh")
st.write("**Indian School Certificate (ISC)** (April 2021 – June 2022) - Percentage: 81.6 / 100.0")
st.write("**Indian Certificate of Secondary Education (ICSE)** (April 2019 - June 2020) - Percentage: 90.2 / 100.0")

st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Internships")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.subheader("Accenture UK Developer and Technology Virtual Experience Programme")
st.write("Completed the Developer and Technology Job Simulation (October 2024)")
st.write("- Developed an end-to-end understanding of the Software Development Lifecycle.")
st.write("- Researched emerging technology trends in DevOps.")
st.write("- Created a PowerPoint presentation analyzing Waterfall and Agile methodologies.")
st.write("- Designed a custom algorithm using pseudocode.")
st.write("- Debugged a Python program.")

st.subheader("Goldman Sachs Software Engineering Virtual Experience Program")
st.write("Completed a job simulation as a governance analyst (May 2024)")
st.write("- Assessed IT security and suggested improvements.")
st.write("- Identified outdated password hashing algorithms.")
st.write("- Proposed uplifts to increase password protection.")

st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Projects")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.subheader("News Aggregator")
st.write("Technologies Used: HTML, CSS, React JS, Node JS")
st.write("A news aggregator project built using the MERN stack (MongoDB, Express, React, Node.js) that allows users to view news articles from various sources.")
st.write("[View Project](https://github.com/abhinxvz/news_aggregator)")

st.subheader("Login Authenticator")
st.write("Technologies Used: HTML, CSS, JavaScript, Firebase")
st.write("Demonstrates how to implement a login authenticator using Firebase and Node.js.")
st.write("[View Project](https://github.com/abhinxvz/Login_Authenticator)")

st.subheader("Chatbot")
st.write("Technologies Used: HTML, CSS, JavaScript")
st.write("A clone of ChatGPT, built using JavaScript, allowing users to interact with a chatbot.")
st.write("[View Project](https://github.com/abhinxvz/chat-bot)")


st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Skills")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.write("**Programming Languages:** C, Java, Python, JavaScript, C++")
st.write("**Web Technologies:** HTML, CSS, Node JS, React JS")
st.write("**Cloud Skills:** Cloud Computing Fundamentals, Create and Manage Cloud Resources")
st.write("**Soft Skills:** Communication, Leadership, Teamwork, Problem Solving, Critical Thinking, Adaptability, Time Management")
st.write("**Miscellaneous:** MySQL, Git, GitHub, Gitlab, Vercel, Photoshop, Illustrator, Figma, Firebase")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Technical Certifications")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
certifications = [
    "Microsoft Learn Cloud Skills Challenge at Build 2024",
    "Responsive Web Design - freeCodeCamp",
    "Google Cloud Computing Foundations: Cloud Computing Fundamentals",
    "Advanced Software Engineering Job Simulation at Walmart",
    "Backend Web Development: DevTown",
    "Implement Load Balancing on Compute Engine Skill Badge"
]
for cert in certifications:
    st.write(f"- {cert}")

st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Positions of Responsibility")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.subheader("Design Lead, OPEN COMMUNITY UPES")
st.write("**Sept 2024 – Present**")
st.write("- Created placement posters for seniors.")
st.write("- Worked on future events like gaming and technical workshops.")

st.subheader("Core Team Member, Google Developer Groups")
st.write("**Sept 2024 – Present**")
st.write("- Designed layouts for events.")
st.write("- Organized workshops and was a speaker for a UI/UX workshop.")

st.subheader("Core Committee Member at UPES CSI")
st.write("**June 2024 – October 2024**")
st.write("- Designed iterations for various festivals like Guru Purnima, Janmashtami, etc.")
st.write("- Promoted the YUGMAK flagship event of CSI.")
st.write("- Created sponsors grid for social media.")
st.write("- Designed ARENA 3.0 poster.")

st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Accomplishments & Recognition")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
accomplishments = [
    "SIH Round 1 Winner (2024)",
    "Silver League with 6875 points at cloudskillsboost (2023)",
    "Attended webinar session on DSA Blueprint to Success organized by ULSA (2024)",
    "Solved 51 questions on LeetCode with a streak of 35 days (2021)",
    "Gold Medalist, NSTSE Olympiad (2016)",
    "Participated in CSI Hackathon 8.0 (2024)",
    "51 Badges and 11 trophies and at LEVEL 9 in Microsoft Learn (2023 - 24)",
    "Completed Level 1 of the Asia AI Odyssey Challenge (MS Learn 2024)",
    "Contributor at Buildspace (Gaudmire) (2024)",
    "Contributor at Google Facilitator Program (2024)",
    "Indigo Squad Member at Mood Indigo, IIT Bombay (2024)"
]
for accomplishment in accomplishments:
    st.write(f"- {accomplishment}")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.header("Contact Me")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.markdown("""
    Feel free to reach out to me through the following channels:
    - **Email:** [abhinxv18@gmail.com](mailto:abhinxv18@gmail.com)
    - **LinkedIn:** [abhinav-singh-a33026269](https://www.linkedin.com/in/abhinav-singh-a33026269)
    - **GitHub:** [abhinxvz](https://github.com/abhinxvz)
    - **Contact Number:** +91 9559987748
""")
st.markdown('<div class="strip"></div>', unsafe_allow_html=True)
st.markdown("""
    <style>
        footer {
            font-size: 14px;
            color: #555555;
            text-align: center;
            padding: 20px;
        }
    </style>
    <footer>
        Thank you for visiting my portfolio! I look forward to connecting with you.
    </footer>
""", unsafe_allow_html=True)
