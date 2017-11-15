# coding:utf-8
"""
Class : sublime.View
Methods : find_by_class(point, forward, classes, <separators>)
Return Value : sublime.Region
Description : Finds the next location after point that matches the given classes. If forward is False, searches backwards instead of forwards. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.
"""


import sublime
import sublime_plugin


class ViewFindByClassCommand(sublime_plugin.TextCommand):

        # more Flag:
        #
        # sublime.CLASS_WORD_START
        # sublime.CLASS_WORD_END
        # sublime.CLASS_PUNCTUATION_START
        # sublime.CLASS_PUNCTUATION_END
        # sublime.CLASS_SUB_WORD_START
        # sublime.CLASS_SUB_WORD_END
        # sublime.CLASS_LINE_START
        # sublime.CLASS_LINE_END
        # sublime.CLASS_EMPTY_LINE

    def run(self, edit):
        print('Test View method : find_by_class')
        self.next_word()

    # jump to next word
    def next_word(self):
        region = self.view.sel()[0]
        # print(region)
        point = region.b
        classes = sublime.CLASS_WORD_START
        next_region = self.view.find_by_class(point, True, classes)
        # print(next_region)
        self.view.sel().clear()
        self.view.sel().add(next_region)
        self.view.show(next_region)

    # jump to last word
    def last_word(self):
        region = self.view.sel()[0]
        # print(region)
        point = region.b
        classes = sublime.CLASS_WORD_START
        next_region = self.view.find_by_class(point, False, classes)
        # print(next_region)
        self.view.sel().clear()
        self.view.sel().add(next_region)
        self.view.show(next_region)

    # jump to next line start
    def next_line(self):
        region = self.view.sel()[0]
        # print(region)
        point = region.b
        classes = sublime.CLASS_LINE_START
        next_region = self.view.find_by_class(point, True, classes)
        # print(next_region)
        self.view.sel().clear()
        self.view.sel().add(next_region)
        self.view.show(next_region)
