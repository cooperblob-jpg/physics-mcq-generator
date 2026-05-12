import streamlit as st
import random
import math
import time

# --- 1. THE 30 QUESTION TEMPLATES ---

# -- PARTICLES & RADIATION --
def q1():
    particles = {"Proton": "uud", "Neutron": "udd", "$\pi^+$ meson": "u anti-d", "$\pi^-$ meson": "anti-u d", "$K^+$ meson": "u anti-s", "$K^-$ meson": "anti-u s", "$K^0$ meson": "d anti-s"}
    name, correct = random.choice(list(particles.items()))
    return f"Quark composition of a {name}?", [correct, "uus", "ddd", "u anti-u"], correct

def q2():
    w, m, g = 7, random.randint(14, 16), random.randint(1, 3)
    ans = (g * -1.60e-19) / (m * 1.67e-27)
    return f"Specific charge of Nitrogen-{m} with +{g}e charge?", [ans, abs(ans), 4.19e7, 1.2e-8], ans

def q3():
    ans = 1.6e-19 / (19 * 1.67e-27)
    return "Magnitude of specific charge of Fluoride ion ($^{19}F^-$)?", [ans, 3.2e-26, 5.0e6, 8.4e-21], ans

def q4():
    f = (1.88e-28 * (3e8**2)) / 6.63e-34
    return "Min frequency of gamma radiation from muon-antimuon annihilation?", [f, f/2, 5.1e16, 2.5e22], f

def q5():
    return "Halving $\lambda$ while keeping total Power constant does what?", ["Max KE Increases, Rate Decreases", "Max KE Decreases, Rate Increases", "Max KE Increases, Rate Unchanged", "Max KE Decreases, Rate Unchanged"], "Max KE Increases, Rate Decreases"

def q6():
    nm = random.randint(400, 700)
    e = (6.63e-34 * 3e8) / (nm * 1e-9)
    return f"Energy of a {nm}nm photon?", [e, e/1.6e-19, 3.2e-19, 4.5e-25], e

def q7():
    v_p = 2.8e4
    v_e = (1.67e-27 * v_p) / 9.11e-31
    return f"Electron speed if it has same $\lambda_{{db}}$ as a proton at {v_p} m/s?", [v_e, v_p, 1.2e6, 5.1e7], v_e

# -- WAVES & OPTICS --
def q8():
    return f"Wave slows to 3/5 of original speed. Refractive index?", [1.67, 0.6, 1.33, 1.5], 1.67

def q9():
    return "Diameter $d \rightarrow 2d$. What length $L$ keeps the same 1st harmonic frequency?", ["l/2", "2l", "l", "l/4"], "l/2"

def q10():
    return "One slit in a double-slit experiment is covered. Effect?", ["Fewer maxima", "Central max brighter", "Narrower fringes", "No change"], "Fewer maxima"

def q11():
    return "Which can NOT be polarised?", ["Ultrasound", "X-rays", "Radio waves", "Microwaves"], "Ultrasound"

def q12():
    lam = 5e-7
    d = (4 * lam) / math.sin(math.radians(30))
    lpm = (1/d)/1000
    return "4th order max at 30° for 500nm light. Lines per mm?", [lpm, 250, 500, 1000], lpm

# -- MECHANICS --
def q13():
    m, a = 12000, 1.4
    t = m * (9.81 + a)
    return f"Thrust of {m}kg rocket accelerating up at {a}m/s²?", [t, m*a, m*9.81, 1.0e5], t

def q14():
    v, ang = 25, 35
    t = (2 * v * math.sin(math.radians(ang))) / 9.81
    return f"Time of flight for projectile at {v}m/s, {ang}°?", [t, 1.5, 2.9, 4.2], t

def q15():
    v, ang = 25, 42
    r = (v**2 * math.sin(math.radians(2*ang))) / 9.81
    return f"Range of projectile at {v}m/s, {ang}°?", [r, 23.0, 32.0, 63.0], r

def q16():
    return "Which forces can NEVER produce a resultant of zero?", ["3N, 6N, 10N", "3N, 4N, 5N", "8N, 8N, 8N", "2N, 10N, 10N"], "3N, 6N, 10N"

def q17():
    return "Gradient of v-t graph is the same as...?", ["Area under a-t", "Area under s-t", "Gradient of s-t", "Acceleration"], "Area under a-t"

def q18():
    return "Wire X has 3x length, 0.5x diameter of Y. Young Modulus of X?", ["E", "0.25E", "6E", "12E"], "E"

def q19():
    return "Wire W: length $l$, radius $r$. Wire X: $2l$, $2r$. Same load. Extension of X?", ["0.5e", "e", "2e", "4e"], "0.5e"

def q20():
    w, dp, l, k = 18, 0.65, 0.8, 240
    ext = ((w*dp)/l)/k
    return f"Sign {w}N, CoM {dp}m from P. $k={k}$. Extension at Q?", [ext, 0.014, 0.04, 0.05], ext

def q21():
    mc, mv, vva, vca = 580, 1200, 6.2, -1.6
    u = (mv*vva + mc*vca)/mc
    return f"580kg car hits stationary 1200kg van. Van moves at 6.2, car recoils at 1.6. Initial car speed?", [u, 5.4, 11.2, 14.4], u

# -- ELECTRICITY --
def q22():
    return "Ideal voltmeter properties?", ["Parallel, infinite R", "Series, zero R", "Parallel, zero R", "Series, infinite R"], "Parallel, infinite R"

def q23():
    v, ri, vled, i = 5, 10, 1.8, 0.02
    r = ((v-vled)/i)-ri
    return "Battery (5V, 10Ω) powers LED (1.8V, 20mA). Series R needed?", [r, 80, 150, 160], r

def q24():
    i = 0.64
    n = (i*60)/(2*1.6e-19)
    return f"Divalent ion flow at {i}A. Ions passing in 1 min?", [n, 1.2e20, 2.4e20, 4.0e18], n

def q25():
    return "As $n$ parallel resistors increase, total $R$?", ["Decreases non-linearly", "Decreases linearly", "Increases", "Stays same"], "Decreases non-linearly"

def q26():
    return "Wire Q is 1/4 length, 2x area of P. Total parallel R?", ["R/9", "R/5", "2R/3", "R/3"], "R/9"

def q27():
    p, v, cap = 0.2, 3.7, 9400
    h = (cap/(p/v))/3600
    return "Phone 200mW, 3.7V, 9400C. Hours until discharge?", [h, 24, 48, 140], h

def q28():
    return "Series putty X and Y. Y has 2x diameter of X. Y is $R$. Total $R$?", ["5R", "4R", "3R", "2R"], "5R"

# -- SHM --
def q29():
    return "Phase difference between $a$ and $s$ in SHM?", ["π rad", "0", "π/2 rad", "2π rad"], "π rad"

def q30():
    m, amp, f = 0.15, 0.055, 0.8
    ke = 0.5 * m * (2*math.pi*f*amp)**2
    return f"Max KE of {m}kg mass, {amp}m amp, {f}Hz frequency?", [ke, 5.7e-3, 0.57, 11], ke

# --- 2. INTERFACE LOGIC ---

st.set_page_config(page_title="AQA Physics Master")
st.title("⚛️ AQA Physics Paper 1: The 30-Question Gauntlet")

# List containing all 30 functions
topics = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21,q22,q23,q24,q25,q26,q27,q28,q29,q30]

if 'current_q' not in st.session_state:
    st.session_state.current_q = random.choice(topics)()
    st.session_state.start_time = time.time()

text, opts, correct = st.session_state.current_q

st.subheader("Question:")
st.write(text)

# --- ANSWERING SECTION (Must be above timer refresh) ---
user_choice = st.radio("Select Answer:", opts, format_func=lambda x: f"{x:.2e}" if isinstance(x, (float, int)) and not isinstance(x, bool) and (abs(x) > 1000 or (0 < abs(x) < 0.01)) else x)

col1, col2 = st.columns(2)
with col1:
    if st.button("Check Answer"):
        if user_choice == correct:
            st.success("🎯 Correct!")
        else:
            st.error(f"❌ Incorrect. Answer: {correct}")

with col2:
    if st.button("Next Question"):
        st.session_state.current_q = random.choice(topics)()
        st.session_state.start_time = time.time()
        st.rerun()

st.divider()

# --- TIMER (At the bottom) ---
timer_placeholder = st.empty()
seconds_left = 60 - int(time.time() - st.session_state.start_time)

if seconds_left > 0:
    timer_placeholder.metric("Time Remaining", f"{seconds_left}s")
    time.sleep(1)
    st.rerun()
else:
    timer_placeholder.error("⏰ Time's up! Speed it up for Section C.")
