import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class BioelectricTissueSimulator:
    """
    A continuous bioelectric cellular automaton modeling morphogenetic field repair,
    simulating gap junction voltage diffusion and anatomical memory restoration.
    """
    def __init__(self, grid_size: int = 50, diffusion_rate: float = 0.15):
        self.grid_size = grid_size
        self.dt = diffusion_rate
        
        # Initialize tissue layers
        self.v_mem = np.zeros((grid_size, grid_size)) 
        self.target_morphology = np.zeros((grid_size, grid_size)) 
        self.cellular_identity = np.ones((grid_size, grid_size))
        
        # Run initialization
        self._initialize_target_geometry()

    def _initialize_target_geometry(self):
        """
        Defines the global morphogenetic target memory template. 
        Models a distinct structural 'organ' in the center of the bioelectric field.
        """
        pad = self.grid_size // 4
        self.target_morphology[pad:-pad, pad:-pad] = 1.0
        self.v_mem = np.copy(self.target_morphology) * -70.0 # Target -70mV resting potential

    def execute_amputation(self, start_xy: tuple, end_xy: tuple):
        """
        Simulates a severe mechanical injury or tissue amputation.
        Severely alters local bioelectric communication by destroying cellular nodes.
        """
        x1, y1 = start_xy
        x2, y2 = end_xy
        print(f"[INJURY EVENT] Amputating tissue slice from coordinate ({x1},{y1}) to ({x2},{y2}).")
        
        self.cellular_identity[x1:x2, y1:y2] = 0.0
        self.v_mem[x1:x2, y1:y2] = 0.0 

    def update_bioelectric_step(self):
        """
        Executes one clock cycle of intercellular gap junction diffusion 
        and top-down bioelectric error-gradient correction loops.
        """
        next_v = np.copy(self.v_mem)
        
        # 1. Simulate Intercellular Gap Junction Diffusion (Discrete Laplacian computation)
        for x in range(1, self.grid_size - 1):
            for y in range(1, self.grid_size - 1):
                if self.cellular_identity[x, y] == 1.0: 
                    laplacian = (self.v_mem[x+1, y] + self.v_mem[x-1, y] + 
                                 self.v_mem[x, y+1] + self.v_mem[x, y-1] - 4 * self.v_mem[x, y])
                    next_v[x, y] += self.dt * laplacian
        
        # 2. Compute the Local-to-Global Morphogenetic Error Gradient
        for x in range(1, self.grid_size - 1):
            for y in range(1, self.grid_size - 1):
                if self.cellular_identity[x, y] == 0.0: 
                    neighbor_voltage_sum = (self.v_mem[x+1, y] + self.v_mem[x-1, y] + 
                                            self.v_mem[x, y+1] + self.v_mem[x, y-1])
                    
                    if neighbor_voltage_sum < -35.0: 
                        self.cellular_identity[x, y] = 1.0
                        next_v[x, y] = -70.0 

        self.v_mem = next_v

    def run_simulation_animation(self, total_steps: int = 120):
        """
        Renders the active simulation, tracking the dynamic transformation
        from injury through collective morphogenetic self-repair.
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        im_volts = ax1.imshow(self.v_mem, cmap='viridis', origin='lower', vmin=-70, vmax=0)
        ax1.set_title("Tissue Bioelectric Profile ($V_{mem}$)")
        fig.colorbar(im_volts, ax=ax1, label="Membrane Potential (mV)")
        
        im_morph = ax2.imshow(self.cellular_identity, cmap='bone', origin='lower', vmin=0, vmax=1)
        ax2.set_title("Anatomical Tissue Geometry")
        
        def animate(frame):
            self.update_bioelectric_step()
            im_volts.set_array(self.v_mem)
            im_morph.set_array(self.cellular_identity)
            return [im_volts, im_morph]

        ani = animation.FuncAnimation(fig, animate, frames=total_steps, interval=50, blit=True, repeat=False)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    tissue = BioelectricTissueSimulator(grid_size=60, diffusion_rate=0.2)
    tissue.execute_amputation(start_xy=(25, 25), end_xy=(42, 42))
    tissue.run_simulation_animation(total_steps=100)
