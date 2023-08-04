import tomlkit

with open(r"C:\Users\killer\Desktop\daw\Folder Manager Config.toml", "rb") as f:
    parsed_toml = tomlkit.load(f)
title = parsed_toml["title"]
minsize = (parsed_toml["GUI"]["Geometry"]["minsize"][0],
           parsed_toml["GUI"]["Geometry"]["minsize"][1])
maxsize = (parsed_toml["GUI"]["Geometry"]["maxsize"][0],
           parsed_toml["GUI"]["Geometry"]["maxsize"][1])
icon = parsed_toml["GUI"]["icon"]
background = parsed_toml["GUI"]["background"]
background_geometry = (parsed_toml["GUI"]["background_geometry"]
                       [0], parsed_toml["GUI"]["background_geometry"][1])
button_font = (parsed_toml["GUI"]["Buttons"]["font"][0], parsed_toml["GUI"]
               ["Buttons"]["font"][1], parsed_toml["GUI"]["Buttons"]["font"][2])
button_color = parsed_toml["GUI"]["Buttons"]["color"]
button_hovercolor = parsed_toml["GUI"]["Buttons"]["hovercolor"]
button_bordercolor = parsed_toml["GUI"]["Buttons"]["bordercolor"]
button_textcolor = parsed_toml["GUI"]["Buttons"]["textcolor"]
button_borderwidth = parsed_toml["GUI"]["Buttons"]["borderwidth"]
entry_color = parsed_toml["GUI"]["Entry"]["color"]
entry_bordercolor = parsed_toml["GUI"]["Entry"]["bordercolor"]
entry_textcolor = parsed_toml["GUI"]["Entry"]["textcolor"]
entry_font = (parsed_toml["GUI"]["Entry"]["font"][0], parsed_toml["GUI"]
              ["Entry"]["font"][1], parsed_toml["GUI"]["Entry"]["font"][2])
label_color = parsed_toml["GUI"]["Label"]["color"]
label_font = (parsed_toml["GUI"]["Label"]["font"][0], parsed_toml["GUI"]
              ["Label"]["font"][1], parsed_toml["GUI"]["Label"]["font"][2])
checkbox_font = (parsed_toml["GUI"]["Checkbox"]["font"][0], parsed_toml["GUI"]
                 ["Checkbox"]["font"][1], parsed_toml["GUI"]["Checkbox"]["font"][2])
