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


if torch.cuda.is_available():
    device = torch.device("cuda")
    device_name = torch.cuda.get_device_name(0)
elif torch.backends.mps.is_available():
    device = torch.device("mps")
    device_name = "Apple Metal (MPS)"
else:
    device = torch.device("cpu")
    device_name = "CPU"

print(f"Device selected: {device} ({device_name})")

print("\n#### Tensor test ####")
a = torch.tensor([1.0, 2.0, 3.0], device=device)
b = torch.tensor([4.0, 5.0, 6.0], device=device)
c = a + b

print(f"Result: {c.tolist()}")
print("\nAll good!")
