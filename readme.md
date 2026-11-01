## Requirements

- Python 3.9+
- [Git](https://git-scm.com/) on your PATH
- Internet on first run (~1.3 GB model download)
- NVIDIA GPU with CUDA strongly recommended (CPU works but is very slow)
- Gradio: `pip install gradio`
## Install and run

- git clone https://github.com/A-ad-i/DepthAnythingV2_wrapper.git
- cd DepthAnythingV2_wrapper
- pip install gradio
-python depthmap.py

## Options

| Option | Description |
|---|---|
| **greyscale** | Grayscale depth map instead of colored |
| **comparison off?** | Output only the depth map (half width), not side by side |
| **Input size** | 308-980, Larger is more detailed but slower. Default 518. |

Results are saved to `outputs/`.

## License and credits
- Depth Anything V2 by Lihe Yang et al.: https://github.com/DepthAnything/Depth-Anything-V2 (code is Apache 2.0).
- The **Large** model weights are **CC BY-NC 4.0 (non-commercial only)**; verify on the [model page](https://huggingface.co/depth-anything/Depth-Anything-V2-Large). Weights are not included in this repo and are downloaded from the official source.