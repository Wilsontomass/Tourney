import numpy as np
from typing import Any, Tuple

def strategy(history: np.ndarray, memory: Any) -> Tuple[int, Any]:
    if memory is None:
        memory = 1
    if memory == 1 and history.shape[1] > 0 and history[1,-1] == 0:
        memory = 0
    return memory, memory