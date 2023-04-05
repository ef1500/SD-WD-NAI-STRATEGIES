# Lora for dummies
## Presented by: EF1500

### Table of contents
- [Getting Started](#Getting-Started)
- [Creating a dataset](#Creating-dataset)

<a name="Getting-Started"></a>
# Getting Started
Before you get started, there are a few things you will need:
- Enough disk space to fit all your hopes and dreams
- Patience, because training a model takes time (and so does waiting for results)
- A functioning brain
- Lots of free time

Now that you're ready to go, let's talk models. They're the key to success in Lora. Your choice of model will affect everything from how you prompt your images to what the output looks like to how your Lora will function. Some of their key roles include:
- How you prompt your images
- What the output is going to look like
- How your Lora will function

From my observations, using embeddings and lora on models with the same overall style, like "anime" styles usually seem to be interchangeable. For example, you can use the same prompt on different models without any issues, and it will (more or less) look the same. 

From what I've seen, using embeddings and Lora on models with similar styles usually works interchangeably. So go ahead and grab a few checkpoints to play around with. Some good ones are:
- Counterfiet
- abyssorangemix
- meinamix meina
- anything V4

You can find these models on a site like [Civitai](https://civitai.com/).
Once you've got your models, experiment with them. Have some fun, try different prompts, and get a feel for each one. It may seem like a waste of time, but trust me, it'll pay off in the end.

With that out of the way, let's get you ready for training. To get started, you're gonna want to install the [sd-dreambooth extension](https://github.com/d8ahazard/sd_dreambooth_extension) for your Automatic1111 webui. 

***NOTE***: To avoid yourself a ridiculous amount of headbanging, you have to move the .bat file to the folder your original webui.bat file is located and run it from there. Don't be stupid like me and struggle for an hour trying to run it from the sd-dreambooth folder.

Okay, hopefully you figured out how to install that. This is a guide for Lora so I'm not gonna spend time on tech support.

Anyways, let's move on.

<a name="Creating-dataset"></a>
# Creating a dataset
Finally, getting into the real stuff. 

### Part I: STRUCTURING YOUR FOLDERS
This part is optional, but it'll make your life a lot easier. Lora has something called "concepts," which are just fancy words for categories. You can train Lora with as many different concepts as you want, but for now, we'll stick to one or two.

1. Create a folder for your dataset and give it a simple name, like "LOWRES_SYNTHWAVE."
    - The format for creating a concept folder can be anything, but keep it simple. Don't confuse yourself.
2. Within that folder, create three subfolders:
    - "IMGS" for all the images you want to use in your dataset
    - "HIGHRES_CONCEPT" for your processed high-res images
    - "LOWRES_CONCEPT" for your processed low-res images
Your setup should look like so:
```bash
DATASET-NAME
├──IMGS
├──HIGHRES_CONCEPT
└──LOWRES_CONCEPT
```
This structure will make it easy to expand or combine your dataset later on. Plus, it'll keep you organized and less confused. And who doesn't want that?

Now that you've got your folder structure set up, it's time to fill it with images. Happy hunting!

## Part II: GATHER TRAINING MATERIAL
Before diving balls deep into training your LoRA, remember this: garbage in, garbage out. The AI isn't a genius, it's only as good as the art and prompts you feed it.

Here's how to gather your training material:

1. Download as much official art as possible - The more the better
    - A stellar site for getting official art is danbooru. Use the "official_art" tag.
    
    **NOTE: Always download the largest size image. Trust me, you want the full size.**

2. Try to stay consistent with your artstyles. If you are doing multiple artstyles/concepts (Almost like that's what they're named for!)
As mentioned earlier, the AI isn't a genius. If you give the AI artstyles that are vastly different from one another in the same concept file, the AI will become "confused", and it will give you garbage. So do your best to stay as consistent as possible when it comes to
the artstyle, it will pay off immensely.

***NOTE***: Make sure to put everything you don't want in the Lora output in the text file. You're teaching the AI to make something new, so it will absorb any details that aren't in the text file. Trust me, it's a simple trick that will save you a lot of headaches. Personally I've had very beautiful results come from this method, but you don't have to do it like this. The world of how to train your LoRA is pretty opinionated; everyone has their opinion of what looks good and what doesn't. This is what I think looks best.


***NOTE***: Quality over quantity. These aren't embeddings, they're LoRA. I've seen LoRA work perfectly with only 20 images, and I've seen ones that failed horribly with 1000+ images. It all depends on how well you describe what you don't want in your LoRA output.

## Training/Usage/etc. pointers

### Training Process
For training, here's a few screencaps I've put together explaining the process:
1. You start off by creating a new dreambooth model.
![Model Creation](https://imgur.com/HqfJaXl.png)

2. Then, you're going to want to go over to the settings pane and click on Performance Wizard. This will set everything to what works best on your system. Here's an explanation of the important things:
![Explanation](https://imgur.com/XrjCfQv.png)

3. Now, you're going to want to click that little 'advanced' tab and pop out the advanced options. Here's the screencap showing and explaining this pane:
![Details](https://imgur.com/mRJQLcF.png)

Here's how to find the number of tokens that your prompt is using:
![Tokens](https://imgur.com/crftUwL.png)

4. Now, you're gonna want to set up your concepts. Here's the screencap explaining the different details of the concepts pane:
![Concepts](https://imgur.com/s7igbPx.png)

5. Now, click the 'Saving' tab. This tab is pretty self explanitory, here's what it looks like:
![Saving Pane](https://imgur.com/saYZS0g.png)

6. BOMBS AWAY! Time to start training! Here's what that should look like:
![Training Start](https://imgur.com/qAMfFmF.png)

### Training Pointers / etc.

Now, onto the good stuff: training pointers for LoRA. After training a bunch of these things, I've learned a thing or two. Here are some tips to help you get better generations:

1. Use Cosine Annealing or Cosine with Restarts. They work like a charm.
    - If your model is melting, it's either your training rate or your cosine scale that's messed up. It's usually the former, so adjust your learning rate accordingly.
    - Alternatively, stop the training when it looks good. Yes, it requires babysitting, but it's worth it for high-quality results.

    An example of babysitting (The samples folder for the dreambooth model):
    ![babysitting](https://imgur.com/pmG2sK5.png)

2. What to do if your model is fried and you don't want to retrain:
    - Lower the strength of the LoRA until it looks good.
    - Manipulate the CFG to give the model more freedom. Yes, it may result in more garbage, but it can help salvage a burned model.
    - Suck it up and retrain. It's always the better option.

3. HOW DO I EXTRACT THE LORA FROM THE .PT FILE WTF
    - Calm down, don't panic. It's an easy fix. I have written an extension of my own that I use to extract the LoRA so I can use it with other models. You can find it in the scripts folder of this repository. You are going to want to add it to your extensions folder and restart the webui. One gripe that I have is that I have no idea how to add a stupid refresh button so you're gonna have to restart the WHOLE thing when your lora is finished so you can use the extractor. The UI should be pretty straight forward. The base model is the model you trained your lora on, and the lora model is the lora .ckpt/.safetensors file outputted by the dreambooth extension. Fill out all of the boxes according to how you trained your model and then create a name for the output lora file and hit the extract button. The extension should extract the LoRA from the base model and now you can use the lora wherever you want in your prompts.

    Here's what that should look like:

    ![Lora Extraction](https://imgur.com/WVcO43f.png)

4. For anime models, train on NAI or ANYTHING V4. These aren't mixes and they're base models, great for training your LoRA's on.
