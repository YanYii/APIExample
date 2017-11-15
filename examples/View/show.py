# coding:utf-8
"""
Class : sublime.View
Methods : show(location, <show_surrounds>)
Return Value : None
Description : Scroll the view to show the given location, which may be a point, Region or Selection.
"""


import sublime
import sublime_plugin


class ViewShowCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.jump_to_start()

    # Test case
    def jump_to_start(self):
        point = 0
        self.view.show(point)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(point, point))

    # Test case
    def jump_to_end(self):
        point = self.view.size()
        self.view.show(point)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(point, point))
