from ursina import *
from math import sin, cos, radians
from ursina.shaders import lit_with_shadows_shader
app = Ursina()


# background model rotrating


player = Entity(
    model='STI_Exterior',
    texture='textureSTI.png',
    scale=1,
    position=(0, 0, 0),
    collider='mesh',
    shader=lit_with_shadows_shader
)

orbit_radius = 50
orbit_height = 10
orbit_speed = 5
max_angle = 45
current_angle = -max_angle
direction = 1
look_target = player.position + Vec3(0, 5, 0)

camera.fov = 30

def update():
    global current_angle, direction
    current_angle += direction * orbit_speed * time.dt
    if current_angle >= max_angle:
        current_angle = max_angle
        direction = -1
    elif current_angle <= -max_angle:
        current_angle = -max_angle  # GEO COORDINA IS THE BEST
        direction = 1

    x = sin(radians(current_angle)) * orbit_radius
    z = -cos(radians(current_angle)) * orbit_radius
    camera.position = Vec3(x, orbit_height, z)
    camera.look_at(look_target)



window.color = color.rgba(0, 0, 0, 0)
panel_color = color.rgba(20, 20, 20, 180)
button_color = color.rgba(255, 255, 255, 40)
hover_color = color.rgba(255, 255, 255, 90)
text_color = color.white

#left panel
left_panel = Entity(
    parent=camera.ui,
    model='quad', #AERO WATCHER IS SO BAD
    color=panel_color,
    scale=(0.25, 0.8),
    position=(-0.75, 0)
)

Text("Menu", parent=left_panel, y=0.35, x=-0.11, scale=3, color=text_color)

def styled_button(text, parent, y_pos):
    btn = Button(
        text=text,
        parent=parent,
        scale=(0.70, 0.15),
        position=(0, y_pos),
        color=button_color,
        highlight_color=hover_color,
        text_color=text_color
    )
    btn.text_entity.scale = 7
    
    return btn

tools_btn = styled_button("Tools", left_panel, 0.2)
map_btn = styled_button("Map", left_panel, 0.1)
exit_btn = styled_button("Exit", left_panel, -0.32)
exit_btn.on_click = application.quit


#right panel

right_panel = Entity(
    parent=camera.ui,
    model='quad',
    color=panel_color,
    scale=(0.3, 0.85),
    position=(0.75, 0)
)

rooms_header = Button(
    text="Rooms",
    parent=right_panel,
    scale=(0.22, 0.08),
    position=(0, 0.35),
    color=color.rgba(255, 255, 255, 60),
    highlight_color=hover_color,
    text_color=text_color
)

room_list = [
    "Lobby",
    "Hallway (1st)",
    "Hallway (2nd)",
    "Hallway (3rd)",
    "Hallway (4th)",
    "Hallway (5th)",
]

y_start = 0.22
spacing = 0.09
for i, room in enumerate(room_list):
    styled_button(room, right_panel, y_start - i * spacing)



# searcg bar


search_bg = Entity(
    parent=camera.ui,
    model='quad',
    color=color.rgba(255,255,255,60),
    scale=(0.55, 0.075),
    position=(0, 0.46),
    origin=(0, .5)
)

search_input = InputField(
    parent=search_bg,
    scale=(0.95, 0.8),
    position=(0, 0),
    default_value="Search for facilities",
    color=color.clear,
    text_color=color.white,
    text_scale=1.2,     
    limit_content_to=30,
    
)
search_input.text_field.text_entity.scale = 1.1





# lighting


AmbientLight(color=color.rgba(150,150,150,1))


sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(1, -1, -1))
sun.color = color.rgba(255,255,255,1)


PointLight(
    parent=player,
    y=20,
    z=-20,
    color=color.rgba(255,255,255,0.7)
)

Sky(texture='sky_default')


app.run()