import bpy

def insert_keyframes(obj, frame, location, rotation):
    obj.location = location
    obj.rotation_euler = rotation
    obj.keyframe_insert(data_path="location", frame=frame)
    obj.keyframe_insert(data_path="rotation_euler", frame=frame)

def setup_camera(location, rotation):
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=location, rotation=rotation)
    camera = bpy.context.object

    bpy.context.scene.camera = camera

    return camera

cube = bpy.context.active_object

if cube and cube.type == 'MESH':
    keyframes = [
        (1, (0, 0, 0), (0, 0, 0)),
        (50, (5, 0, 0), (0, 0, 3.14159/2)),
        (100, (0, 0, 0), (0, 0, 3.14159))
    ]

    for frame, location, rotation in keyframes:
        insert_keyframes(cube, frame, location, rotation)

    camera_location = (30, -25, 20)
    camera_rotation = (1.1, 0, 0.9)
    camera = setup_camera(camera_location, camera_rotation)

    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.filepath = "//renders/rendering_test.mp4"
    bpy.context.scene.render.fps = 24
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 100

    bpy.ops.render.render(animation=True)
else:
    print("No active cube object selected.")
