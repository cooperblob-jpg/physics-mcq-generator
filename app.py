import streamlit as st
import random
import math
import time

# --- 1. CORE ENGINE: ALL 31 QUESTION TEMPLATES ---
# Verified: Full wording restored and variables synchronized

def generate_photon_q():
    nm = random.randint(380, 750)
    e = (6.63e-34 * 3e8) / (nm * 1e-9)
    return f"Calculate the energy of a single photon with a wavelength of {nm} nm.", [e, e*1.6e-19, e/1e-9, 2.5e-19], e

def q_quark_composition():
    particles = {"Proton": "uud", "Neutron": "udd", "$\pi^+$ meson": "u anti-d", "$\pi^-$ meson": "anti-u d", "$K^+$ meson": "u anti-s", "$K^-$ meson": "anti-u s", "$K^0$ meson": "d anti-s"}
    name, correct = random.choice(list(particles.items()))
    opts = [correct, "uus", "ddd", "u anti-u"]
    random.shuffle(opts)
    return f"What is the quark composition of a {name}?", opts, correct

def q_specific_charge_n():
    m, g = random.randint(14, 16), random.randint(1, 3)
    ans = (g * -1.60e-19) / (m * 1.67e-27)
    return f"An atom of Nitrogen-{m} gains {g} electrons. Calculate the specific charge of the resulting ion.", [ans, abs(ans), 4.19e7, 1.2e-8], ans

def q_fluoride_ion():
    ans = 1.6e-19 / (19 * 1.67e-27)
    return "What is the magnitude of the specific charge of a fluoride ion ($_{9}^{19}F^{-}$)?", [ans, 3.2e-26, 5.0e6, 8.4e-21], ans

def q_annihilation():
    f = (1.88e-28 * (3e8**2)) / 6.63e-34
    return "Two gamma photons are produced via muon-antimuon annihilation. What is the minimum frequency of the resulting radiation?", [f, f/2, 5.1e16, 2.5e22], f

def q_photoelectric():
    return "A beam of light of wavelength $\lambda$ is incident on a metal surface. The wavelength is halved but energy incident per second is kept the same. What happens to the Max KE and the number of photoelectrons emitted per second?", ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"], "Max KE Increases, Rate Decreases"

def q_de_broglie_speed():
    v_p = 2.8e4
    v_e = (1.67e-27 * v_p) / 9.11e-31
    return f"Electrons have the same de Broglie wavelength as protons moving at {v_p:.1e} m/s. What is the speed of the electrons?", [v_e, v_p, 1.2e6, 5.1e7], v_e

def q_refractive_index():
    return "A light wave enters a glass block and slows down to 3/5 of its original speed. What is the refractive index of the glass?", [1.67, 0.6, 1.33, 1.5], 1.67

def q_first_harmonic():
    return "A string has length $l$ and diameter $d$. A second string of same material and tension has diameter $2d$. What length $L$ is required for the second string to have the same first-harmonic frequency?", ["l/2", "2l", "l", "l/4"], "l/2"

def q_double_slit_cover():
    return "In a standard two-slit interference experiment, one slit is covered with opaque black paper. What is the observable effect on the pattern?", ["Fewer maxima are observed", "Intensity of central maximum increases", "Width of central maximum decreases", "Outer maxima become wider"], "Fewer maxima are observed"

def q_ultrasound_xray():
    return "Which of the following statements is **not** correct for both ultrasound waves and X-rays?", ["Both can be polarised", "Both can be refracted", "Both can be diffracted", "Both can be reflected"], "Both can be polarised"

def q_diffraction_grating():
    lam = 5e-7
    d = (4 * lam) / math.sin(math.radians(30))
    lpm = (1/d)/1000
    return "Light of wavelength 500nm is incident on a grating. The 4th order maximum is observed at 30°. How many lines per mm are on the grating?", [lpm, 250, 500, 1000], lpm

def q_rocket_thrust():
    m, a = 12000, 1.4
    t = m * (9.81 + a)
    return f"A rocket of mass {m} kg accelerates upwards at {a} m/s². Calculate the thrust provided by the engines.", [t, m*a, m*9.81, 1.0e5], t

def q_projectile_time():
    v, ang = 25, 35
    t = (2 * v * math.sin(math.radians(ang))) / 9.81
    return f"A projectile is launched from ground level at {v} m/s at an angle of {ang}° to the horizontal. How long until it hits the ground?", [t, 1.5, 2.9, 4.2], t

def q_projectile_dist():
    v, ang = 25, 42
    r = (v**2 * math.sin(math.radians(2*ang))) / 9.81
    return f"A projectile is launched at {v} m/s at {ang}° to the horizontal. What is the total horizontal range?", [r, 23.0, 32.0, 63.0], r

def q_resultant_force():
    return "Which of the following combinations of coplanar forces can **never** produce a resultant force of zero?", ["3N, 6N, 10N", "3N, 4N, 5N", "8N, 8N, 8N", "2N, 10N, 10N"], "3N, 6N, 10N"

def q_graph_features():
    return "In kinematics, which of the following pairs of features provide the same physical information?", ["Gradient of v-t / Area under a-t", "Gradient of s-t / Area under v-t", "Gradient of v-t / Area under s-t", "Gradient of s-t / Area under a-t"], "Gradient of v-t / Area under a-t"

def q_young_modulus_theory():
    return "Wire X has three times the length and half the diameter of wire Y. If both are made of the same material, what is the Young Modulus of X relative to Y?", ["E", "0.25E", "6E", "12E"], "E"

def q_wire_extension_ratio():
    return "Wire W has length $l$ and radius $r$. Wire X is made of the same material and has length $2l$ and radius $2r$. If both support the same load, and W extends by $e$, what is the extension of X?", ["0.5e", "e", "2e", "4e"], "0.5e"

def q_spring_extension():
    w, dp, l, k = 18, 0.65, 0.8, 240
    ext = ((w*dp)/l)/k
    return f"A {w}N sign is {l}m long. Its center of mass is {dp}m from spring P. If $k={k}$ N/m, find the extension of spring Q at the far end.", [ext, 0.014, 0.04, 0.05], ext

def q_momentum_collision():
    mc, mv, vva, vca = 580, 1200, 6.2, -1.6
    u = (mv*vva + mc*vca)/mc
    return f"A {mc}kg car hits a stationary {mv}kg van. The van moves forward at 6.2m/s while the car recoils at 1.6m/s. Initial car speed?", [u, 5.4, 11.2, 14.4], u

def q_voltmeter_ideal():
    return "What are the ideal properties for a voltmeter to minimize its effect on a circuit?", ["In parallel with infinite resistance", "In series with zero resistance", "In parallel with zero resistance", "In series with infinite resistance"], "In parallel with infinite resistance"

def q_led_resistor():
    v, ri, vled, i = 5, 10, 1.8, 0.02
    r = ((v-vled)/i)-ri
    return f"A 5V battery (10Ω internal) powers an LED (1.8V, 20mA). What series resistor R is needed?", [r, 80, 150, 160], r

def q_ion_flow():
    i = 0.64
    n = (i*60)/(2*1.6e-19)
    return f"A beam of doubly-charged positive ions ($2e$) constitutes a current of {i}A. How many ions pass a point in 1 minute?", [n, 1.2e20, 2.4e20, 4.0e18], n

def q_parallel_resistors():
    return "As the number of identical resistors connected in parallel increases, how does the total resistance $R$ of the circuit change?", ["Decreases non-linearly", "Decreases linearly", "Increases linearly", "Stays the same"], "Decreases non-linearly"

def q_wire_parallel():
    return "Wire P has resistance $R$. Wire Q, of the same material, is 1/4 the length and has 2x the diameter. What is the total resistance when connected in parallel?", ["R/9", "R/5", "2R/3", "R/3"], "R/9"

def q_battery_discharge():
    p, v, cap = 0.2, 3.7, 9400
    h = (cap/(p/v))/3600
    return f"A phone consumes {p*1000}mW at 3.7V. If the battery capacity is {cap}C, how many hours will it last?", [h, 24, 48, 140], h

def q_putty_resistors():
    return "Resistor Y has twice the diameter of Resistor X but the same length and material. If Y has resistance $R$, what is the total resistance when they are in series?", ["5R", "4R", "3R", "2R"], "5R"

def q_shm_phase():
    return "What is the phase difference between acceleration and displacement for an object undergoing Simple Harmonic Motion?", ["π rad", "0", "π/2 rad", "2π rad"], "π rad"

def q_shm_ke():
    m, amp, f = 0.15, 0.055, 0.8
    ke = 0.5 * m * (2*math.pi*f*amp)**2
    return f"A {m}kg mass oscillates in SHM with amplitude {amp}m and frequency {f}Hz. Calculate the maximum Kinetic Energy.", [ke, 5.7e-3, 0.57, 11], ke

def q_graph_ep():
    return "Which graph correctly represents Gravitational Potential Energy ($E_p$) versus displacement ($s$) for a simple pendulum?", ["Parabola opening upwards", "V-shape", "Straight line passing through origin", "Inverted Parabola"], "Parabola opening upwards"

# --- 2. INTERFACE LOGIC ---

st.set_page_config(page_title="AQA Physics Master")
st.title("⚛️ AQA Physics Paper 1 Practice")

# Verified Formatter: Handles strings and floats separately to avoid TypeError
def safe_format(x):
    if isinstance(x, (int, float)):
        if abs(x) > 1000 or (0 < abs(x) < 0.01):
            return f"{x:.2e}"
    return str(x)

topics = [
    generate_photon_q, q_quark_composition, q_specific_charge_n, q_fluoride_ion, q_annihilation, 
    q_photoelectric, q_de_broglie_speed, q_refractive_index, q_first_harmonic, q_double_slit_cover, 
    q_ultrasound_xray, q_diffraction_grating, q_rocket_thrust, q_projectile_time, q_projectile_dist, 
    q_resultant_force, q_graph_features, q_young_modulus_theory, q_wire_extension_ratio, q_spring_extension, 
    q_momentum_collision, q_voltmeter_ideal, q_led_resistor, q_ion_flow, q_parallel_resistors, 
    q_wire_parallel, q_battery_discharge, q_putty_resistors, q_shm_phase, q_shm_ke, q_graph_ep
]

# SESSION INITIALIZATION
if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(topics)()
    st.session_state.start_time = time.time()
    st.session_state.answered = False # Tracks if answer feedback should be shown

text, opts, correct = st.session_state.current_q

# DISPLAY
st.subheader("Question:")
st.write(text)

# RADIO BUTTON
user_choice = st.radio("Select Answer:", opts, format_func=safe_format, key="physics_radio")

# FEEDBACK LOGIC
feedback_container = st.empty()

col1, col2 = st.columns(2)
with col1:
    if st.button("Check Answer"):
        st.session_state.answered = True

if st.session_state.answered:
    if user_choice == correct:
        feedback_container.success("🎯 Correct!")
    else:
        feedback_container.error(f"❌ Incorrect. The answer was: {safe_format(correct)}")

with col2:
    if st.button("Next Question"):
        st.session_state.current_q = random.choice(topics)()
        st.session_state.start_time = time.time()
        st.session_state.answered = False # Reset feedback for next question
        st.rerun()

st.divider()

# TIMER
timer_placeholder = st.empty()
seconds_left = 60 - int(time.time() - st.session_state.start_time)

if seconds_left > 0:
    timer_placeholder.metric("Time Remaining", f"{seconds_left}s")
    time.sleep(1)
    st.rerun()
else:
    timer_placeholder.error("⏰ Time's up! Speed is key for Section C.")
