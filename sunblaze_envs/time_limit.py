from gym.wrappers.time_limit import TimeLimit as TimeLimitBase

class TimeLimit(TimeLimitBase):
    """Updated to support reset() with reset_params flag for Adaptive"""

    def reset(self, reset_params=True):
        self._elapsed_steps = 0
        return self.env.reset(reset_params)
