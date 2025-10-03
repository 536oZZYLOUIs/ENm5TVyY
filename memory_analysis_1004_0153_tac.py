# 代码生成时间: 2025-10-04 01:53:20
import streamlit as st
import psutil
import os
from collections import Counter

"""
Streamlit application to analyze memory usage.
"""


@st.cache
def get_memory_usage():
    """
    Get the memory usage details of the system.
    """
    process = psutil.Process(os.getpid())
    mem = process.memory_info()
    return mem.rss  # Resident Set Size


def main():
    """
    Main function to run the Streamlit application.
    """
    st.title('Memory Usage Analysis')
    
    # Cache the memory usage to avoid recalculating on each rerun
    memory_usage = get_memory_usage()
    
    # Display the memory usage
    st.subheader('Memory Usage Details')
    st.write(f"Resident Set Size: {memory_usage / (1024 * 1024):.2f} MB")
    
    # Error handling for unexpected issues
    try:
        # Get the process list and their memory usage
        process_list = psutil.process_iter(['pid', 'name', 'memory_info'])
        processes = []
        for proc in process_list:
            try:
                processes.append((proc.info['pid'], proc.info['name'], proc.info['memory_info'].rss))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        # Sort the processes by memory usage
        processes.sort(key=lambda x: x[2], reverse=True)
        
        # Display the top 10 memory consuming processes
        st.subheader('Top 10 Memory Consuming Processes')
        if processes:
            for i, (pid, name, rss) in enumerate(processes[:10]):
                st.write(f"{i + 1}. {name} (PID: {pid}) - {rss / (1024 * 1024):.2f} MB")
        else:
            st.write('No processes found.')
    except Exception as e:
        st.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()