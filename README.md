# Wallzy

## Description

Wallzy is a "wallpaper API" to help you find great new wallpapers from a curated collection of images. Over the years, I've developed sort of a hobby of collecting interesting wallpapers and I wanted a convenient way to share them with friends. Hence, this API.

The API provides functionalities to search for and retrieve images based on various categories and tags. There are currently 200 images in the collection, all of which I have manually tagged. So please don't mind if you think an image is wrongly tagged. In a task like this, some subjective opinions were bound to creep in!

Finally, I just want quickly point that this "API" directly serves image URLs instead of the JSON content typically returned by traditional web APIs.

## Deployment

The API is currently deployed on [Render](https://render.com) using its free tier. You can access the deployment at: [https://wallzy.onrender.com](https://wallzy.onrender.com)

There's just one caveat with Render's free tier: it spins down the server after 15 minutes of inactivity and starts it back up when a new request comes in, which can take a minute or so. While I try to keep it active by running a script that pings the API every so often, you may find that it is taking a while to respond. Don't worry, it will come online soon after you've made a request.

You can also choose to run the API [locally](#running-locally).

## API Endpoints

The API is meant to be self-discoverable and as such visiting the root of the API tells you everything you need to know including the supported endpoints and example usage.
Currently, the API has the following endpoints each of which correspond to a tag.

+ `/nature` 
+ `/ghibli`
+ `/city`
+ `/abstract`
+ `/painting`
+ `/digital_art`
+ `/comfy`
+ `/best`

For example, visiting the `/nature` endpoint returns a random image tagged "nature" from the collection.

There are also two special endpoints : `/random` and `/intersection`.

Visiting `/random` returns a completely random image from the collection. It is not restricted to any particular tag.

And `/intersection` allows you to do an intersection of tags using query parameters and returns a random image from the images that match all of your specified tags.

For example, you can visit the endpoint : `/intersection/?tags=nature&tags=painting` to get a random image that has both the tags "nature" and "painting".
This endpoint supports a variable number of tags so you can supply more than two. The API will let you know when an intersection was empty.

## Usage

You can start using the API with your browser via the [render deployment](https://wallzy.onrender.com) or by running it [locally](#running-locally).

If using it in the browser feels cumbersome, then perhaps a better way would be to directly get wallpapers using your terminal with the help of tools like `curl` or `wget`. 
Suppose you want to directly download a random "nature" wallpaper from the API, you can do it with `curl`:

```bash
$ curl -L -o background.jpg https://wallzy.onrender.com/nature
```

Or with `wget`:
```bash
$ wget -O background.jpg https://wallzy.onrender.com/nature
```

## Running Locally

You can always also choose to run the API server locally if the render deployment is down for some reason. Running it locally should always work.

1. Clone the repository:
```bash
git clone https://github.com/dxvsh/wallzy.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```
 
3. Run the API server:
```bash
uvicorn main:app --reload
```

The local server should now be running at: [http://127.0.0.1:8000](http://127.0.0.1:8000).


## Bash Script to automatically set wallpapers 

If you're using the GNOME desktop environment on Linux, I've written a small bash script to fetch and set a wallpaper automatically.

You can download the script `wallzy.sh` from this git repository and use it like so:

1. Make the script executable:

```bash
$ chmod +x wallzy.sh
```

2. Use the script to automatically fetch and set a wallpaper with a given tag:
```bash
$ ./wallzy.sh <tag_name>
```
For example, if you want set a random wallpaper tagged "city" from the API, run:
```bash
$ ./wallzy.sh city
```

Please note that the script only works on the GNOME DE.

And finally, thanks for your interest in this project! I hope it helped you find some good wallpapers!