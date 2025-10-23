"""Simple smoke test: import the installed package and print version/info."""
try:
    import mlproject
    print("mlproject import succeeded")
except Exception as e:
    print("mlproject import FAILED:", e)
    raise
