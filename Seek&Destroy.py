__author__ = 'debowin'
import re

def main():
    """
    Performs a find operation for a search text in a given input string and highlights the results within
    <b></b> tags. Also, provides features to match whole word and case insensitivity.
    """
    ip_text = raw_input('Where to look for? ')
    src_text = raw_input('What to look for? ')
    whole_words = raw_input('Whole words only?(y/n) ')
    case_sensitive = raw_input('Case Sensitive?(y/n) ')
    if(case_sensitive=='n'):
        src_text = '(?i)'+src_text # Case Insensitive flag
    if(whole_words=='y'):
        src_pattern = re.compile(r'\b('+src_text+r')\b')
    else:
        src_pattern = re.compile(src_text)
    # print(srcpattern.pattern)
    newtext = re.sub(src_pattern,r'<b>\1</b>',ip_text) # To handle the case when src_text contains (?i)
    if newtext != ip_text:
        # Match(es) found!
        print 'Match(es) enclosed with <b></b> tags...'
        print newtext
    else:
        # Hard Luck!
        print 'No matches found...'

if __name__ == "__main__":
    main()