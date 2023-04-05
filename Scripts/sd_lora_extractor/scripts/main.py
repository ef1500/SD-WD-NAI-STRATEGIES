import modules
from modules.ui import create_refresh_button, setup_progressbar, random_symbol
from modules import sd_hijack, shared
from modules.paths import script_path
from webui import wrap_gradio_gpu_call
from modules import scripts, script_callbacks
from modules import sd_models

from extractor import extract_lora_from_models

import argparse

import gradio as gr
import os
import re


def generate_args_from_dict(passed_args):
    argspace = argparse.Namespace(
        v2=passed_args['v2'],
        save_precision=passed_args['save_precision'],
        model_org=passed_args['model_org'],
        model_tuned=passed_args['model_tuned'],
        save_to=passed_args['save_to'],
        device=passed_args['device'],
        dim=passed_args['dim']
    )
    return argspace

def convert_model_name(model_name):
    rgx = r'\s*\[.*\]'
    return re.sub(rgx, '', model_name)

'''
UI Part
'''

class Script(scripts.Script):
  def __init__(self) -> None:
    super().__init__()

  def title(self):
    return "LoRA Extractor"

  def show(self, is_img2img):
    return scripts.AlwaysVisible

  def ui(self, is_img2img):
    return ()

def extract_model(v2_model, lora_precision, select_model_org, select_lora_model, lora_folder, new_lora_name, lora_output_type, device, delete_old_model, delete_pt_files, delete_dreambooth_model):
    
    
    model_org = convert_model_name(os.path.join('./models/Stable-diffusion/', select_model_org))
    model_tuned = convert_model_name(os.path.join('./models/Stable-diffusion/', select_lora_model))
    
    args = {
        'v2' : v2_model,
        'save_precision': lora_precision,
        'model_org': model_org,
        'model_tuned': model_tuned,
        'save_to': str(os.path.join(lora_folder, 
                                    f"{new_lora_name}.{lora_output_type}")),
        'device': device,
        'dim': 4}
    
    arg_namespace = generate_args_from_dict(args)

    extract_lora_from_models.svd(arg_namespace)
    if delete_old_model:
        os.remove(args['model_tuned'])
    if delete_pt_files:
        for filename in os.listdir(os.path.dirname(args['save_to'])):
            if filename.endswith('.pt') and os.path.splitext(os.path.basename(args['model_tuned']))[0] in filename:
                os.remove(os.path.join(os.path.dirname(args['save_to']), filename))
    if delete_dreambooth_model:
        pass

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as lora_selector:
        with gr.Row().style(equal_height=False):
            with gr.Column():
                with gr.Row():
                    select_model_org = gr.Dropdown(label='Original Model', elem_id="org_model", interactive=True,
                                                                            choices=sd_models.checkpoint_tiles())
                    # Create Refresh Button here
                    select_lora_model = gr.Dropdown(label='LoRA Model', elem_id="lora_model", interactive=True,
                                                                            choices=sd_models.checkpoint_tiles())
                with gr.Row():
                    new_lora_name = gr.Textbox(label='New Lora Name', placeholder="LoRA Name", interactive=True)
                    lora_output_type = gr.Dropdown(label='LoRA Output Type', elem_id="lora_type", interactive=True,
                                                choices=['ckpt', 'safetensors'])
                with gr.Row():
                    lora_precision = gr.Dropdown(label="LoRA Precision", elem_id='lora_precision_type', interactive=True,
                                                                            choices=['bf16', 'fp16', 'float'])
                    device = gr.Dropdown(label='Device', elem_id='device_id', interactive=True,
                                                                            choices=['cuda'])
                    v2_model = gr.Checkbox(label='V2 Model', value=False, interactive=True)

            with gr.Column():
                with gr.Row():
                    delete_old_model = gr.Checkbox(label='Delete old model', value=False, interactive=True)
                    delete_pt_files = gr.Checkbox(label='Delete .pt files in LoRA Folder', value=True, interactive=True)
                with gr.Row():
                    delete_dreambooth_model = gr.Checkbox(label='Delete dreambooth model', value=False, interactive=True)
                    lora_folder = gr.Textbox(label='LoRA folder location', placeholder="LoRA Folder", value="./models/Lora", interactive=True)
                with gr.Row():
                    extract_lora = gr.Button(value="Extract!", variant='primary', interactive=True)
                    
                    
        extract_lora.click(
            fn=extract_model,
            inputs=[
                v2_model,
                lora_precision,
                select_model_org,
                select_lora_model,
                lora_folder,
                new_lora_name,
                lora_output_type,
                device,
                delete_old_model,
                delete_pt_files,
                delete_dreambooth_model],
            outputs = []
        )
                
    return [(lora_selector, "LoRA Extractor", "lora_extractor")]

script_callbacks.on_ui_tabs(on_ui_tabs)