import streamlit as st
import random
import math
import time

# --- 1. CORE ENGINE: ALL 31 QUESTION TEMPLATES ---

def generate_photon_q():
    nm = random.randint(380, 750)
    correct = (6.63e-34 * 3e8) / (nm * 1e-9)
    opts = [correct, correct*1.6e-19, correct/1e-9, 2.5e-19]
    random.shuffle(opts)
    return f"Calculate the energy of a single photon with a wavelength of {nm} nm.", opts, correct

def q_quark_composition():
    particles = {"Proton": "uud", "Neutron": "udd", "$\pi^+$ meson": "u anti-d", "$\pi^-$ meson": "anti-u d", "$K^+$ meson": "u anti-s", "$K^-$ meson": "anti-u s", "$K^0$ meson": "d anti-s"}
    name, correct = random.choice(list(particles.items()))
    opts = [correct, "uus", "ddd", "u anti-u"]
    random.shuffle(opts)
    return f"What is the quark composition of a {name}?", opts, correct

def q_specific_charge_n():
    m, g = random.randint(14, 16), random.randint(1, 3)
    correct = (g * -1.60e-19) / (m * 1.67e-27)
    opts = [correct, abs(correct), 4.19e7, 1.2e-8]
    random.shuffle(opts)
    return f"An atom of Nitrogen-{m} gains {g} electrons. Calculate the specific charge of the resulting ion.", opts, correct

def q_fluoride_ion():
    correct = 1.6e-19 / (19 * 1.67e-27)
    opts = [correct, 3.2e-26, 5.0e6, 8.4e-21]
    random.shuffle(opts)
    return "What is the magnitude of the specific charge of a fluoride ion ($_{9}^{19}F^{-}$)?", opts, correct

def q_annihilation():
    correct = (1.88e-28 * (3e8**2)) / 6.63e-34
    opts = [correct, correct/2, 5.1e16, 2.5e22]
    random.shuffle(opts)
    return "Two gamma photons are produced via muon-antimuon annihilation. What is the minimum frequency of the resulting radiation?", opts, correct

def q_photoelectric():
    correct = "Max KE Increases, Rate Decreases"
    opts = ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"]
    random.shuffle(opts)
    return "A beam of light of wavelength $\lambda$ is incident on a metal surface. The wavelength is halved but energy incident per second is kept the same. What happens to the Max KE and the number of photoelectrons emitted per second?", opts, correct

def q_de_broglie_speed():
    v_p = 2.8e4
    correct = (1.67e-27 * v_p) / 9.11e-31
    opts = [correct, v_p, 1.2e6, 5.1e7]
    random.shuffle(opts)
    return f"Electrons have the same de Broglie wavelength as protons moving at {v_p:.1e} m/s. What is the speed of the electrons?", opts, correct

def q_refractive_index():
    correct = 1.67
    opts = [1.67, 0.6, 1.33, 1.5]
    random.shuffle(opts)
    return "A light wave enters a glass block and slows down to 3/5 of its original speed. What is the refractive index of the glass?", opts, correct

def q_first_harmonic():
    correct = "l/2"
    opts = ["l/2", "2l", "l", "l/4"]
    random.shuffle(opts)
    return "A string has length $l$ and diameter $d$. A second string of same material and tension has diameter $2d$. What length $L$ is required for the second string to have the same first-harmonic frequency?", opts, correct

def q_double_slit_cover():
    correct = "Fewer maxima are observed"
    opts = ["Fewer maxima are observed", "Intensity of central maximum increases", "Width of central maximum decreases", "Outer maxima become wider"]
    random.shuffle(opts)
    return "In a standard two-slit interference experiment, one slit is covered with opaque black paper. What is the observable effect on the pattern?", opts, correct

def q_ultrasound_xray():
    correct = "Both can be polarised"
    opts = ["Both can be polarised", "Both can be refracted", "Both can be diffracted", "Both can be reflected"]
    random.shuffle(opts)
    return "Which of the following statements is **not** correct for both ultrasound waves and X-rays?", opts, correct

def q_diffraction_grating():
    lam = 5e-7
    d = (4 * lam) / math.sin(math.radians(30))
    correct = (1/d)/1000
    opts = [correct, 250, 500, 1000]
    random.shuffle(opts)
    return "Light of wavelength 500nm is incident on a grating. The 4th order maximum is observed at 30°. How many lines per mm are on the grating?", opts, correct

def q_rocket_thrust():
    m, a = 12000, 1.4
    correct = m * (9.81 + a)
    opts = [correct, m*a, m*9.81, 1.0e5]
    random.shuffle(opts)
    return f"A rocket of mass {m} kg accelerates upwards at {a} m/s². Calculate the thrust provided by the engines.", opts, correct

def q_projectile_time():
    v, ang = 25, 35
    correct = (2 * v * math.sin(math.radians(ang))) / 9.81
    opts = [correct, 1.5, 2.9, 4.2]
    random.shuffle(opts)
    return f"A projectile is launched from ground level at {v} m/s at an angle of {ang}° to the horizontal. How long until it hits the ground?", opts, correct

def q_projectile_dist():
    v, ang = 25, 42
    correct = (v**2 * math.sin(math.radians(2*ang))) / 9.81
    opts = [correct, 23.0, 32.0, 63.0]
    random.shuffle(opts)
    return f"A projectile is launched at {v} m/s at {ang}° to the horizontal. What is the total horizontal range?", opts, correct

def q_resultant_force():
    correct = "3N, 6N, 10N"
    opts = ["3N, 6N, 10N", "3N, 4N, 5N", "8N, 8N, 8N", "2N, 10N, 10N"]
    random.shuffle(opts)
    return "Which of the following combinations of coplanar forces can **never** produce a resultant force of zero?", opts, correct

def q_graph_features():
    correct = "Gradient of v-t / Area under a-t"
    opts = ["Gradient of v-t / Area under a-t", "Gradient of s-t / Area under v-t", "Gradient of v-t / Area under s-t", "Gradient of s-t / Area under a-t"]
    random.shuffle(opts)
    return "In kinematics, which of the following pairs of features provide the same physical information?", opts, correct

def q_young_modulus_theory():
    correct = "E"
    opts = ["E", "0.25E", "6E", "12E"]
    random.shuffle(opts)
    return "Wire X has three times the length and half the diameter of wire Y. If both are made of the same material, what is the Young Modulus of X relative to Y?", opts, correct

def q_wire_extension_ratio():
    correct = "0.5e"
    opts = ["0.5e", "e", "2e", "4e"]
    random.shuffle(opts)
    return "Wire W has length $l$ and radius $r$. Wire X is made of the same material and has length $2l$ and radius $2r$. If both support the same load, and W extends by $e$, what is the extension of X?", opts, correct

def q_spring_extension():
    w, dp, l, k = 18, 0.65, 0.8, 240
    correct = ((w*dp)/l)/k
    opts = [correct, 0.014, 0.04, 0.05]
    random.shuffle(opts)
    return f"A {w}N sign is {l}m long. Its center of mass is {dp}m from spring P. If $k={k}$ N/m, find the extension of spring Q at the far end.", opts, correct

def q_momentum_collision():
    mc, mv, vva, vca = 580, 1200, 6.2, -1.6
    correct = (mv*vva + mc*vca)/mc
    opts = [correct, 5.4, 11.2, 14.4]
    random.shuffle(opts)
    return f"A {mc}kg car hits a stationary {mv}kg van. The van moves forward at 6.2m/s while the car recoils at 1.6m/s. Initial car speed?", opts, correct

def q_voltmeter_ideal():
    correct = "In parallel with infinite resistance"
    opts = ["In parallel with infinite resistance", "In series with zero resistance", "In parallel with zero resistance", "In series with infinite resistance"]
    random.shuffle(opts)
    return "What are the ideal properties for a voltmeter to minimize its effect on a circuit?", opts, correct

def q_led_resistor():
    v, ri, vled, i = 5, 10, 1.8, 0.02
    correct = ((v-vled)/i)-ri
    opts = [correct, 80, 150, 160]
    random.shuffle(opts)
    return f"A 5V battery (10Ω internal) powers an LED (1.8V, 20mA). What series resistor R is needed?", opts, correct

def q_ion_flow():
    i = 0.64
    correct = (i*60)/(2*1.6e-19)
    opts = [correct, 1.2e20, 2.4e20, 4.0e18]
    random.shuffle(opts)
    return f"A beam of doubly-charged positive ions ($2e$) constitutes a current of {i}A. How many ions pass a point in 1 minute?", opts, correct

def q_parallel_resistors():
    correct = "Decreases non-linearly"
    opts = ["Decreases non-linearly", "Decreases linearly", "Increases linearly", "Stays the same"]
    random.shuffle(opts)
    return "As the number of identical resistors connected in parallel increases, how does the total resistance $R$ of the circuit change?", opts, correct

def q_wire_parallel():
    correct = "R/9"
    opts = ["R/9", "R/5", "2R/3", "R/3"]
    random.shuffle(opts)
    return "Wire P has resistance $R$. Wire Q, of the same material, is 1/4 the length and has 2x the diameter. What is the total resistance when connected in parallel?", opts, correct

def q_battery_discharge():
    p, v, cap = 0.2, 3.7, 9400
    correct = (cap/(p/v))/3600
    opts = [correct, 24, 48, 140]
    random.shuffle(opts)
    return f"A phone consumes {p*1000}mW at 3.7V. If the battery capacity is {cap}C, how many hours will it last?", opts, correct

def q_putty_resistors():
    correct = "5R"
    opts = ["5R", "4R", "3R", "2R"]
    random.shuffle(opts)
    return "Resistor Y has twice the diameter of Resistor X but the same length and material. If Y has resistance $R$, what is the total resistance when they are in series?", opts, correct

def q_shm_phase():
    correct = "π rad"
    opts = ["π rad", "0", "π/2 rad", "2π rad"]
    random.shuffle(opts)
    return "What is the phase difference between acceleration and displacement for an object undergoing Simple Harmonic Motion?", opts, correct

def q_shm_ke():
    m, amp, f = 0.15, 0.055, 0.8
    correct = 0.5 * m * (2*math.pi*f*amp)**2
    opts = [correct, 5.7e-3, 0.57, 11]
    random.shuffle(opts)
    return f"A {m}kg mass oscillates in SHM with amplitude {amp}m and frequency {f}Hz. Calculate the maximum Kinetic Energy.", opts, correct

def q_graph_ep():
    correct = "Parabola opening upwards"
    opts = ["Parabola opening upwards", "V-shape", "Straight line passing through origin", "Inverted Parabola"]
    random.shuffle(opts)
    return "Which graph correctly represents Gravitational Potential Energy ($E_p$) versus displacement ($s$) for a simple pendulum?", opts, correct

# --- 2. UI LOGIC ---

st.set_page_config(page_title="AQA Physics Trainer", layout="centered")
st.title("⚛️ AQA Physics Paper 1: Infinite Trainer")

# ULTIMATE FORMATTER: Handles rounding to 3 sig figs and prevents TypeErrors
def safe_format(x):
    if isinstance(x, (int, float)):
        if x == 0: return "0"
        # Scientific notation for very small/large magnitudes
        if abs(x) > 1000 or (0 < abs(x) < 0.01):
            return f"{x:.2e}"
        # Standard rounding to 3 significant figures
        return f"{float(f'{x:.3g}'):g}"
    return str(x)

topics = [
    generate_photon_q, q_quark_composition, q_specific_charge_n, q_fluoride_ion, q_annihilation, 
    q_photoelectric, q_de_broglie_speed, q_refractive_index, q_first_harmonic, q_double_slit_cover, 
    q_ultrasound_xray, q_diffraction_grating, q_rocket_thrust, q_projectile_time, q_projectile_dist, 
    q_resultant_force, q_graph_features, q_young_modulus_theory, q_wire_extension_ratio, q_spring_extension, 
    q_momentum_collision, q_voltmeter_ideal, q_led_resistor, q_ion_flow, q_parallel_resistors, 
    q_wire_parallel, q_battery_discharge, q_putty_resistors, q_shm_phase, q_shm_ke, q_graph_ep
]

if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(topics)()
    st.session_state.start_time = time.time()
    st.session_state.answered = False
    st.session_state.q_key = 0 

text, opts, correct = st.session_state.current_q

st.subheader("Question:")
st.write(text)

# Dynamic key ensure selection is cleared on "Next"
user_choice = st.radio("Select Answer:", opts, format_func=safe_format, key=f"rad_{st.session_state.q_key}")

feedback = st.empty()

c1, c2 = st.columns(2)
with c1:
    if st.button("Check Answer"):
        st.session_state.answered = True

if st.session_state.answered:
    if user_choice == correct:
        feedback.success("🎯 Correct!")
    else:
        feedback.error(f"❌ Incorrect. Answer: {safe_format(correct)}")

with c2:
    if st.button("Next Question"):
        st.session_state.current_q = random.choice(topics)()
        st.session_state.start_time = time.time()
        st.session_state.answered = False
        st.session_state.q_key += 1 
        st.rerun()

st.divider()

# Timer Display
timer = st.empty()
left = 60 - int(time.time() - st.session_state.start_time)
if left > 0:
    timer.metric("Time Remaining", f"{left}s")
    time.sleep(1)
    st.rerun()
else:
    timer.error("⏰ Time's up! Speed is essential for AQA Paper 1.")
