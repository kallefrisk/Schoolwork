from enum import Enum
import gymnasium as gym
from gymnasium import spaces
import pygame
import numpy as np
import torch




class GridWorldEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 24}

    def __init__(self, world: torch.Tensor,
                 terminal_dict: dict,
                 action_map: dict,
                 start: np.ndarray,
                 frame_rate: int = 24,
                 render_mode=None):
        """
        Initializes a GridWorld generated from world-tensor.
        """

        self.env_width, self.env_height = world.shape  # The size of the rectangular grid
        self.world = world
        self.terminal_states = terminal_dict
        self.start_state = start
        self.action_map = action_map
        self.metadata["render_fps"] = frame_rate
        self.window_size = 512  # The size of the PyGame window

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2,
        # i.e. MultiDiscrete([size, size]).
        self.env_size = world.shape.numpy()
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.MultiDiscrete(self.env_size),
                "target": spaces.MultiDiscrete(self.env_size),
            }
        )

        # We have 4 actions, corresponding to "right", "up", "left", "down", "right"
        self.action_space = spaces.Discrete(4)

        """
        The following dictionary maps abstract actions from `self.action_space` to 
        the direction we will walk in if that action is taken.
        i.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_direction = action_map

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def _get_obs(self):
        return {"agent": self._agent_location, "targets": self._target_locations}

    def _get_info(self):
        return {
            "distance": np.linalg.norm(
                self._agent_location - self._target_locations, ord=1
            )
        }

    def _is_obstacle(self, x, y):
        if self.world[y, x] == 1:
            return True
        else:
            return False

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        self._agent_location = self.start_state
        self._target_locations = []

        for location in self.terminal_states.keys():
            self._target_locations.append(location)

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action):
        # Map the action (element of {0,1,2,3}) to the direction we walk in
        direction = self._action_to_direction[action]
        new_location = np.clip(self._agent_location + direction,
                               np.zeros(shape=direction.size), self.env_size)

        # If acceptable move: move
        if self.world[new_location] != 1:
            self._agent_location = new_location
        # If unacceptable move: NoOp
        else:
            self._agent_location = self._agent_location
        # An episode is done iff the agent has reached the target
        terminated = self._agent_location in self._target_locations
        reward = self.terminal_states[self._target_locations] if terminated else 0  # Binary sparse rewards
        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, False, info

    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()

    def _render_frame(self):
        square_pixel_size = 52
        ground_color: int = 0x969696
        obstacle_color: int = 0
        agent_color: int = 0xC80000

        square_pixel_dims = [square_pixel_size, square_pixel_size]
        win_width = self.env_width * square_pixel_size
        win_height = self.env_height * square_pixel_size
        env_height = self.env_height
        env_width = self.env_width

        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((win_width, win_height))
            pygame.display.set_caption("GridWorld")
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((win_width, win_height))
        canvas.fill(ground_color)

        # Draw obstacles and grid
        for y in range(env_height):
            pygame.draw.line(
                canvas,
                obstacle_color,
                (0, square_pixel_size * y),
                (win_width, square_pixel_size * y),
                width=3,
            )
            for x in range(env_width):
                if y == 0:
                    pygame.draw.line(
                        canvas,
                        obstacle_color,
                        (square_pixel_size * x, 0),
                        (square_pixel_size * x, win_height),
                        width=3,
                    )
                if self._is_obstacle(x, y):
                    loc = np.array([x, y])
                    pygame.draw.rect(
                        canvas,
                        obstacle_color,
                        pygame.Rect(square_pixel_dims * loc, square_pixel_dims),
                    )

        # Draw agent
        pygame.draw.rect(
            canvas,
            agent_color,
            pygame.Rect(square_pixel_dims * self.agent_loc, square_pixel_dims),
        )

        if self.render_mode == "human":
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()
            self.clock.tick(self.metadata["render_fps"])
        else:
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()
