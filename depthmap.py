import gradio as gr
from pathlib import Path
import os
import subprocess
import sys
import urllib.request
if not os.path.exists("Depth-Anything-V2/run_video.py"):
    subprocess.run(["git","clone","https://github.com/DepthAnything/Depth-Anything-V2.git"], check=True)
    os.makedirs('outputs', exist_ok=True)
    os.makedirs("Depth-Anything-V2/checkpoints", exist_ok=True)
    urllib.request.urlretrieve(
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Large/resolve/main/depth_anything_v2_vitl.pth?download=true",
    "Depth-Anything-V2/checkpoints/depth_anything_v2_vitl.pth")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True, cwd="Depth-Anything-V2")

def gen_depth(input_file,grey,pred_check,input_size):
    output_dir = os.path.abspath("outputs")
    output_file = Path(output_dir) / (Path(input_file).stem + ".mp4")
    input_file = os.path.abspath(input_file)
    cmd=[
                sys.executable,
                "run_video.py",
                "--encoder", "vitl",
                "--video-path", input_file,
                "--outdir", output_dir,
            ]
    if grey:
        cmd.append("--grayscale")
    if pred_check:
        cmd.append("--pred-only")
    cmd += ["--input-size", str(input_size)]
    result = subprocess.run(cmd, cwd="Depth-Anything-V2")

    if result.returncode == 0 or output_file.exists():
        return str(output_file)
        
    else:
        raise gr.Error(f"Processing failed:\n{result.stderr[-500:]}")
demo=gr.Interface(fn=gen_depth,inputs=[gr.Video(label="Input video"),
gr.Checkbox(label='greyscale',value=True),gr.Checkbox(label='comparision off?(0.5x size)',value=True),
gr.Slider(minimum=308,maximum=980,step=14,value=518)],
outputs=gr.Video(label="Depthed"))
demo.launch(allowed_paths=[os.path.abspath("outputs")]) 