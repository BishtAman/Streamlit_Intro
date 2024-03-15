import torch
from diffusers import DiffusionPipeline

model_path = ("../../Models/models--stabilityai--stable-diffusion-xl-base-1.0/snapshots"
              "/462165984030d82259a11f4367a4eed129e94a7b")
base = DiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float32, variant="fp16", use_safetensors=True)


prompt = "A cute cat jumping over a fence"

image = base(prompt=prompt, num_inference_steps=20, guidance_scale=4).image[0]
image.show()
