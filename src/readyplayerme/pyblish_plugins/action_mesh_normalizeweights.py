"""Normalize the skin weights for vertices of meshes in the Blender file."""
import bpy
import pyblish.api

from readyplayerme.pyblish_plugins.shared_funcs import (
    context_window,
    deselect_objects,
    get_mesh_by_name,
    object_from_mesh,
    select_all_bmesh,
)


class MeshNormalizeWeights(pyblish.api.Action):
    """Normalize the skin weights for vertices of meshes in the Blender file."""

    label = "Normalize Weights"
    icon = "percent"
    on = "failedOrWarning"

    @context_window
    def process(self, context, plugin):
        deselect_objects()
        for result in context.data["results"]:
            if plugin == result["plugin"] and not result["action"]:
                instance = result["instance"]
                try:
                    mesh = get_mesh_by_name(instance.name)
                    obj = object_from_mesh(mesh)
                except KeyError as e:
                    self.log.error(f"Action {self.label} failed. Parent of mesh '{instance.name}' not found.")
                    raise ValueError(f"Action '{self.label}' failed for '{instance.name}'.") from e
                bpy.context.view_layer.objects.active = obj
                # Make sure we're in EDIT mode for operator to work.
                bpy.ops.object.mode_set(mode="EDIT")
                select_all_bmesh(mesh)
                bpy.ops.object.vertex_group_normalize_all(lock_active=False)
                bpy.ops.object.mode_set(mode="OBJECT")
                self.log.info(f"Successfully normalized bone influences for '{instance.name}'.")
