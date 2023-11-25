def generate_api_docs(base_url):
    api_docs = {
        "API Documentation": {
            "title": "Wallzy - A Curated Wallpaper API",
            "description": "Wallzy is a curated wallpaper 'API' to help you find your favorite new wallpapers.",
            "endpoints": {
                "/random": {
                    "description": "Returns a random image from the collection, could belong to any category.",
                    "url": f"{base_url}random"
                },
                "/nature": {
                    "description": "Images featuring natural elements like forests, mountains, lakes, flowers etc. Present in a variety of art-styles.",
                    "url": f"{base_url}nature",
                },
                "/ghibli": {
                    "description": "Stills captured directly from Studio Ghibli's beautiful movies.",
                    "url": f"{base_url}ghibli",
                },
                "/city": {
                    "description": "Images including bustling cities, quaint towns, buildings, bridges and other architecture.",
                    "url": f"{base_url}city",
                },
                "/abstract": {
                    "description": "Patterns, shapes & colors; experimental and abstract art.",
                    "url": f"{base_url}abstract",
                },
                "/painting": {
                    "description": "Beautiful paintings done in a variety of art forms.",
                    "url": f"{base_url}painting",
                },
                "/digital_art": {
                    "description": "Breathtaking digital artwork, created using tools like Krita, Blender, Photoshop, etc",
                    "url": f"{base_url}digital_art",
                },
                "/comfy": {
                    "description": "Images that evoke a cozy, 'comfy' feeling. Very subjective.",
                    "url": f"{base_url}comfy",                
                },
                "/best": {
                    "description": "My personal favorite images out of the entire collection.",
                    "url": f"{base_url}best",
                },
                "/intersection/": {
                    "description": "Retrieve images based on multiple tags. Only the images matching all of the supplied tags will be considered.",
                    "url": f"{base_url}intersection/?tags=t1&tags=t2",
                    "example_usage": f"{base_url}intersection/?tags=nature&tags=painting&tags=best"
                }    
            }
        }
    }
    return api_docs