# 代码生成时间: 2025-10-04 18:22:43
import streamlit as st
import psutil
from datetime import datetime

"""
Network Traffic Monitor using Streamlit and Psutil.
This application will monitor and display network traffic statistics.
"""

# Function to get network statistics
def get_network_stats():
    net_io = psutil.net_io_counters(pernic=True)
    stats = {
        'Received Bytes': net_io['eth0'].bytes_recv,
        'Transmitted Bytes': net_io['eth0'].bytes_sent
    }
    return stats

# Streamlit layout
def main():
    st.title('Network Traffic Monitor')

    # Get current stats
    stats = get_network_stats()

    # Display statistics
    st.write(f"Received Bytes: {stats['Received Bytes']}")
    st.write(f"Transmitted Bytes: {stats['Transmitted Bytes']}")

    # Timer for updating stats
    if 'timer' in st.session_state:
        st.session_state.timer -= 1
    else:
        st.session_state.timer = 5  # 5 seconds timer

    if st.session_state.timer == 0:
        stats = get_network_stats()
        st.write(f"Received Bytes: {stats['Received Bytes']}")
        st.write(f"Transmitted Bytes: {stats['Transmitted Bytes']}")
        st.session_state.timer = 5

    # Button to clear stats
    if st.button('Clear Stats'):
        psutil.net_io_counters(pernic=True)  # Resets the counters
        st.experimental_rerun()  # Reruns the app to refresh stats

if __name__ == '__main__':
    main()