import streamlit as st
import random
import math

# --- 1. QUESTION TEMPLATES ---

def q_specific_charge():
    protons, mass_num = 7, 16
    electrons_gained = 3
    total_mass = mass_num * 1.67e-27
    net_charge = electrons_gained * -1.60e-19
    ans = net_charge / total_mass
    return f"An atom of Nitrogen-16 ($_{7}^{16}N$) gains {electrons_gained} electrons. What is the specific charge of the ion?", [ans, abs(ans), ans*2, 4.19e7], ans

def q_photoelectric():
    # Logic: wavelength halved -> frequency doubled -> Max KE increases. 
    # Power same but energy per photon doubled -> fewer photons per second.
    question = "A beam of light of wavelength $\lambda$ is incident on a metal surface. The wavelength is halved but energy incident per second is kept the same. What happens to the Max KE and the number of photoelectrons emitted per second?"
    options = ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"]
    return question, options, "Max KE Increases, Rate Decreases"

def q_de_broglie_speed():
    m_p, m_e = 1.67e-27, 9.11e-31
    v_p = 2.8e4
    v_e = (m_p * v_p) / m_e
    return f"Electrons have the same de Broglie wavelength as protons moving at {v_p:.1e} m/s. What is the speed of the electrons?", [v_e, v_p, 1.2e6, 5.1e7], v_e

def q_ultrasound_xray():
    question = "Which statement is **not** correct for both ultrasound and X-rays?"
    options = ["Both can be polarised", "Both can be refracted", "Both can be diffracted", "Both can be reflected"]
    return question, options, "Both can be polarised"

def q_first_harmonic():
    # f = (1 / 2L) * sqrt(T/mu). mu = density * Area. 
    # If Diameter doubles, Area quadruples, mu quadruples.
    # To keep f same: If D -> 2D, sqrt(mu) -> 2. So L must become L/2 to cancel it out.
    question = "A string has length $l$ and diameter $d$. A second string of the same material and tension needs the same first-harmonic frequency. If the diameter is $2d$, what must the length be?"
    return question, ["l/2", "2l", "l", "l/4"], "l/2"

def q_double_slit_cover():
    question = "In a two-slit interference pattern, one slit is covered with opaque black paper. What is the effect?"
    options = ["Fewer maxima are observed", "Intensity of central maximum increases", "Width of central maximum decreases", "Outer maxima become wider"]
    return question, options, "Fewer maxima are observed"

def q_diffraction_grating():
    # n * lambda = d * sin(theta)
    n, lam, theta = 4, 5.0e-7, 30
    d = (n * lam) / math.sin(math.radians(theta))
    lines_per_m = 1 / d
    lines_per_mm = lines_per_m / 1000
    return f"Light of wavelength {lam:.1e} m is incident on a grating. The 4th order maximum is at 30°. How many lines per mm?", [lines_per_mm, lines_per_mm*1000, 1.0e3, 2.5e2], lines_per_mm

def q_graph_features():
    question = "Which row gives two features of graphs that provide the same information?"
    options = ["Gradient of v-t / Area under a-t", "Gradient of s-t / Area under v-t", "Gradient of v-t / Area under s-t", "Gradient of s-t / Area under a-t"]
    return question, options, "Gradient of v-t / Area under a-t"

def q_rocket_thrust():
    m, a, g = 12000, 1.4, 9.81
    # Thrust - mg = ma  => Thrust = m(g + a)
    thrust = m * (g + a)
    return f"A rocket of mass {m} kg accelerates upwards at {a} m/s². What is the thrust?", [thrust, m*a, m*g, 1.7e4], thrust

def q_projectile_dist():
    v, angle, g = 25, 42, 9.81
    range_val = (v**2 * math.sin(math.radians(2 * angle))) / g
    return f"A projectile is launched at {v} m/s at {angle}° to the horizontal. What is the horizontal distance when it hits the ground?", [range_val, 23.0, 32.0, 63.0], range_val

def q_momentum_collision():
    m_c, m_v = 580, 1200
    v_v_after, v_c_after = 6.20, -1.60
    # m_c * u_c + 0 = m_v * v_v + m_c * v_c
    u_c = (m_v * v_v_after + m_c * v_c_after) / m_c
    return f"A {m_c}kg car hits a stationary {m_v}kg van. Van moves at {v_v_after} m/s, car recoils at {abs(v_c_after)} m/s. Initial car speed?", [u_c, 5.43, 12.8, 14.4], u_c

def q_young_modulus_ratio():
    question = "A wire has Young modulus $E$. A second wire of the same material has 3x length and 0.5x diameter. What is its Young modulus?"
    return question, ["E", "0.25E", "6E", "12E"], "E"

def q_led_resistor():
    emf, r_int, v_led, i = 5, 10, 1.8, 0.020
    # EMF = I(R + r + R_led_equiv) -> R = (EMF - V_led)/I - r
    r_ext = ((emf - v_led) / i) - r_int
    return f"Battery (5V, 10Ω internal) powers an LED (1.8V, 20mA). What is the value of resistor R needed in series?", [r_ext, 80.0, 160.0, 90.0], r_ext

def q_parallel_resistors():
    question = "As the number of identical resistors $n$ in parallel increases, how does the total resistance $R_n$ change?"
    options = ["Decreases non-linearly", "Decreases linearly", "Increases linearly", "Increases non-linearly"]
    return question, options, "Decreases non-linearly"

def q_wire_parallel():
    # R = rho * L / A. Wire Q: rho, L/4, 2A -> R_q = R / 8
    # 1/Rt = 1/R + 1/(R/8) = 1/R + 8/R = 9/R -> Rt = R/9
    question = "Wire P has resistance $R$. Wire Q has 1/4 the length and 2x the area. What is the total resistance if connected in parallel?", ["R/9", "R/3", "2R/3", "3R/2"], "R/9"

# --- 2. INTERFACE LOGIC ---

st.set_page_config(page_title="AQA Physics Trainer")
st.title("🚀 AQA Physics Paper 1: Infinite MCQs")

all_questions = [
    q_specific_charge, q_photoelectric, q_de_broglie_speed, q_ultrasound_xray,
    q_first_harmonic, q_double_slit_cover, q_diffraction_grating, q_graph_features,
    q_rocket_thrust, q_projectile_dist, q_momentum_collision, q_young_modulus_ratio,
    q_led_resistor, q_parallel_resistors, q_wire_parallel
]

if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(all_questions)()

q_text, q_options, q_ans = st.session_state.current_q

st.subheader("Question:")
st.write(q_text)

user_choice = st.radio("Select Answer:", q_options, format_func=lambda x: f"{x:.2e}" if isinstance(x, float) and (x > 1000 or x < 0.1) else x)

if st.button("Check Answer"):
    if user_choice == q_ans:
        st.success("Correct!")
    else:
        st.error(f"Incorrect. The correct answer was {q_ans}")

if st.button("Next Random Question"):
    st.session_state.current_q = random.choice(all_questions)()
    st.rerun()
