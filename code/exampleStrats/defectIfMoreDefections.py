import numpy as np
from typing import Any, Tuple

def strategy(history: np.ndarray, memory: Any) -> Tuple[int, Any]:
    if history.shape[1] > 0 and np.sum(history[1,:]) < history.shape[1]/2:
        return 0, None
    else:
        return 1, None