import numpy as np
from typing import Any, Tuple

def strategy(history: np.ndarray, memory: Any) -> Tuple[int, Any]:
    if history.shape[1] % 4 < 2:
        return 1, None
    else:
        return 0, None