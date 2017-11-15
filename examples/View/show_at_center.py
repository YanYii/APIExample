# coding:utf-8
"""
Class : sublime.View
Methods : show_at_center(location)
Return Value : None
Description : Scroll the view to center on the location, which may be a point or Region.
"""


import sublime
import sublime_plugin


class ViewShowAtCenterCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.show_end_at_center()

    # Test case
    def show_end_at_center(self):
        point = self.view.size()
        self.view.show_at_center(point)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(point, point))

    # Test case
    def show_center(self):
        center = self.view.size() / 2
        self.view.show_at_center(center)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(center, center))
