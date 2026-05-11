import streamlit as st
import random
import math

# --- 1. QUESTION TEMPLATES (The "Engine") ---

# -- PARTICLES & RADIATION --
def generate_photon_q():
    wavelength_nm = random.randint(380, 750) 
    wavelength_m = wavelength_nm * 1e-9
    h, c_correct = 6.63e-34, 3.00e8
    energy_j = (h * c_correct) / wavelength_m
    options = [energy_j, (h * wavelength_m) / c_correct, (h * c_correct) / wavelength_nm, energy_j * 1.6e-19]
    return f"Calculate the energy of a photon with a wavelength of {wavelength_nm} nm.", options, energy_j

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
    f = (m_muon * c**2) / h
    return "Two gamma photons are produced via muon-antimuon annihilation. What is the minimum frequency of the radiation?", [f, f/2, 2.55e22, 5.10e16], f

def q_photoelectric():
    question = "A beam of light of wavelength $\lambda$ is incident on a metal surface. The wavelength is halved but energy incident per second is kept the same. What happens to the Max KE and the number of photoelectrons emitted per second?"
    options = ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"]
    return question, options, "Max KE Increases, Rate Decreases"

def q_de_broglie_speed():
    m_p, m_e, v_p = 1.67e-27, 9.11e-31, 2.8e4
    v_e = (m_p * v_p) / m_e
    return f"Electrons have the same de Broglie wavelength as protons moving at {v_p:.1e} m/s. What is the speed of the electrons?", [v_e, v_p, 1.2e6, 5.1e7], v_e

# -- WAVES & OPTICS --
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

# -- MECHANICS & MATERIALS --
def q_graph_features():
    question = "Which row gives two features of graphs that provide the same information?"
    options = ["Gradient of v-t / Area under a-t", "Gradient of s-t / Area under v-t", "Gradient of v-t / Area under s-t", "Gradient of s-t / Area under a-t"]
    return question, options, "Gradient of v-t / Area under a-t"

def q_rocket_thrust():
    m, a, g = 12000, 1.4, 9.81
    thrust = m * (g + a)
    return f"A rocket of mass {m} kg accelerates upwards at {a} m/s². What is the thrust?", [thrust, 1.7e4, 1.0e5, 1.6e5], thrust

def q_projectile_dist():
    v, angle, g = 25, 42, 9.81
    range_val = (v**2 * math.sin(math.radians(2 * angle))) / g
    return f"A projectile is launched at {v} m/s at {angle}° to the horizontal. What is the horizontal distance when it hits the ground?", [range_val, 23.0, 32.0, 63.0], range_val

def q_projectile_time():
    v, angle, g = 25, 35, 9.81
    t = (2 * v * math.sin(math.radians(angle))) / g
    return f"A projectile is launched at {v} m/s at {angle}° to the horizontal. How long until it hits the ground?", [t, 1.5, 2.1, 4.2], t

def q_momentum_collision():
    m_c, m_v, v_v_after, v_c_after = 580, 1200, 6.20, -1.60
    u_c = (m_v * v_v_after + m_c * v_c_after) / m_c
    return f"A {m_c}kg car hits a stationary {m_v}kg van. Van moves at {v_v_after} m/s, car recoils at {abs(v_c_after)} m/s. Initial car speed?", [u_c, 5.43, 11.2, 14.4], u_c

def q_young_modulus_theory():
    return "A wire has Young modulus $E$. A second wire of the same material has 3x length and 0.5x diameter. What is its Young modulus?", ["E", "0.25E", "6E", "12E"], "E"

def q_resultant_force():
    return "Which combination of coplanar forces can NEVER produce a resultant force of zero?", ["3N, 6N, 10N", "3N, 4N, 5N", "8N, 8N, 8N", "2N, 10N, 10N"], "3N, 6N, 10N"

def q_spring_extension():
    weight, dist_p, length, k = 18, 0.65, 0.80, 240
    f_q = (weight * dist_p) / length
    ext = f_q / k
    return f"A {weight}N sign is {length}m long. Center of mass is {dist_p}m from spring P. If $k = {k}$ N/m, find extension of spring Q.", [ext, 0.014, 0.038, 0.049], ext

def q_wire_extension_ratio():
    return "Wire X has 2x the length and 2x the radius of Wire W. Same material, same load. If W extends by $e$, what is the extension of X?", ["0.5e", "e", "0.25e", "2e"], "0.5e"

# -- ELECTRICITY --
def q_led_resistor():
    emf, r_int, v_led, i = 5, 10, 1.8, 0.020
    r_ext = ((emf - v_led) / i) - r_int
    return f"Battery (5V, 10Ω internal) powers an LED (1.8V, 20mA). What is the value of resistor R needed in series?", [r_ext, 80.0, 160.0, 150.0], r_ext

def q_parallel_resistors():
    return "As the number of identical resistors $n$ in parallel increases, how does the total resistance $R_n$ change?", ["Decreases non-linearly", "Decreases linearly", "Increases linearly", "Increases non-linearly"], "Decreases non-linearly"

def q_wire_parallel():
    return "Wire P has resistance $R$. Wire Q has 1/4 the length and 2x the area. What is the total resistance if connected in parallel?", ["R/9", "R/3", "2R/3", "3R/2"], "R/9"

def q_ion_flow():
    current, ions_charge = 0.64, 2 * 1.6e-19
    ions = (current * 60) / ions_charge
    return f"A gas of doubly-charged ions flows at {current}A. How many ions pass a point in 1.0 minute?", [ions, 2e18, 4e18, 1.2e20], ions

def q_battery_discharge():
    p, v, capacity = 0.200, 3.7, 9400
    hours = (capacity / (p / v)) / 3600
    return f"A phone uses {p*1000}mW with a {v}V battery (capacity {capacity}C). Hours to discharge?", [hours, 2, 48, 140], hours

def q_putty_resistors():
    return "Two resistors X and Y are in series. Diameter of Y is 2x X. Lengths are equal. Resistance of Y is $R$. Total resistance?", ["5R", "4R", "3R", "4R/5"], "5R"

def q_voltmeter_ideal():
    return "Which row gives the ideal position and resistance for a voltmeter?", ["In parallel with infinite resistance", "In series with zero resistance", "In parallel with zero resistance", "In series with infinite resistance"], "In parallel with infinite resistance"

# -- FURTHER MECHANICS (SHM) --
def q_shm_phase():
    return "In SHM, what is the phase difference between displacement and acceleration?", ["π rad", "0", "π/2 rad", "π/4 rad"], "π rad"

def q_shm_ke():
    m, amp, freq = 0.15, 0.055, 0.80
    ke = 0.5 * m * (2 * math.pi * freq * amp)**2
    return f"A {m}kg mass oscillates in SHM (Amp {amp*1000}mm, Freq {freq}Hz). Max KE?", [ke, 5.7e-3, 0.57, 11], ke

def q_graph_ep():
    return "Which graph shows Gravitational Potential Energy ($E_p$) vs displacement ($s$) for a pendulum?", ["Parabola opening upwards", "V-shape", "Straight line", "Inverted Parabola"], "Parabola opening upwards"

# --- 2. INTERFACE ---
st.set_page_config(page_title="AQA Physics Master Trainer")
st.title("🚀 AQA Physics Paper 1: Complete Practice")

topics = [
    generate_photon_q, q_specific_charge_n, q_fluoride_ion, q_annihilation, q_photoelectric, 
    q_de_broglie_speed, q_ultrasound_xray, q_first_harmonic, q_double_slit_cover, 
    q_diffraction_grating, q_refractive_index, q_graph_features, q_rocket_thrust, 
    q_projectile_dist, q_projectile_time, q_momentum_collision, q_young_modulus_theory, 
    q_resultant_force, q_spring_extension, q_wire_extension_ratio, q_led_resistor, 
    q_parallel_resistors, q_wire_parallel, q_ion_flow, q_battery_discharge, 
    q_putty_resistors, q_voltmeter_ideal, q_shm_phase, q_shm_ke, q_graph_ep
]

if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(topics)()

text, opts, correct = st.session_state.current_q
st.subheader("Question:")
st.write(text)

user_choice = st.radio("Select Answer:", opts, format_func=lambda x: f"{x:.2e}" if isinstance(x, float) and (abs(x) > 1000 or abs(x) < 0.01) else x)

if st.button("Check Answer"):
    if user_choice == correct:
        st.success("🎯 Correct!")
    else:
        st.error(f"❌ Incorrect. The answer was {correct}")

st.divider()
if st.button("Next Random Question"):
    st.session_state.current_q = random.choice(topics)()
    st.rerun()
