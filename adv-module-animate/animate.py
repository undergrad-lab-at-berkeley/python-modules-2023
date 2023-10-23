import compute
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np

def animate_positions(time, pos, save=False):
    '''
    Makes an animation depicting the positions returned by compute.simulate.
    Implemented in the Matplotlib docs (slightly differently than how we're doing it) here: 
    https://matplotlib.org/gallery/animation/double_pendulum.html

    Arguments
    ---------
    time : np.ndarray, (num_steps)
    The array of times returned by compute.simulate.

    pos : np.ndarray, (num_steps, N, 2)
    The array of positions returned by compute.simulate.
    '''
    dt = min(np.diff(time))

    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(np.min(pos[:,:,0])-0.1, np.max(pos[:,:,0])+0.1), ylim=(np.min(pos[:,:,1])-0.1, np.max(pos[:,:,1])+0.1))
    ax.set_aspect('equal')
    ax.grid()

    line, = ax.plot([], [], 'o-', lw=2)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def animate(i):
        thisx = np.hstack(([0], pos[i,:,0]))
        thisy = np.hstack(([0], pos[i,:,1]))

        line.set_data(thisx, thisy)
        time_text.set_text(time_template % (i*dt))
        return line, time_text

    ani = animation.FuncAnimation(
        fig, animate, len(time), interval=dt*1000, blit=True)

    if save:
        writervideo = animation.FFMpegWriter(fps=300) 
        ani.save('double_pendulum.mp4', writer=writervideo)

    plt.show()

if __name__ == "__main__":
    N = 2
    if N == 1:
        angles_init = np.pi / 180 * np.array([30])
        lengths = np.array([1])
        masses = np.array([0.1])
    elif N == 2:
        angles_init = np.pi / 180 * np.array([85, -15])
        lengths = np.array([1, 1])
        masses = np.array([1, 1])

    times, positions = compute.simulate(angles_init, lengths, masses, dt=0.01, num_steps=10000)
    animate_positions(times, positions, save=False)
