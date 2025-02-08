import pygame
import pytmx

def load_tmx_map(tmx_file):
    """Load TMX map using pytmx and return:
       - A pygame.Surface with the rendered tile layers
       - A list of collision rects from the 'ground' object layer
    """
    tmx_data = pytmx.load_pygame(tmx_file, pixelalpha=True)
    tile_width = tmx_data.tilewidth
    tile_height = tmx_data.tileheight

    # Create a surface for the entire map
    # Note: width/height in tiles multiplied by tile dimensions
    map_width = tmx_data.width * tile_width
    map_height = tmx_data.height * tile_height
    map_surface = pygame.Surface((map_width, map_height), pygame.SRCALPHA, 32)

    # Draw all tile layers onto map_surface
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    # (x * tile_width, y * tile_height) is the “pixel” location
                    map_surface.blit(tile, (x * tile_width, y * tile_height))

    # Build a collision list from the 'ground' object layer
    collision_rects = []
    try:
        ground_layer = tmx_data.get_layer_by_name("ground")  # object layer
    except:
        ground_layer = None

    if ground_layer:
        for obj in ground_layer:
            # If the object is a simple rectangle
            if obj.width and obj.height:
                rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                collision_rects.append(rect)
            # If the object is a polyline/polygon
            elif hasattr(obj, "points"):
                # We’ll do a super-basic bounding box approach:
                #   find min_x, min_y, max_x, max_y among the points
                #   create a rectangle from that bounding box.
                points = obj.points
                xs = [p[0] for p in points]
                ys = [p[1] for p in points]
                min_x, max_x = min(xs), max(xs)
                min_y, max_y = min(ys), max(ys)

                # The object's global position offsets all points
                global_offset_x = obj.x
                global_offset_y = obj.y

                bb_width = max_x - min_x
                bb_height = max_y - min_y
                rect = pygame.Rect(
                    global_offset_x + min_x,
                    global_offset_y + min_y,
                    bb_width,
                    bb_height
                )
                collision_rects.append(rect)
            # Otherwise, ignore or handle differently if needed

    return map_surface, collision_rects