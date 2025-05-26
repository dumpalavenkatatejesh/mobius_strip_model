import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson 
from mpl_toolkits.mplot3d import Axes3D

class MobiusStrip:
    def __init__(self, R=1.0, w=0.2, n=200):
        self.R = R
        self.w = w
        self.n = n
        self.u, self.v = np.meshgrid(
            np.linspace(0, 2 * np.pi, n),
            np.linspace(-w/2, w/2, n)
        )
        self.x, self.y, self.z = self._compute_coordinates()

    def _compute_coordinates(self):
        u = self.u
        v = self.v
        x = (self.R + v * np.cos(u / 2)) * np.cos(u)
        y = (self.R + v * np.cos(u / 2)) * np.sin(u)
        z = v * np.sin(u / 2)
        return x, y, z

    def plot(self):
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.x, self.y, self.z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
        ax.set_title("Mobius Strip")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()

    def surface_area(self):
        # Calculate derivatives
        dx_du, dx_dv = np.gradient(self.x, axis=(0, 1))
        dy_du, dy_dv = np.gradient(self.y, axis=(0, 1))
        dz_du, dz_dv = np.gradient(self.z, axis=(0, 1))

        # Cross product of partial derivatives
        cross_x = dy_du * dz_dv - dz_du * dy_dv
        cross_y = dz_du * dx_dv - dx_du * dz_dv
        cross_z = dx_du * dy_dv - dy_du * dx_dv

        area_density = np.sqrt(cross_x**2 + cross_y**2 + cross_z**2)

        # Numerical integration using simpsonon's rule
        area = simpson([simpson(row, self.v[0]) for row in area_density], self.u[:, 0])
        return area

    def edge_length(self):
        # Evaluate only at v = ±w/2 (strip edge)
        u_vals = np.linspace(0, 2 * np.pi, self.n)
        v_edge = self.w / 2

        # Parametric equations for edge
        x_edge = (self.R + v_edge * np.cos(u_vals / 2)) * np.cos(u_vals)
        y_edge = (self.R + v_edge * np.cos(u_vals / 2)) * np.sin(u_vals)
        z_edge = v_edge * np.sin(u_vals / 2)

        # Compute differential arc length
        dx = np.gradient(x_edge)
        dy = np.gradient(y_edge)
        dz = np.gradient(z_edge)

        ds = np.sqrt(dx**2 + dy**2 + dz**2)
        length = simpson(ds, u_vals)
        return 2 * length  # Both edges
    
R = float(input("Enter radius R (e.g., 1.0): "))
w = float(input("Enter strip width w (e.g., 0.3): "))
n = int(input("Enter resolution n (e.g., 200): "))

strip = MobiusStrip(R=R, w=w, n=n)
print(f"\n🟢 Surface Area: {strip.surface_area():.4f}")
print(f"🔵 Edge Length: {strip.edge_length():.4f}\n")
strip.plot()
