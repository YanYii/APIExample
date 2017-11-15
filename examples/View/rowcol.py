# coding:utf-8
"""
Class : sublime.View
Methods : rowcol(point)
Return Value : (int, int)
Description : Calculates the 0-based line and column numbers of the point.
"""


import sublime
import sublime_plugin


class ViewRowcolCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        region = self.view.sel()[0]
        row, col = self.view.rowcol(region.b)
        print('select point , row : ' + str(row) + ', col : ' + str(col))
        print('the index of row start by 0')
        print('the index of col start by 0')
