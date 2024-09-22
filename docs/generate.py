import bpy
import sys
import pathlib

try:
    from bl_ext.user_default import molecularnodes as mn
except ImportError:
    try:
        from bl_ext.vscode_development import molecularnodes as mn
    except ImportError:
        import molecularnodes as mn

DOCS_FOLDER = pathlib.Path(__file__).resolve().parent

# import the scripts for building documentation
sys.path.insert(0, str(DOCS_FOLDER))
import noodlenotes


# load the data file which contains all of the nodes to build docs for
bpy.ops.wm.open_mainfile(filepath=mn.blender.nodes.MN_DATA_FILE)


header = """---
toc: true
toc-depth: 2
fig-align: center
---
"""

for submenu in mn.ui.node_menu.menu_items.submenus:
    with open(DOCS_FOLDER / f"nodes/{submenu.name}.qmd", "w") as file:
        file.write(header)
        file.write(f"# {submenu.title}\n\n")
        if submenu.description:
            file.write(submenu.description)
            file.write("\n\n")
        for menu_item in submenu.items:
            if menu_item.is_break:
                continue
            if menu_item.backup is not None:
                name = menu_item.backup
            else:
                name = menu_item.name
            documenter = noodlenotes.MenuItemDocummenter(menu_item)

            file.write(documenter.as_markdown())
            file.write("\n\n")