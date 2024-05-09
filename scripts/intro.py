# rating = [1, 2, 3, 4, 5]
# rating = ["20px", "40px", "60px", "80px", "100px"]

def intro():    
    dic = {
        "status" : ["Graduate Electronics Engineer at Mercedes AMG High Performance Powertrain"],
        "skillrating" : ["100px", "80px", "100px", "80px", \
                        "80px", "100px", "60px", "60px", "40px", \
                        "40px", "80px", \
                        "80px", "40px", "20px", "20px"],
        "skills" : ["MATLAB", "Python", "KiCad", "Altium", \
                    "PLECS", "LTSPICE", "Autodesk Inventor","OrCAD", "NX",\
                    "SolidWorks", "HTML & CSS", \
                    "Excel", "HDL", "C", "C++"],
        "skilldesc" : ["Extensive knowledge using MATLAB throughout my studies. Creating scripts for bulk calculations e.g. transformer design to determine optimal design. \
                    Simulink simulating control (digital and analog) of electronics.",
                    "Scripts for calculations and estimations of electronics circuits. Furthermore, this website uses Python \
                        along with Flask as part of implementing variables in HTML.",
                    "Used KiCad during my formula student days along with GitHub to share and maintain projects.",
                    "Designing circuits and creating layouts along with rulesets Altium as a research assistant at SDU and in my early worklife.",
                    "Advanced PLECS simulations estimating system response of power converters and thermal losses. With and without MATLAB integration.",
                    "Circuit simulations design during student days and early worklife.",
                    "Using Autodesk Inventor during my time in formula student and during my studies. Mostly to import PCBs and design \
                       test 3D printed rigs.",
                    "Using OrCAD only for circuit design.",
                    "Working with NX to import and release PCBs for manufacturing.",
                    "Using SolidWorks during my formula student days in Australia.",
                    "I have been using HTML during creation of this website. HTML with python integration. \
                        CSS is the style sheet language that have been setup the HTML elements of this website.",
                    "Using excel integration with python and creating macros for automation.",
                    "Introduced to programming FPGAs during my studies. Worked on a simple project to set up a game with HDL and C.",
                    "Using C during my days as a student and in early worklife.",
                    "Introduced to object-oriented programming during my studies, with main focus on C++.",],
        "interests" : ["Formula 1", "Electric Vehicles", "Sports",
                    "Football", "Space Exploration"],
        "activities" : ["Football", "Running", "Music", "Hiking"],
        "location" : ""
    }
    return dic

def summary():
    dic = ["I am an electrical engineer, with a particular interest in power electronics. ",
                "I am passionately pursuing a career to be at the forefront of inventing new technologies for a renewable future.",
                "I am constantly seeking for opportunities to broaden my knowledge by learning and sharing experiences.", 
                "I love to work together with people who share my passion for always doing their best to create the newest, ",
                "highperformance solutions, which is why I have chosen to spend the majority of my spare time working",
                "on the Formula Student project."]
    return dic
