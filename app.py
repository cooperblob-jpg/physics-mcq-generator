import streamlit as st
import random
import math
import time

# --- 1. QUESTION TEMPLATES (All 31 Types) ---

# -- PARTICLES & RADIATION --
def q_quark_composition():
    particles = {"Proton": "uud", "Neutron": "udd", "$\pi^+$ meson": "u anti-d", "$\pi^-$ meson": "anti-u d", "$K^+$ meson": "u anti-s", "$K^-$ meson": "anti-u s", "$K^0$ meson": "d anti-s"}
    name, correct = random.choice(list(particles.items()))
    distractors = ["uus", "ddd", "u anti-u", "d anti-d"]
    options = list(set([correct] + random.sample(distractors, 3)))
    return f"What is the quark composition of a {name}?", options, correct

def q_specific_charge_n():
    protons, mass_num, gained = 7, 16, 3
    ans = (gained * -1.60e-19) / (mass_num * 1.67e-27)
    return f"An atom of Nitrogen-16 ($_{{7}}^{{16}}N$) gains {gained} electrons. What is the specific charge?", [ans, abs(ans), ans*2, 4.19e7], ans

def q_fluoride_ion():
    ans = -1.60e-19 / (19 * 1.67e-27)
    return "What is the magnitude of the specific charge of a fluoride ion ($_{9}^{19}F^{-}$)?", [abs(ans), 3.2e-26, 8.4e-21, 5.0e6], abs(ans)

def q_annihilation():
    m_muon, c, h = 1.88e-28, 3e8, 6.63e-34
    f = (m_muon * (c**2)) / h
    return "Two gamma photons are produced via muon-antimuon annihilation. Min frequency?", [f, f/2, 2.55e22, 5.10e16], f

def q_photoelectric():
    return "Wavelength $\lambda$ is halved but total energy/sec is constant. What happens to Max KE and emission rate?", ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"], "Max KE Increases, Rate Decreases"

def generate_photon_q():
    nm = random.randint(380, 750)
    e = (6.63e-34 * 3e8) / (nm * 1e-9)
    return f"Calculate the energy of a photon with wavelength {nm} nm.", [e, e*1.6e-19, e/1e-9, 2.5e-19], e

def q_de_broglie_speed():
    m_p, m_e, v_p = 1.67e-27, 9.11e-31, 2.8e4
    v_e = (m_p * v_p) / m_e
    return f"Electrons have the same $\lambda_{{db}}$ as protons moving at {v_p:.1e} m/s. Electron speed?", [v_e, v_p, 1.2e6, 5.1e7], v_e

# -- WAVES & OPTICS --
def q_refractive_index():
    n, d = 3, 5
    ans = d / n
    return f"A wave slows to {n}/{d} of its original speed. Refractive index?", [ans, 1.33, 1.50, 0.67], ans

def q_first_harmonic():
    return "String length $l$, diameter $d$. If diameter becomes $2d$, what length $L$ keeps the same 1st harmonic frequency?", ["l/2", "2l", "l", "l/4"], "l/2"

def q_diffraction_grating():
    lam, theta = 5.0e-7, 30
    d = (4 * lam) / math.sin(math.radians(theta))
    lpm = (1 / d) / 1000
    return f"4th order max is at 30° for {lam:.1e}m light. Lines per mm?", [lpm, 1000, 250, 2.5e5], lpm

def q_ultrasound_xray():
    return "Which is NOT correct for both ultrasound and X-rays?", ["Both can be polarised", "Both refracted", "Both diffracted", "Both reflected"], "Both can be polarised"

def q_double_slit_cover():
    return "One slit is covered with opaque paper. Effect?", ["Fewer maxima observed", "Central max brighter", "Central max narrower", "Outer max wider"], "Fewer maxima observed"

# -- MECHANICS & MATERIALS --
def q_rocket_thrust():
    m, a, g = 12000, 1.4, 9.81
    thrust = m * (g + a)
    return f"Rocket mass {m}kg, acceleration {a}m/s². Thrust?", [thrust, 1.7e4, 1.0e5, 1.6e5], thrust

def q_projectile_time():
    v, ang = 25, 35
    t = (2 * v * math.sin(math.radians(ang))) / 9.81
    return f"Projectile launched at {v}m/s, {ang}°. Time until ground hit?", [t, 1.5, 2.1, 4.2], t

def q_spring_extension():
    w, dp, l, k = 18, 0.65, 0.80, 240
    ext = ((w * dp) / l) / k
    return f"{w}N sign, length {l}m. CoM is {dp}m from P. $k={k}$ N/m. Extension at Q?", [ext, 0.014, 0.038, 0.049], ext

def q_resultant_force():
    return "Which combination of forces can NEVER produce a zero resultant?", ["3N, 6N, 10N", "3N, 4N, 5N", "8N, 8N, 8N", "2N, 10N, 10N"], "3N, 6N, 10N"

def q_graph_features():
    return "Which row gives two features providing the same info?", ["Gradient of v-t / Area under a-t", "Gradient of s-t / Area under v-t", "Gradient of v-t / Area under s-t", "Gradient of s-t / Area under a-t"], "Gradient of v-t / Area under a-t"

def q_projectile_dist():
    v, ang = 25, 42
    r = (v**2 * math.sin(math.radians(2*ang))) / 9.81
    return f"Projectile {v}m/s at {ang}°. Horizontal range?", [r, 23.0, 32.0, 63.0], r

def q_momentum_collision():
    mc, mv, vva, vca = 580, 1200, 6.20, -1.60
    uc = (mv * vva + mc * vca) / mc
    return f"{mc}kg car hits stationary {mv}kg van. Van v={vva}, car recoils at {abs(vca)}. Initial car speed?", [uc, 5.43, 11.2, 14.4], uc

def q_young_modulus_theory():
    return "Wire X has 3x length and 0.5x diameter of wire Y (same material). Young Modulus of X?", ["E", "0.25E", "6E", "12E"], "E"

def q_wire_extension_ratio():
    return "Wire X has 2x length and 2x radius of W. Same load/material. If W extends $e$, X extends?", ["0.5e", "e", "0.25e", "2e"], "0.5e"

# -- ELECTRICITY --
def q_led_resistor():
    emf, ri, vled, cur = 5, 10, 1.8, 0.020
    r = ((emf - vled) / cur) - ri
    return f"Battery (5V, 10Ω) powers LED (1.8V, 20mA). Series resistor R needed?", [r, 80.0, 160.0, 150.0], r

def q_parallel_resistors():
    return "As $n$ identical resistors in parallel increase, total resistance $R_n$?", ["Decreases non-linearly", "Decreases linearly", "Increases linearly", "Increases non-linearly"], "Decreases non-linearly"

def q_wire_parallel():
    return "Wire P has $R$. Wire Q is 1/4 length, 2x area. Total parallel resistance?", ["R/9", "R/3", "2R/3", "3R/2"], "R/9"

def q_ion_flow():
    i = 0.64
    ans = (i * 60) / (2 * 1.6e-19)
    return f"Doubly-charged ion flow at {i}A. Ions passing in 1.0 min?", [ans, 2e18, 4e18, 1.2e20], ans

def q_battery_discharge():
    p, v, cap = 0.2, 3.7, 9400
    h = (cap / (p / v)) / 3600
    return f"Phone {p*1000}mW, {v}V battery, {cap}C capacity. Hours until empty?", [h, 2, 48, 140], h

def q_putty_resistors():
    return "Resistor Y has 2x diameter of X. Same length/material. Y is $R$. Total series resistance?", ["5R", "4R", "3R", "4R/5"], "5R"

def q_voltmeter_ideal():
    return "Ideal position and resistance for a voltmeter?", ["In parallel with infinite resistance", "In series with zero resistance", "In parallel with zero resistance", "In series with infinite resistance"], "In parallel with infinite resistance"

# -- SHM --
def q_shm_phase():
    return "Phase difference between displacement and acceleration in SHM?", ["π rad", "0", "π/2 rad", "π/4 rad"], "π rad"

def q_shm_ke():
    m, amp, f = 0.15, 0.055, 0.80
    ke = 0.5 * m * (2 * math.pi * f * amp)**2
    return f"{m}kg mass in SHM (Amp {amp*1000}mm, Freq {f}Hz). Max KE?", [ke, 5.7e-3, 0.57, 11], ke

def q_graph_ep():
    return "Graph of Gravitational Potential Energy ($E_p$) vs displacement ($s$) for a pendulum?", ["Parabola opening upwards", "V-shape", "Straight line", "Inverted Parabola"], "Parabola opening upwards"

# --- 2. INTERFACE & LOGIC ---

st.set_page_config(page_title="AQA Physics Master Trainer")
st.title("⚛️ AQA Physics Paper 1: Infinite Trainer")

# All 31 functions in the list
topics = [
    q_quark_composition, q_specific_charge_n, q_fluoride_ion, q_annihilation, q_photoelectric, 
    generate_photon_q, q_de_broglie_speed, q_refractive_index, q_first_harmonic, 
    q_diffraction_grating, q_ultrasound_xray, q_double_slit_cover, q_rocket_thrust, 
    q_projectile_time, q_spring_extension, q_resultant_force, q_graph_features, 
    q_projectile_dist, q_momentum_collision, q_young_modulus_theory, q_wire_extension_ratio, 
    q_led_resistor, q_parallel_resistors, q_wire_parallel, q_ion_flow, q_battery_discharge, 
    q_putty_resistors, q_voltmeter_ideal, q_shm_phase, q_shm_ke, q_graph_ep
]

if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(topics)()
    st.session_state.start_time = time.time()

text, opts, correct = st.session_state.current_q

st.subheader("Question:")
st.write(text)

# --- TIMER ---
timer_placeholder = st.empty()
elapsed = time.time() - st.session_state.start_time
seconds_left = 60 - int(elapsed)

if seconds_left > 0:
    timer_placeholder.metric("Time Remaining", f"{seconds_left}s")
    time.sleep(1)
    st.rerun()
else:
    timer_placeholder.error("⏰ Time's up! Speed is key for Section C.")

# --- THE ANSWER BOX (Multiple Choice) ---
user_choice = st.radio(
    "Select your answer:", 
    opts, 
    format_func=lambda x: f"{x:.2e}" if isinstance(x, (float, int)) and not isinstance(x, bool) and (abs(x) > 1000 or (0 < abs(x) < 0.01)) else x
)

if st.button("Check Answer"):
    if user_choice == correct:
        st.success("🎯 Correct! Keep it up.")
    else:
        st.error(r"❌ Incorrect. Check your math.")
        st.info(f"The correct answer was: {correct}")

st.divider()

if st.button("Next Random Question"):
    st.session_state.current_q = random.choice(topics)()
    st.session_state.start_time = time.time()
    st.rerun()
