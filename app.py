import streamlit as st
import numpy as np
from typing import List, Tuple

# Page configuration
st.set_page_config(
    page_title="Matrix Chain Multiplication",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for purple theme
st.markdown("""
    <style>
        :root {
            --primary-purple: #7c3aed;
            --light-purple: #ddd6fe;
            --dark-purple: #5b21b6;
            --accent-purple: #a78bfa;
        }
        
        .main {
            background: linear-gradient(135deg, #f5f3ff 0%, #faf5ff 100%);
        }
        
        .stButton > button {
            background: linear-gradient(90deg, #7c3aed 0%, #a855f7 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            background: linear-gradient(90deg, #6d28d9 0%, #9333ea 100%);
            box-shadow: 0 4px 12px rgba(124, 58, 237, 0.4);
        }
        
        .metric-container {
            background: linear-gradient(135deg, #ede9fe 0%, #f3e8ff 100%);
            border-left: 4px solid #7c3aed;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        }
        
        .result-box {
            background: linear-gradient(135deg, #ddd6fe 0%, #e9d5ff 100%);
            border: 2px solid #7c3aed;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }
        
        .section-header {
            color: #5b21b6;
            border-bottom: 3px solid #a78bfa;
            padding-bottom: 10px;
            font-size: 24px;
            font-weight: bold;
        }
        
        .info-box {
            background: linear-gradient(135deg, #f3e8ff 0%, #faf5ff 100%);
            border-left: 4px solid #a855f7;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1 style='color: #5b21b6; font-size: 48px;'>⚙️ Matrix Chain Multiplication</h1>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #7c3aed;'>Algorithm Info</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class='info-box'>
    <b>Matrix Chain Multiplication</b> finds the most efficient way to multiply a sequence of matrices by determining the optimal parenthesization.
    
    <b>Time Complexity:</b> O(n³)
    <b>Space Complexity:</b> O(n²)
    </div>
    """, unsafe_allow_html=True)

def matrix_chain_multiplication(dimensions: List[int]) -> Tuple[int, List[List[int]], List[List[int]]]:
    """
    Calculate minimum number of scalar multiplications needed and return split table.
    
    Args:
        dimensions: List of dimensions (e.g., [10, 20, 30] for matrices 10x20, 20x30)
    
    Returns:
        Tuple of (minimum multiplications, DP table m, split table s)
    """
    n = len(dimensions) - 1
    
    # Create DP and split tables
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    
    # For chain length
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i-1][j-1] = float('inf')
            
            for k in range(i, j):
                cost = m[i-1][k-1] + m[k][j-1] + dimensions[i-1] * dimensions[k] * dimensions[j]
                if cost < m[i-1][j-1]:
                    m[i-1][j-1] = cost
                    s[i-1][j-1] = k
    
    return int(m[0][n - 1]), m, s


def build_parenthesization(s: List[List[int]], i: int, j: int) -> str:
    """Return optimal parenthesization as a string for matrices M(i+1)..M(j+1).

    s is the split table as produced by matrix_chain_multiplication. Indices i and j are 0-based.
    """
    if i == j:
        return f"M{i+1}"
    k = s[i][j]  # k is 1-based split index
    left = build_parenthesization(s, i, k-1)
    right = build_parenthesization(s, k, j)
    return f"({left}{right})"

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("<div class='section-header'>📊 Input Configuration</div>", unsafe_allow_html=True)
    
    num_matrices = st.slider(
        "Number of Matrices",
        min_value=2,
        max_value=5,
        value=4,
        step=1,
        key="num_matrices"
    )
    
    st.markdown("<div class='info-box'><b>Enter dimensions:</b> For n matrices, you need n+1 dimension values. For example, for 3 matrices: (10×20)·(20×30)·(30×40), enter [10, 20, 30, 40]</div>", unsafe_allow_html=True)
    
    # Input dimensions
    dimensions = []
    cols = st.columns(num_matrices + 1)
    
    for i in range(num_matrices + 1):
        with cols[i]:
            if i == 0:
                dim = st.number_input(f"p[{i}]", value=10, min_value=1, step=1, key=f"dim_{i}")
            else:
                dim = st.number_input(f"p[{i}]", value=10 + i*10, min_value=1, step=1, key=f"dim_{i}")
            dimensions.append(dim)

with col2:
    st.markdown("<div class='section-header'>ℹ️ Matrix Details</div>", unsafe_allow_html=True)
    
    for i in range(num_matrices):
        matrix_info = f"Matrix M{i+1}: {dimensions[i]} × {dimensions[i+1]}"
        st.markdown(f"""
        <div class='metric-container'>
            <b>Matrix {i+1}:</b><br>
            Dimensions: {dimensions[i]} × {dimensions[i+1]}
        </div>
        """, unsafe_allow_html=True)

# Calculate button
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🔢 Calculate Optimal Solution", use_container_width=True):
        with st.spinner("Computing optimal parenthesization..."):
            min_multiplications, dp_table, splits = matrix_chain_multiplication(dimensions)
        
        st.markdown("<div class='section-header'>✅ Results</div>", unsafe_allow_html=True)
        
        # Result
        st.markdown(f"""
        <div class='result-box'>
            <h2 style='color: #5b21b6; margin: 0;'>Minimum Scalar Multiplications</h2>
            <h1 style='color: #7c3aed; margin: 10px 0; font-size: 48px;'>{min_multiplications:,}</h1>
            <p style='color: #6d28d9; margin: 0;'>This is the optimal number of multiplications needed</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Optimal parenthesization sequence
        n = len(dimensions) - 1
        sequence = build_parenthesization(splits, 0, n-1) if n > 0 else ''
        st.markdown("<div class='section-header'>🔗 Optimal Parenthesization</div>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class='info-box'>
            <b>Sequence:</b> <code>{sequence}</code>
        </div>
        """, unsafe_allow_html=True)
        
        # Show DP table
        st.markdown("<div class='section-header'>📋 DP Table (m[i][j] values)</div>", unsafe_allow_html=True)
        
        df_data = {}
        
        for i in range(n):
            row_values = []
            for j in range(n):
                if i <= j:
                    row_values.append(int(dp_table[i][j]) if dp_table[i][j] != float('inf') else '∞')
                else:
                    row_values.append('-')
            df_data[f'M{i+1}'] = row_values
        
        cols_names = [f'M{j+1}' for j in range(n)]
        

        # Build rows as list of dicts and display with Streamlit table to avoid pandas dependency
        table_rows = []
        for r in range(n):
            row = {col: df_data[col][r] for col in df_data}
            row['Matrix'] = cols_names[r]
            table_rows.append(row)
        
        # Ensure Matrix column appears first
        cols_order = ['Matrix'] + list(df_data.keys())
        st.table([{k: row[k] for k in cols_order} for row in table_rows])
        
        # Algorithm explanation
        st.markdown("<div class='section-header'>📖 Algorithm Steps</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='info-box'>
        <b>Step 1:</b> Initialize DP table with base cases (single matrices require 0 multiplications)<br><br>
        
        <b>Step 2:</b> For each chain length from 2 to {num_matrices}:<br>
        - Calculate minimum cost by trying all possible split points<br>
        - Formula: cost = m[i][k] + m[k+1][j] + p[i-1] × p[k] × p[j]<br><br>
        
        <b>Step 3:</b> The value at m[0][{num_matrices-1}] gives the minimum multiplications<br><br>
        
        <b>Result:</b> <span style='color: #7c3aed; font-weight: bold;'>{min_multiplications:,}</span> scalar multiplications needed
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding: 20px; border-top: 2px solid #a78bfa;'>
        <p style='color: #7c3aed;'>Design & Analysis of Algorithms | Matrix Chain Multiplication Problem</p>
    </div>
""", unsafe_allow_html=True)

