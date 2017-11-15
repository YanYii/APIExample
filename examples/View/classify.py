# coding:utf-8
"""
Class : sublime.View
Methods : classify(point)
Return Value : int
Description :  Classifies point, returning a bitwise OR of zero or more of these flags:
                    sublime.CLASS_WORD_START
                    sublime.CLASS_WORD_END
                    sublime.CLASS_PUNCTUATION_START
                    sublime.CLASS_PUNCTUATION_END
                    sublime.CLASS_SUB_WORD_START
                    sublime.CLASS_SUB_WORD_END
                    sublime.CLASS_LINE_START
                    sublime.CLASS_LINE_END
                    sublime.CLASS_EMPTY_LINE
"""


import sublime
import sublime_plugin


class ViewClassifyCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('--------------------------------------------------------')
        print('Defualt Flag value :')
        print('')

        print('    sublime.CLASS_WORD_START           :  ' +
              str(sublime.CLASS_WORD_START))
        print('    sublime.CLASS_WORD_END             :  ' +
              str(sublime.CLASS_WORD_END))
        print('    sublime.CLASS_PUNCTUATION_START    :  ' +
              str(sublime.CLASS_PUNCTUATION_START))
        print('    sublime.CLASS_PUNCTUATION_END      :  ' +
              str(sublime.CLASS_PUNCTUATION_END))
        print('    sublime.CLASS_SUB_WORD_START       :  ' +
              str(sublime.CLASS_SUB_WORD_START))
        print('    sublime.CLASS_SUB_WORD_END         :  ' +
              str(sublime.CLASS_SUB_WORD_END))
        print('    sublime.CLASS_LINE_START           :  ' +
              str(sublime.CLASS_LINE_START))
        print('    sublime.CLASS_LINE_END             :  ' +
              str(sublime.CLASS_LINE_END))
        print('    sublime.CLASS_EMPTY_LINE           :  ' +
              str(sublime.CLASS_EMPTY_LINE))

        print('')
        print('--------------------------------------------------------')
        print('Current Flag Value: ')
        print('')

        region = self.view.sel()[0]
        flag = self.view.classify(region.b)

        print('    flag & sublime.CLASS_WORD_START           :  ' +
              str(flag & sublime.CLASS_WORD_START))
        print('    flag & sublime.CLASS_WORD_END             :  ' +
              str(flag & sublime.CLASS_WORD_END))
        print('    flag & sublime.CLASS_PUNCTUATION_START    :  ' +
              str(flag & sublime.CLASS_PUNCTUATION_START))
        print('    flag & sublime.CLASS_PUNCTUATION_END      :  ' +
              str(flag & sublime.CLASS_PUNCTUATION_END))
        print('    flag & sublime.CLASS_SUB_WORD_START       :  ' +
              str(flag & sublime.CLASS_SUB_WORD_START))
        print('    flag & sublime.CLASS_SUB_WORD_END         :  ' +
              str(flag & sublime.CLASS_SUB_WORD_END))
        print('    flag & sublime.CLASS_LINE_START           :  ' +
              str(flag & sublime.CLASS_LINE_START))
        print('    flag & sublime.CLASS_LINE_END             :  ' +
              str(flag & sublime.CLASS_LINE_END))
        print('    flag & sublime.CLASS_EMPTY_LINE           :  ' +
              str(flag & sublime.CLASS_EMPTY_LINE))
        print('')
        print('--------------------------------------------------------')
        print('flag ：' + str(flag))
