from typing import Callable
import inspect
import functools


def focus_inputs(*controls_name: str) -> Callable:
    """
    ### Enfocar inputs
    
    Decorador para métodos de clase. Válida el valor de cada input. 
    
    - Si un input tiene un valor nulo o vacío, hace focus en el primer focus 
    inválido. 
    
    - Funciona  para sync y async.

    ```python
    @focus_inputs('name', 'password')
    async def handle_submit(self, e):
        pass
    ```
    """
    def decorator(func: Callable) -> Callable:
        is_coro = inspect.iscoroutinefunction(func)

        def _firs_invalid(self, controls):
            items = [getattr(c, "value", None) for c in controls]
            for idx, val in enumerate(items):
                if val is None or ((isinstance(val, str)) and val.strip() == ""):
                    controls[idx].focus()
                    if hasattr(self, "page") and getattr(self, "page") is not None:
                        try:
                            self.page.update()
                        except Exception:
                            pass
                    return True
                return False

        @functools.wraps(func)
        def sync_wrapper(self, e=None, *args, **kwargs):
            controls = [getattr(self, name) for name in controls_name]
            if _firs_invalid(self, controls):
                return
            return func(self, e, *args, **kwargs)

        @functools.wraps(func)
        async def async_wrapper(self, e=None, *args, **kwargs):
            controls = [getattr(self, name) for name in controls_name]
            if _firs_invalid(self, controls):
                return
            return await func(self, e, *args, **kwargs)

        return async_wrapper if is_coro else sync_wrapper

    return decorator
