import nltk
import language_check

def spell_check(t):
    text=t
    tool=language_check.LanguageTool('en-us')
    matches=tool.check(text)
    text=language_check.correct(text,matches)
    return text

