api_docs = {
    "API Documentation": {
        "title": "Wallzy - A Curated Wallpaper API",
        "description": "Wallzy is a curated wallpaper 'API' to help you find your favorite new wallpapers.",
        "endpoints": {
            "/random": {
                "description": "Returns a random image from the collection, could belong to any category.",
                "url": "/random"
            },
            "/nature": {
                "description": "Images featuring natural elements like forests, mountains, lakes, flowers etc. Present in a variety of art-styles.",
                "url": "/nature",
            },
            "/ghibli": {
                "description": "Stills captured directly from Studio Ghibli's beautiful movies.",
                "url": "/ghibli",
            },
            "/city": {
                "description": "Images including bustling cities, quaint towns, buildings, bridges and other architecture.",
                "url": "/city",
            },
            "/abstract": {
                "description": "Patterns, shapes & colors; experimental and abstract art.",
                "url": "/abstract",
            },
            "/painting": {
                "description": "Beautiful paintings done in a variety of art forms.",
                "url": "/painting",
            },
            "/digital_art": {
                "description": "Breathtaking digital artwork, created using tools like Krita, Blender, Photoshop, etc",
                "url": "/digital_art",
            },
            "/comfy": {
                "description": "Images that evoke a cozy, 'comfy' feeling. Very subjective.",
                "url": "/comfy",                
            },
            "/best": {
                "description": "My personal favorite images out of the entire collection.",
                "url": "/best",
            },
            "/intersection/": {
                "description": "Retrieve images based on multiple tags. Only the images matching all of the supplied tags will be considered.",
                "url": "/intersection/?tags=t1&tags=t2",
                "example_usage": "/intersection/?tags=nature&tags=painting&tags=best"
            }    
        }
    }
}