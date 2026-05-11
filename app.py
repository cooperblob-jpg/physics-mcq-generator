import streamlit as st
import random
import math
import time

# --- 1. QUESTION TEMPLATES (The "Engine") ---

def generate_photon_q():
    wavelength_nm = random.randint(380, 750) 
    wavelength_m = wavelength_nm * 1e-9
    h, c_correct = 6.63e-34, 3.00e8
    energy_j = (h * c_correct) / wavelength_m
    options = [energy_j, (h * wavelength_m) / c_correct, (h * c_correct) / wavelength_nm, energy_j * 1.6e-19]
    return f"Calculate the energy of a photon with a wavelength of {wavelength_nm} nm.", options, energy_j

def q_quark_composition():
    particles = {
        "Proton": "uud",
        "Neutron": "udd",
        "$\pi^+$ meson": "u anti-d",
        "$\pi^-$ meson": "anti-u d",
        "$K^+$ meson": "u anti-s",
        "$K^-$ meson": "anti-u s",
        "$K^0$ meson": "d anti-s"
    }
    name, correct = random.choice(list(particles.items()))
    distractors = ["uus", "ddd", "u anti-u", "d anti-d"]
    options = list(set([correct] + random.sample(distractors, 3)))
    return f"What is the quark composition of a {name}?", options, correct

def q_specific_charge_n():
    protons, mass_num = 7, 16
    electrons_gained = 3
    total_mass = mass_num * 1.67e-27
    net_charge = electrons_gained * -1.60e-19
    ans = net_charge / total_mass
    return f"An atom of Nitrogen-16 ($_{{7}}^{{16}}N$) gains {electrons_gained} electrons. What is the specific charge of the ion?", [ans, abs(ans), ans*2, 4.19e7], ans

def q_fluoride_ion():
    q, m = -1.6e-19, 19 * 1.67e-27
    ans = q / m
    return "What is the magnitude of the specific charge of a fluoride ion ($_{9}^{19}F^{-}$)?", [abs(ans), 3.2e-26, 8.4e-21, 5.0e6], abs(ans)

def q_annihilation():
    m_muon, c, h = 1.88e-28, 3e8, 6.63e-34
    f = (m_muon * (c**2)) / h
    return "Two gamma photons are produced via muon-antimuon annihilation. What is the minimum frequency of the radiation?", [f, f/2, 2.55e22, 5.10e16], f

def q_photoelectric():
    question = "A beam of light of wavelength $\lambda$ is incident on a metal surface. The wavelength is halved but energy incident per second is kept the same. What happens to the Max KE and the number of photoelectrons emitted per second?"
    options = ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"]
    return question, options, "Max KE Increases, Rate Decreases"

def q_de_broglie_speed():
    m_p, m_e, v_p = 1.67e-27, 9.11e-31, 2.8e4
    v_e = (m_p * v_p) / m_e
    return f"Electrons have the same de Broglie wavelength as protons moving at {v_p:.1e} m/s. What is the speed of the electrons?", [v_e, v_p, 1.2e6, 5.1e7], v_e

def q_ultrasound_xray():
    question = "Which statement is **not** correct for both ultrasound and X-rays?"
    options = ["Both can be polarised", "Both can be refracted", "Both can be diffracted", "Both can be reflected"]
    return question, options, "Both can be polarised"

def q_first_harmonic():
    question = "A string has length $l$ and diameter $d$. A second string of the same material and tension needs the same first-harmonic frequency. If the diameter is $2d$, what must the length be?"
    return question, ["l/2", "2l", "l", "l/4"], "l/2"

def q_double_slit_cover():
    question = "In a two-slit interference pattern, one slit is covered with opaque black paper. What is the effect?"
    options = ["Fewer maxima are observed", "Intensity of central maximum increases", "Width of central maximum decreases", "Outer maxima become wider"]
    return question, options, "Fewer maxima are observed"

def q_diffraction_grating():
    n, lam, theta = 4, 5.0e-7, 30
    d = (n * lam) / math.sin(math.radians(theta))
    lines_per_mm = (1 / d) / 1000
    return f"Light of wavelength {lam:.1e} m is incident on a grating. The 4th order maximum is at 30°. How many lines per mm?", [lines_per_mm, 1.0e3, 2.5e2, 2.5e5], lines_per_mm

def q_refractive_index():
    numer, denom = 3, 5
    ans = denom / numer
    return f"A wave enters a cable and slows down to {numer}/{denom} of its original speed. What is the refractive index?", [ans, 1.33, 1.50, 0.67], ans

def q_rocket_thrust():
    m, a, g = 12000, 1.4, 9.81
    thrust = m * (g + a)
    return f"A rocket of mass {m} kg accelerates upwards at {a} m/s². What is the thrust?", [thrust, 1.7e4, 1.0e5, 1.6e5], thrust

def q_projectile_time():
    v, angle, g = 25, 35, 9.81
    t = (2 * v * math.sin(math.radians(angle))) / g
    return f"A projectile is launched at {v} m/s at {angle}° to the horizontal. How long until it hits the ground?", [t, 1.5, 2.1, 4.2], t

def q_spring_extension():
    weight, dist_p, length, k = 18, 0.65, 0.80, 240
    f_q = (weight * dist_p) / length
    ext = f_q / k
    return f"A {weight}N sign is {length}m long. Center of mass is {dist_p}m from spring P. If $k = {k}$ N/m, find extension of spring Q.", [ext, 0.014, 0.038, 0.049], ext

def q_led_resistor():
    emf, r_int, v_led, i = 5, 10, 1.8, 0.020
    r_ext = ((emf - v_led) / i) - r_int
    return f"Battery (5V, 10Ω internal) powers an LED (1.8V, 20mA). What is the value of resistor R needed in series?", [r_ext, 80.0, 160.0, 150.0], r_ext

def q_shm_ke():
    m, amp, freq = 0.15, 0.055, 0.80
    ke = 0.5 * m * (2 * math.pi * freq * amp)**2
    return f"A {m}kg mass oscillates in SHM (Amp {amp*1000}mm, Freq {freq}Hz). Max KE?", [ke, 5.7e-3, 0.57, 11], ke

def q_graph_ep():
    return "Which graph shows Gravitational Potential Energy ($E_p$) vs displacement ($s$) for a pendulum?", ["Parabola opening upwards", "V-shape", "Straight line", "Inverted Parabola"], "Parabola opening upwards"

# --- 2. INTERFACE & LOGIC ---

st.set_page_config(page_title="AQA Physics Pro")
st.title("🚀 AQA Physics Paper 1: Master Practice")

topics = [
    generate_photon_q, q_quark_composition, q_specific_charge_n, q_fluoride_ion, 
    q_annihilation, q_photoelectric, q_de_broglie_speed, q_ultrasound_xray, 
    q_first_harmonic, q_double_slit_cover, q_diffraction_grating, q_refractive_index, 
    q_rocket_thrust, q_projectile_time, q_spring_extension, q_led_resistor, 
    q_shm_ke, q_graph_ep
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
    timer_placeholder.error("⏰ Time's up! Speed is key for Paper 1 MCQs.")

# --- SELECTION ---
user_choice = st.radio("Select Answer:", opts, format_func=lambda x: f"{x:.2e}" if isinstance(x, float) and (abs(x) > 1000 or abs(x) < 0.01) else x)

if st.button("Check Answer"):
    if user_choice == correct:
        st.success("🎯 Correct! Well done.")
    else:
        st.error(r"❌ Incorrect. Check your units and formulas.")
        st.info(f"The correct answer was: {correct}")

st.divider()

if st.button("Next Random Question"):
    st.session_state.current_q = random.choice(topics)()
    st.session_state.start_time = time.time()
    st.rerun()
