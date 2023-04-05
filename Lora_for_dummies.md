# Lora for dummies
## Presented by: EF1500

### Table of contents
- [Getting Started](#Getting-Started)
- [Creating a dataset](#Creating-dataset)

<a name="Getting-Started"></a>
# Getting Started
Before you get started, there are a few things you will need:
- A lot of extra space on your hard disk
- Patience
- A functioning brain
- Lots of free time

Once you're sure you have those things, let's get started for real now. The first thing that you're gonna want to make sure that you have is models. Models are arguable the most crucial part of your endevaour. They will dictate the following:
- How you prompt your images
- What the output is going to look like
- How your Lora will function

From my observations, using embeddings and lora on models with the same overall style, like "anime" styles usually seem to be interchangeable. For example, you can use the same prompt on different models without any issues, and it will (more or less) look the same. 

Get yourself at least three or four additional checkpoints in addition to what you already have. Some suggestions would be:
- Counterfiet
- abyssorangemix
- meinamix meina
- anything V4

You can find these models on a site like [Civitai](https://civitai.com/).
Once you've gathered your models, play around with them for a little while. Don't use it with any embeddings, have some fun, find what looks good, what doesn't etc.; Familiarize yourself with it. You may think this has no impact on your overall quality, but it helps tremendously. For example, I had a few prompts that worked perfectly on NAI, but absolutley break anything v4.5. But since I had familiarized myself with the model, it was an easy fix. No problem.

With that out of the way, let's get you ready for training. To get started, you're gonna want to install the [sd-dreambooth extension](https://github.com/d8ahazard/sd_dreambooth_extension) for your Automatic1111 webui. 

***NOTE***: To avoid yourself a ridiculous amount of headbanging, you have to move the .bat file to the folder your original webui.bat file is located and run it from there. Don't be stupid like me and struggle for an hour trying to run it from the sd-dreambooth folder.

Okay, hopefully you figured out how to install that. This is a guide for Lora so I'm not gonna spend time on tech support.

Anyways, let's move on.

<a name="Creating-dataset"></a>
# Creating a dataset
Finally, getting into the real stuff. 

### Part I: STRUCTURING YOUR FOLDERS
This is optional; more for organization, but has helped me immensely. Very  similar to how we did for the embeddings, but we're gonna name it a little differently.

Basically, LoRA has something called concepts and they're exactly what they seay they are: concetpts. You can train a LoRA with as many different things as you want. For the sake of this simple guide we're gonna boil things down to one or two things.

1. Create a folder for your dataset and name it accordingly (LOWRES_SYNTHWAVE, for example)
    - The format for creating a concept folder can be anything really, but try to stick to something like 1,2,3 or LOWRES/HIGHRES, something simple. Don't confuse yourself.
2. Create three subfolders within the dataset folder.
Your setup should look like so:
```bash
DATASET-NAME
├──IMGS
├──HIGHRES_CONCEPT
└──LOWRES_CONCEPT
```
The IMGS folder will be the folder for all the images you want to use in the dataset. Save your training material to this folder. (Helpful if you want to use it in other places)
The Concept folders are for your processed images. 
I have found that this structure makes it easy to expand, combine- do whatever with the dataset if needed.

## Part II: GATHER TRAINING MATERIAL
Before diving balls deep into training your LoRA, you need to understand that an AI isn't a genius.
What it outputs is a reflection of what you inputted. If you give it garbage, then you're gonna end up with garbage output.

1. Download as much official art as possible - The more the better
    - A stellar site for getting official art is danbooru. Use the "official_art" tag.
    
    **NOTE: Make ABSOLUTELY sure that you are viewing the image's largest size. DO NOT save the preview size, you want the full size, trust me.**

2. Try to stay consistent with your artstyles. If you are doing multiple artstyles/concepts (Almost like that's what they're named for!)
As mentioned earlier, the AI isn't a genius. If you give the AI artstyles that are vastly different from one another in the same concept file, the AI will become "confused", and it will give you garbage. So do your best to stay as consistent as possible when it comes to
the artstyle, it will pay off immensely.

***NOTE***: In the text files from your processing, you want to make absolutely sure that what you want IN THE LORA OUTPUT IS ***NOT*** IN THE TEXT FILE. I REPEAT, NOT IN THE TEXT FILE! You're teaching it to make something new, and it's going to attempt to absorb any details that aren't in the text file that describes your image. So everything you don't want, put in the text file. It will still work if you don't, but not very well. You will get some insane results from that one simple trick.

***NOTE***: Another Note, quality over quantity. These aren't embeddings, they're LoRA. I've had LoRA's work perfectly off of 20 images, and I've had ones that failed horribly with 1000+ images. It's all in how well you are at describing at what you don't want in your LoRA output.

## Training/Usage/etc. pointers

Okay, so now what I wrote this whole thing for: Training pointers.
After training a whole lotta these things I've gotten pretty familiar with the process and I've got a few pointers to give. The default settings should work pretty well for you, but these should help you get at least some edge to make your generations better.

1. Use Cosine Annealing or Cosine with Restarts, they'll work just about every time. 
    - For cosine annealing, I've noticed that there's a lot of correlation between the cosine scale and the output quality. The more images you have, the lower the cosine scale should be. If you have a larger dataset, just use Cos. with restart and set the number of restarts to three. 
    - If you notice that your model is melting, then that means one of two things:
        - Your training rate is screwing you over
        - Your Cosine scale is messed up.
    - It's usually the former of these two and you've probably got a bad training rate. If your model is "melting" then that's a great indicator that you screwed up and you need a better learning rate. If it melts, start over. Alternatively, just stop the training when you think it looks best. This will require some babysitting but it can yield some high quality results if you have the patience for it.

2. What to do if you've got a burned model and you don't wanna retrain it
    - Manipulate the strength of the LoRA and keep lowering it until you think it looks best.
    - Manipulate the CFG to a lower value until you find a value that looks best to you. What this does is gives the model more "freedom". Lowering the CFG may allow for more garbage generations, but if your model is fried it can lend a hand.
    - Suck it up and retrain it anyways because that's always the better option

3. HOW DO I EXTRACT THE LORA FROM THE .PT FILE WTF
    - Calm down, don't panic. It's an easy fix. I have written an extension of my own that I use to extract the LoRA so I can use it with other models. You can find it in the scripts folder of this repository. You are going to want to add it to your extensions folder and restart the webui. One gripe that I have is that I have no idea how to add a stupid refresh button so you're gonna have to restart the WHOLE thing when your lora is finished so you can use the extractor. The UI should be pretty straight forward. The base model is the model you trained your lora on, and the lora model is the lora .ckpt/.safetensors file outputted by the dreambooth extension. Fill out all of the boxes according to how you trained your model and then create a name for the output lora file and hit the extract button. The extension should extract the LoRA from the base model and now you can use the lora wherever you want in your prompts.

4. For anime models, train on NAI or ANYTHING V4. These aren't mixes and they're base models, great for training your LoRA's on.

Uhh I don't know what else to put so yeah, that's it. Thank you thank you