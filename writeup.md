# Möbius Strip Modeling – Short Write-up

## 🔧 Code Structure

The project is organized around a `MobiusStrip` class in `mobius_strip.py`, which handles:
- Initialization of the Möbius strip parameters (radius `R`, width `w`, resolution `n`)
- Mesh generation using the parametric equations of the Möbius strip
- Numerical computation of surface area using vector calculus and Simpson's rule
- Edge length estimation by integrating arc length along the boundary
- Optional 3D visualization using `matplotlib`

---

## 📐 Mathematical Details

### ✳️ Parametric Equations Used

The Möbius strip is defined by the following parametric equations:

   `x(u, v) = (R + v·cos(u / 2))·cos(u)`
   `y(u, v) = (R + v·cos(u / 2))·sin(u)`
   `z(u, v) = v·sin(u / 2)`
    
Where:
- `u ∈ [0, 2π]` is the angle parameter
- `v ∈ [-w/2, w/2]` is the width parameter
- `R` is the radius (distance from center to strip)
- `w` is the total width of the strip

These equations create a single-sided surface with a 180° twist.

### 🔢 Numerical Methods

To compute the surface area and edge length:

- **Gradient**: Used to compute partial derivatives of the surface (for area calculation).
- **Cross product**: Tangent vectors are crossed to compute the area element at each point.
- **Simpson’s Rule** (`scipy.integrate.simps`): Used for accurate numerical integration over the grid.

---

## 🧮 Surface Area Approximation

1. Compute ∂x/∂u and ∂x/∂v using `np.gradient`
2. Calculate the cross product of the tangent vectors
3. Find the magnitude (area density) of the resulting normal vector
4. Integrate over the parameter domain to estimate total surface area

---

## 📏 Edge Length Estimation

1. Evaluate parametric equations at `v = ±w/2` (strip boundaries)
2. Compute differential arc length `ds = sqrt(dx² + dy² + dz²)`
3. Integrate over `u` using Simpson’s Rule
4. Multiply by 2 (since Möbius strip boundary loops once over 2π)

---

## 🎯 Challenges Faced

- Correctly aligning vector derivatives over a 2D mesh
- Maintaining performance while increasing resolution (`n`)
- Avoiding visual artifacts on the 3D twisted geometry
- Ensuring numerical integration produces stable results

---

## ✅ Outcome

This project demonstrates:
- Accurate modeling of non-orientable surfaces in Python
- Use of vector calculus and numerical integration in geometry
- Clean and modular code structure for scientific computing
