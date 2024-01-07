from simulations import ProjectileMotion
import matplotlib.pyplot as plt

simulation = ProjectileMotion(y_init=10, v_init=20, theta=60, time=4)
simulation.run_simulation()
results = simulation.get_results()

position_x = results.get("position_x", None)
position_y = results.get("position_y", None)

plt.scatter(position_x, position_y)
plt.show()