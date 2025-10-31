# Quantum Algorithm and Computational Methods
# Program: Deutsch–Jozsa Algorithm (n=4) for a balanced function f(x)=x0⊕x1⊕x2⊕x3

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from IPython.display import display

def deutsch_jozsa_balanced(n=4, shots=1024):
    """
    Implements the Deutsch–Jozsa algorithm for n input qubits
    using a balanced oracle f(x) = x0 XOR x1 XOR ... XOR x_{n-1}
    """
    # Total qubits = n input + 1 ancilla
    qc = QuantumCircuit(n + 1, n)

    # Step 1: Initialize the ancilla qubit in |1⟩
    qc.x(n)

    # Step 2: Apply Hadamard gates to all qubits
    qc.h(range(n + 1))

    # --- Oracle for f(x)=x0⊕x1⊕x2⊕x3 ---
    # Implemented by CNOT from each input qubit to the ancilla
    for i in range(n):
        qc.cx(i, n)
    # --- End of Oracle ---

    # Step 3: Apply Hadamard to input qubits
    qc.h(range(n))

    # Step 4: Measure input qubits
    qc.measure(range(n), range(n))

    # Simulation
    sim = AerSimulator()
    result = sim.run(qc, shots=shots).result()
    counts = result.get_counts()

    # Display
    print(f"Deutsch–Jozsa Algorithm for Balanced Function (n={n})")
    display(qc.draw('mpl'))
    display(plot_histogram(counts))

    # Interpretation
    print("\nMeasurement counts (input qubits):")
    print(counts)
    print("\nExpected Result: Multiple outcomes (not only 0000) → Oracle is balanced.")

# Run the algorithm
deutsch_jozsa_balanced(n=4, shots=1024)

