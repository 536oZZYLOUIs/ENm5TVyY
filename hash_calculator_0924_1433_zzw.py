# 代码生成时间: 2025-09-24 14:33:04
import streamlit as st
def calculate_hash(input_string, hash_type):
    """Calculates the hash of the input string based on the provided hash type."""
    try:
        if hash_type == 'MD5':
            return hashlib.md5(input_string.encode()).hexdigest()
        elif hash_type == 'SHA1':
            return hashlib.sha1(input_string.encode()).hexdigest()
        elif hash_type == 'SHA256':
            return hashlib.sha256(input_string.encode()).hexdigest()
        else:
            raise ValueError("Unsupported hash type.")
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    """Main function to handle the Streamlit app logic."""
    st.title('Hash Calculator Tool')
    """Input Text Area"""
    input_string = st.text_area("Enter text to calculate hash:", "")
    """Hash Type Selection"""
    hash_type = st.selectbox(
        "Choose the hash type:",
        ["MD5", "SHA1", "SHA256"],
        index=0
    )
    """Calculate and Display the Hash"""
    if st.button('Calculate Hash'):
        result = calculate_hash(input_string, hash_type)
        st.text_area("Hash Result:", result, height=5)

def run():
    """Runs the Streamlit app."""
    main()
"""Streamlit entry point."""
if __name__ == '__main__':
    run()