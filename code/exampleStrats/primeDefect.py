import numpy as np
from typing import Any, Tuple

def strategy(history: np.ndarray, memory: Any) -> Tuple[int, Any]:
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return 0
        for i in range(3, int(np.sqrt(n)) + 1, 2):
            if n % i == 0:
                return 0
        return 1
    return is_prime(history.shape[1]), None