from tkinter.messagebox import showerror

from scipy import linalg


def sor_solver(A, b, omega, initial_guess, convergence_criteria):
    """
    Arguments:
        A: nxn numpy matrix.
        b: n dimensional numpy vector.
        omega: relaxation factor.
        initial_guess: An initial solution guess for the solver to start with.
        convergence_criteria: The maximum discrepancy acceptable to regard the current solution as fitting.
    Returns:
        phi: solution vector of dimension n.
    """
    try:
        phi = initial_guess[:]
        residual = linalg.norm(A @ phi - b)  # Initial residual
        while residual > convergence_criteria:
            for i in range(A.shape[0]):
                sigma = 0
                for j in range(A.shape[1]):
                    if j != i:
                        sigma += A[i, j] * phi[j]
                phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
            residual = linalg.norm(A @ phi - b)
        return phi
    except ValueError:
        showerror(title="Помилка", message="Даний метод не може розв'язати таку СЛАР!")
        return None
