## Dataset Making for Dummies!
***BEFORE YOU READ: This is an extension of Rentry's [article](https://rentry.org/sd-e621-textual-inversion) about textual inversions. Please read it before reading this short guide.***

### **TL;DR: Garbage in = Garbage out**

#### What is this for? Why is this necessary?
This little mini-guide will go over some tips, tricks, and strategies that will help make your life easier and hopefully bring about higher quality results from training your embeddings/hypernetworks. This guide also includes pointers and observations made by various members of the [Holopirates](https://forum.holopirates.moe/) discord server.

### Part I: STRUCTURING YOUR FOLDERS
This is optional; more for organization, but has helped me immensely.
1. Create a folder for your dataset and name it accordingly (HAKOS_BAELZ_DATASET, for example)
2. Create three subfolders within the dataset folder. Name them "IMGS", "DATASET_IMGS", and "SET".
Your setup should look like so:
```bash
DATASET-NAME
├──IMGS
├──DATASET_IMGS
└──SET
```
The IMGS folder will be the folder for all the images you want to use in the dataset. Save your training material to this folder.
The DATASET_IMGS folder is for your cropped images, the images that will be preprocessed and tagged (Part III).
The SET folder is for the actual training set. This is where the results from your tagging should go.
I have found that this structure makes it easy to expand, combine- do whatever with the dataset if needed.

## Part II: GATHER TRAINING MATERIAL
Before diving balls deep into training your hypernetwork/embedding, you need to understand that an AI isn't a genius.
What it outputs is a reflection of what you inputted. If you give it garbage, then you're gonna end up with garbage output.

1. Download as much official art as possible - The more the better
    - A stellar site for getting official art is danbooru. Use the "official_art" tag.
    
    **NOTE: Make ABSOLUTELY sure that you are viewing the image's largest size. DO NOT save the preview size, as they are usually small in
    resolution and when you crop the images in a later step, your image size may be extremely small and will negatively impact your model's
    output.**

2. Try to stay consistent with your artstyles.
As mentioned earlier, the AI isn't a genius. If you give the AI artstyles that are vastly different from one another,
the AI will become "confused", and it will give you garbage. So do your best to stay as consistent as possible when it comes to
the artstyle, it will pay off immensely

***IMPORTANT***: As soknife and Fortune have mentioned, if you are training an artist/artstyle, use art from that artstyle/artist only.

#### A FEW POINTERS:
- Use the "highres" or "absurdres" tag when gathering art. This will ensure that you are getting the highest resolution images avaliable.
- I have found that avoiding extremely detailed images yields better results when processing/tagging the images. Try to find pictures with simple backgrounds and not too much action. This will ensure that the model will focus on your desired subject. You *can* use highly detailed images, but do try to keep it at a minimum. 
- Try to shoot for 200+ Images. You can use less, but do so at your own peril. My best sets have always been the ones with 200+ gathered
images from around the web. Scour the internet, search far and wide, do what you gotta do! 

**Tip: If the image is long and rectangular, save it twice so you can crop either side (or just save it once if you are using a photo
editor/cropper that supports splitting photos in two)**

If you are short on images, and you are training a particular character, it is OK to supplement your training material with less than 
ideal fanart as long as the art resembles the character you are attempting to replicate. Do your best to keep this to a minimum. 
I personally consider this option a last resort, but others have reported decent results with this strategy.

In the case for Hololive characters, for example, there is no "official art". If you find yourself in a similar case, I reccomend doing
your best to find high quality fanart that closely resembles the character that you are trying to replicate. Similar to what I said 
above but here, your training data is contingent on the quality of the fanart. This is where the consistency in the artstyle is key.
**Think of it like this: The output of your model will be a reflection of the combined artstyles and art you have fed the net. Keep this
in mind as you are scouring the web for your training data.**

## PART III: CURATING YOUR DATASET
This is the part where things will become very opinionated, as many people have their own methods for curating and preparing their
dataset. I will simply explain how I have done things, but feel free to experiment and play around with the settings, find what works best for your needs.

If you have the time, now would be a good time to go through your IMGS folder and check for any images that you may have saved that 
could potentially hinder the results of your model. **Remember: The model is a reflection of the combined images' artstyle. You *can* be
more leniant with this rule if you have a smaller number of images and you're using some supplementary fanart as mentioned earlier. **

1. Crop all your images manually using a site like [bulk image crop](https://bulkimagecrop.com/) or your preferred method of cropping. Crop all images to a 1:1 Ratio. 

You *can* have SD do this for you, however in my experiece, the results are not very good. You will bring about much, much better results doing the gruntwork of cropping your images by hand. Have patience! This process can take a bit of time, but the payoff is worth it.

## PART IV: GENERAL OBSERVATIONS

1. As mentioned by soknife, using the "make flipped copies" option when training a character with heterochromia leads to less than 
favorable results. 

2. soknife also mentioned that a 10:1 ratio of sfw/nsfw images leads to very favorable results

3. soknife noted that using 32+ vectors with textual inversions can lead to "melted" features.
    - From my experimentation, using 24 seems to be ideal. Others have said 18 has had substantial results. Anything in the 18-24 range seems to work excellently.

4. If you are getting Out of Memory Errors from CUDA, try restarting the webui with no arguments (not even one!)
I had this issue when training and it took painfully long to figure out.

## PART V: AFTERWORDS
So far, these dataset making techniques seem to work excellent with both hypernetworks and textual inversions.
Special thanks to the Holopirates, who have been tirelessly experimenting, training, and posting about their findings.

There are pretrained textual inversion models made by soknife on the [Holopirates Forum](https://forum.holopirates.moe/t/stable-diffusion-embeds/2103/30?u=soknife)
(Huge thanks to him for making them!)

-ef1500
