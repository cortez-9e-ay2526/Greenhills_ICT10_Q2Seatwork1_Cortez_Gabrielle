from pyscript import document
from pyodide.ffi.wrappers import add_event_listener

def view_user(event):
    # Wipe visual containers and targets cleanly before analysis passes
    document.getElementById('result').innerHTML = ''
    slender_box = document.getElementById('slender-container')
    static_screen = document.getElementById('static-screen')
    card_box = document.getElementById('card-box')
    
    slender_box.style.display = "none"
    slender_box.style.opacity = "0"
    static_screen.style.display = "none"
    card_box.style.animation = "none"

    # Grab values safely out from target raw inputs
    first = document.getElementById('firstname').value
    last = document.getElementById('lastname').value
    
    # Strip inner and extra whitespace sequences smoothly
    clean_first = " ".join(first.split())
    clean_last = " ".join(last.split())
    full_name = f"{clean_first} {clean_last}".strip()
    
    # Master list of combined school records and entities
    club_members = [
        "victoria rivera", "reuben lim", "antonio manalo", "juan manapat", 
        "lucas dannug", "reign macachor", "hans ukwatte", "dan perez", 
        "kirche segura", "chelsea coronado", "elaina daclan", "na yeon kim", 
        "kristine manabat", "arkin cuenca", "zangief briones", "cedric visorde", 
        "mohammad calaca", "lara estrada", "cassiopeia rigodon", "miiska eugenio", 
        "kristine pasco", "joshua ortiz", "josua ortiz",
        "jeffrey woods", "liu woods", "toby rogers", "sally williams", 
        "jack nichols", "jane arkensaw", "jane richardson", "nina hopkins", 
        "natalie oulette", "helen otis", "tim wright", "brian thomas", 
        "jonathan blake", "dina clark", "benjamin lawman", "ben"
    ]
    
    # Run lookup check across case-lowered string
    student_checker = full_name.lower() in club_members

    # Strictly conforms to zero conditional branches/loops layout using a binary tuple offset matrix
    display_message = (
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    )
    
    # Assign message into result div target
    document.getElementById('result').innerHTML = display_message[student_checker]

    # Visual dynamic effects mapping trick utilizing lists to match the boolean evaluation index
    # [0] (False path) changes nothing. [1] (True path) displays Slenderman, adds screen noise, and shakes the container
    display_styles = ["none", "block"]
    slender_box.style.display = display_styles[student_checker]
    static_screen.style.display = display_styles[student_checker]
    
    # Inject transitions smoothly if validation check is successful
    opacity_styles = ["0", "1"]
    slender_box.style.opacity = opacity_styles[student_checker]
    
    animation_styles = ["none", "aggressive-shake 0.1s infinite"]
    card_box.style.animation = animation_styles[student_checker]

# Secure modern explicit global click action binder tracking loop
add_event_listener(document.getElementById("submit-btn"), "click", view_user)
