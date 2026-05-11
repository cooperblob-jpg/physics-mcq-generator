import streamlit as st
import random

st.title("🚀 A-Level Physics MCQ Generator")
st.write("Master your Paper 1 timing with infinite variations.")

# 1. THE PHYSICS ENGINE (A simple template for Photon Energy)
def generate_photon_q():
    # Randomize wavelength in nanometers
    wavelength_nm = random.randint(380, 750) 
    wavelength_m = wavelength_nm * 1e-9
    
    # Constants
    h = 6.63e-34
    c = 3.00e-8 # deliberate mistake trap: should be 3e8
    c_correct = 3.00e8
    
    # Calculate correct answer
    energy_j = (h * c_correct) / wavelength_m
    
    # Generate common traps (distractors)
    trap_1 = (h * wavelength_m) / c_correct  # Wrong formula
    trap_2 = (h * c_correct) / (wavelength_nm) # Forgot 10^-9 conversion
    
    options = [energy_j, trap_1, trap_2, energy_j * 1.6e-19] # Trap 4: Wrong eV conversion
    return wavelength_nm, options, energy_j

# 2. THE WEBSITE INTERFACE
if 'current_q' not in st.session_state:
    st.session_state.current_q = generate_photon_q()

wl, opts, ans = st.session_state.current_q

st.subheader(f"Question: Calculate the energy of a photon with a wavelength of {wl} nm.")
user_choice = st.radio("Select the correct energy (Joules):", opts, format_func=lambda x: f"{x:.2e}")

if st.button("Check Answer"):
    if user_choice == ans:
        st.success("Correct! You spotted the unit conversion.")
    else:
        st.error(f"Not quite. Remember: $E = \\frac{hc}{\\lambda}$ and $\\lambda$ must be in meters.")

if st.button("Generate New Question"):
    st.session_state.current_q = generate_photon_q()
    st.rerun()
