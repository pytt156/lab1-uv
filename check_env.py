import torch
import pandas as pd
import sklearn
import ipykernel
import sys

print("#### Python version ####")
print(f"Python: {sys.version.split()[0]}")

print(f"""
#### Package versions ####
Torch version: {torch.__version__}
Pandas version: {pd.__version__}
SciKit-Learn version: {sklearn.__version__}
Ipykernel version: {ipykernel.__version__}
""")

print("#### GPU check ####")
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")

if cuda_available:
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    device = "cuda"
else:
    device = "cpu"

print("\n#### Tensor test ####")
a = torch.tensor([1.0, 2.0, 3.0], device=device)
b = torch.tensor([4.0, 5.0, 6.0], device=device)
c = a + b

print(f"Device used: {device} ")
print(f"Result: {c.tolist()}")

print("\nOK!")
