# coding:utf-8
"""
Class : sublime.View
Methods : expand_by_class(point | region, classes, <separators>)
Return Value : sublime.Region
Description : Expands point|region to the left and right, until each side lands on a location that matches classes. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
"""


import sublime
import sublime_plugin

# more flag:
#
# 	sublime.CLASS_WORD_START
# 	sublime.CLASS_WORD_END
# 	sublime.CLASS_PUNCTUATION_START
# 	sublime.CLASS_PUNCTUATION_END
# 	sublime.CLASS_SUB_WORD_START
# 	sublime.CLASS_SUB_WORD_END
# 	sublime.CLASS_LINE_START
# 	sublime.CLASS_LINE_END
# 	sublime.CLASS_EMPTY_LINE


class ViewExpandByClassCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('Test View method: expand_by_class')
        self.expand_word()

    # 向左向右扩展region区域，截止到 flag，例如： sublime.CLASS_WORD_END
    # use point param ( also region param can do that )
    def expand_word(self):
        r = self.view.sel()[0]
        # print(r)
        point = r.b
        classes = sublime.CLASS_WORD_END
        region = self.view.expand_by_class(point, classes)
        # print(region)
        self.view.sel().clear()
        self.view.sel().add(region)
        self.view.show(region)

    # 向左向右扩展region区域，截止到 flag，例如： sublime.CLASS_LINE_END
    # use region param ( also point param can do that )
    def expand_line(self):
        r = self.view.sel()[0]
        # print(r)
        classes = sublime.CLASS_LINE_END
        region = self.view.expand_by_class(r, classes)
        # print(region)
        self.view.sel().clear()
        self.view.sel().add(region)
        self.view.show(region)
